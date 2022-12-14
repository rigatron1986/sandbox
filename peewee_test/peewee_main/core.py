# -*- coding: utf-8 -*-
import copy
import json
from collections import namedtuple

import cpeewee as peewee
import fields


def _check_connection(db):
    db.connect()
    db.close()


def check_connections():
    from .config import DATABASES, TYPE_POSTGRESQL, TYPE_MYSQL
    from bfx.util.time_handle import call_with_timeout

    database_classes = {
        TYPE_POSTGRESQL: peewee.PostgresqlDatabase,
        TYPE_MYSQL: peewee.MySQLDatabase
    }

    for db_info in DATABASES:
        DatabaseClass = database_classes[db_info["type"]]  # Ignore N806, this actually is a class
        db = DatabaseClass(**db_info["config"])
        try:
            call_with_timeout(
                _check_connection, (db,),
                err_txt="Can't connect to {0} at {1}:{2}! Please contact to PLE or ITD!".format(
                    db.database, db.connect_kwargs["host"], db.connect_kwargs["port"]), wait_time=10)
        except Exception as e:
            print e


def convert_to_dict(peewee_model):
    """
    Returns a safe dictionary representation of a model that will not affect the original model if changed
    """
    return copy.deepcopy(peewee_model._data)


def create_model_dict(members, model_class):
    """
    Creates a dictionary of items that inherit from a given model class

    Args:
        members: The members of the module to be added
        model_class: The model class to restrict the members to

    Returns:
        A dictionary with names and class references for all models of that type.
        For example:

        {
            "Department": Department,
            "Group": Group,
            "Person": Person,
            "Attachment": Attachment,
            "Note": Note,
        }

    """
    models = {}
    for name, obj in members.items():
        try:
            if issubclass(obj, model_class):
                models[name] = obj
        except TypeError:
            pass
    return models


class DeferredRelation(peewee.DeferredRelation):
    """
    The Peewee deferred relations are buggy - they only work the first time. Here we support multiple models.
    """

    def __init__(self, model_name):
        super(DeferredRelation, self).__init__()
        self.field_entries = []
        self.model_name = model_name

    def set_field(self, model_class, field, name):
        FieldEntry = namedtuple("FieldEntry", "model_class field_instance field_name")
        entry = FieldEntry(model_class, field, name)

        if entry not in self.field_entries:
            self.field_entries.append(entry)

    def connect(self, model_dict):
        for entry in self.field_entries:
            # Only connect this field to a subclass of the model it appeared in originally
            try:
                model_class = model_dict[entry.model_class.__name__]
                if not issubclass(model_class, entry.model_class):
                    continue
            except KeyError:
                continue
            field = entry.field_instance.clone()
            field_name = entry.field_name

            if field.to_field:
                to_model = field.to_field.model_class
                to_model_name = to_model.__name__
                new_to_model = model_dict[to_model_name]
                new_to_field = new_to_model._meta.fields[field.to_field.name]
                field.to_field = new_to_field

            field.rel_model = model_dict[self.model_name]
            field.add_to_class(model_class, field_name)


class DeferredThroughModel(DeferredRelation, fields.DeferredThroughModel):
    """
    This supports ManyToManyFields.
    """

    def connect(self, model_dict):
        for entry in self.field_entries:
            # Only connect this field to a subclass of the model it appeared in originally
            try:
                model_class = model_dict[entry.model_class.__name__]
                if not issubclass(model_class, entry.model_class):
                    continue
            except KeyError:
                continue
            field = entry.field_instance.clone()
            field_name = entry.field_name

            field.rel_model = model_dict[entry.field_instance.rel_model.model_name]
            field._through_model = model_dict[self.model_name]
            field.add_to_class(model_class, field_name)


class DeferredEntityDict(DeferredRelation):
    """
    This supports ManyToManyFields.
    """

    def __init__(self, entity_dict):
        super(DeferredRelation, self).__init__()
        self.field_entries = []
        self.entity_dict = entity_dict

    def set_field(self, model_class, field, name):
        FieldEntry = namedtuple("FieldEntry", "model_class field_instance field_name")
        self.field_entries.append(FieldEntry(model_class, field, name))

    def connect(self, model_dict):
        for entry in self.field_entries:
            # Only connect this field to a subclass of the model it appeared in originally
            try:
                model_class = model_dict[entry.model_class.__name__]
                if not issubclass(model_class, entry.model_class):
                    continue
            except KeyError:
                continue
            field = entry.field_instance.clone()
            field_name = entry.field_name

            entity_types = {}
            for key in self.entity_dict:
                try:
                    entity_types[key] = model_dict[self.entity_dict[key]]
                except KeyError:
                    continue

            field.entity_types = entity_types
            field.add_to_class(model_class, field_name)


class DeferredRelationManager(object):
    """
    This utility allows smart connecting of deferred relations based on a dictionary. It also supports subclassing.
    This functionality allows us to define Shotgun models in a common file, along with foreign keys, and then subclass
    these models for specific shotgun instance setups.

    Example:

        # common models

        drm = DeferredRelationsManager()

        class Sequence(peewee.Model):
            shot = ForeignKeyField(drm.model("Shot"))

        class Shot(peewee.Model):
            pass


        # specific models

        class Shot(common.Shot):
            class Meta:
                database = staging_db

        MODEL_DICT = {"Shot": ShotSubclass }

        common.drm.connect_relations(MODEL_DICT)

    """

    def __init__(self):
        super(DeferredRelationManager, self).__init__()
        self.relations = {}
        self.links = {}
        self.dicts = {}

    def model(self, name):
        if name not in self.relations:
            self.relations[name] = DeferredRelation(name)
        return self.relations[name]

    def link(self, name):
        if name not in self.links:
            self.links[name] = DeferredThroughModel(name)
        return self.links[name]

    def dict(self, entity_dict):
        dict_key = json.dumps(entity_dict)
        if dict_key not in self.dicts:
            self.dicts[dict_key] = DeferredEntityDict(entity_dict)
        return self.dicts[dict_key]

    def connect_relations(self, model_dict):
        for relation in self.relations.values():
            relation.connect(model_dict)
        for link in self.links.values():
            link.connect(model_dict)
        for entity_dict in self.dicts.values():
            entity_dict.connect(model_dict)


class EntityForeignKeyFieldDescriptor(peewee.RelationDescriptor):
    def __init__(self, field, rel_model):
        super(EntityForeignKeyFieldDescriptor, self).__init__(field, rel_model)
        self.default_model = self.rel_model

    def __get__(self, instance, instance_type=None):
        if not instance:
            return self.field
        instance_entity_type = getattr(instance, self.field.entity_type_name)
        rel_model = self.field.entity_types.get(instance_entity_type)
        if rel_model:
            self.rel_model = rel_model
            self.field.to_field = self.rel_model._meta.primary_key
            return super(EntityForeignKeyFieldDescriptor, self).__get__(instance)
        return None

    def __set__(self, instance, value):
        self.rel_model = self.default_model
        for entity_type, rel_model in self.field.entity_types.items():
            if isinstance(value, rel_model):
                self.rel_model = rel_model
                self.field.to_field = self.rel_model._meta.primary_key
                setattr(instance, self.field.entity_type_name, entity_type)
                setattr(instance, self.field.entity_id_name, value._get_pk_value())
        super(EntityForeignKeyFieldDescriptor, self).__set__(instance, value)


class ReverseEntityForeignKeyFieldDescriptor(peewee.ReverseRelationDescriptor):
    def __init__(self, entity_type, field):
        super(ReverseEntityForeignKeyFieldDescriptor, self).__init__(field)
        self.entity_type = entity_type

    def __get__(self, instance, instance_type=None):
        if instance:
            return self.rel_model.select().where((self.field.entity_id == getattr(instance, self.field.to_field.name)) &
                                                 (self.field.entity_type == self.entity_type))
        return self


class EntityForeignKeyField(peewee.ForeignKeyField):
    def __init__(self, type_column, entity_types, *args, **kwargs):
        if "rel_model" in kwargs:
            kwargs.pop("rel_model")
        super(EntityForeignKeyField, self).__init__("self", *args, **kwargs)

        self.type_column = type_column
        self.entity_types = entity_types

    def clone_base(self, **kwargs):
        return super(EntityForeignKeyField, self).clone_base(
            type_column=self.type_column, entity_types=self.entity_types, **kwargs)

    def _get_descriptor(self):
        return EntityForeignKeyFieldDescriptor(self, self.rel_model)

    def _add_to_rel_model(self, entity_types):
        self.entity_types = entity_types
        self.related_name = self._get_related_name()
        self.rel_models = entity_types.values()
        for entity_type, model_class in self.entity_types.items():
            setattr(model_class, self.related_name,
                    ReverseEntityForeignKeyFieldDescriptor(entity_type, self))

    def add_to_class(self, model_class, name):
        if isinstance(self.entity_types, peewee.DeferredRelation):
            self.entity_types.set_field(model_class, self, name)
            return
        super(EntityForeignKeyField, self).add_to_class(model_class, name)
        delattr(self.rel_model, self.related_name)

        self.entity_type_name = '{}_type'.format(name)
        self.entity_id_name = '{}_id'.format(name)
        self.entity_type = peewee.TextField(db_column=self.type_column)
        self.entity_id = peewee.IntegerField(db_column=self.db_column)
        self.entity_type.add_to_class(model_class, self.entity_type_name)
        self.entity_id.add_to_class(model_class, self.entity_id_name)
        if self.entity_types:
            self._add_to_rel_model(self.entity_types)

    def __eq__(self, other):
        if isinstance(other, peewee.Model):
            return ((self.entity_type == other.class_name()) &
                    (self.entity_id == other._get_pk_value()))
        elif isinstance(other, peewee.Field):
            return ((self.entity_type == other.model_class.class_name()) &
                    (self.entity_id == other.model_class._meta.primary_key))
        else:
            return ((self.entity_type == self.rel_model.class_name()) &
                    (self.entity_id == other))


class CachedProperty(property):
    def __init__(self, fget, name=None):
        name = name or fget.__name__

        def _fset(obj, value):
            obj._obj_cache[name] = value
            return value

        def _fget(obj):
            try:
                return obj._obj_cache[name]
            except KeyError:
                return _fset(obj, fget(obj))

        def _fdel(obj):
            del obj._obj_cache[name]

        super(CachedProperty, self).__init__(fget=_fget, fset=_fset, fdel=_fdel)

    def getter(self, fget):
        raise DeprecationWarning('getter has been generated by default')

    def setter(self, fset):
        raise DeprecationWarning('setter has been generated by default')

    def deleter(self, fdel):
        raise DeprecationWarning('deleter has been generated by default')


def cached_property(fget_or_name):
    if callable(fget_or_name):
        return CachedProperty(fget=fget_or_name)
    elif isinstance(fget_or_name, str):
        def name_wrapper(fget):
            return CachedProperty(fget=fget, name=fget_or_name)
        return name_wrapper
    else:
        raise TypeError('param of cached_property must be a function or a name')
