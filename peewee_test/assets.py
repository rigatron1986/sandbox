# from peewee_main import cpeewee as peewee
from peewee_main.fields import ManyToManyField
import peewee
import re
import uuid

from errors import NoSuchAssetInEntity
from errors import EntityNotFound
from errors import AssetAlreadyExists

# from versions import Version as GenericVersion

mysql_db = peewee.MySQLDatabase('ple_assets', user='pi', password='admin@321',
                                host='192.168.101.171', port=3306)

print (mysql_db)

_AssetEntityLink = peewee.Proxy()


class AssetBase(peewee.Model):
    valid_name_matcher = re.compile(r'^[.\-_a-zA-Z0-9]+$')

    class Meta:
        database = mysql_db


class AssetType(AssetBase):
    name = peewee.CharField(max_length=64, unique=True)

    class Meta:
        db_table = 'asset_type'  # Needed because of the underscore

    def create_asset(self, name, parent=None):
        """Create a new asset"""
        assert isinstance(name, basestring), 'param name must be a string'
        assert parent is None or isinstance(parent, Asset), 'param parent must be None or a instance of Asset'
        asset = Asset()
        asset.name = name
        asset.new_version_type = self
        asset.parent = parent
        asset.directory = uuid.uuid1().hex
        asset.save()

        return asset


class Asset(AssetBase):
    name = peewee.CharField(max_length=64)
    new_version_type = peewee.ForeignKeyField(AssetType, on_delete='CASCADE',
                                              on_update='CASCADE', null=True)
    directory = peewee.CharField(unique=True, max_length=128)
    parent = peewee.ForeignKeyField('self', related_name='children', null=True, on_delete='CASCADE',
                                    on_update='CASCADE')

    @classmethod
    def class_name(cls):
        return 'BAsset'

    def get_full_name(self):
        if self.parent_id is None:
            return self.name
        return '{}/{}'.format(self.parent.get_full_name(), self.name)


class Entity(AssetBase):
    """Encapsulates DB access and helper functions for Entity"""

    name = peewee.CharField(max_length=64)
    type = peewee.CharField(null=True, max_length=32)
    sub_type = peewee.CharField(null=True, max_length=32)
    parent = peewee.ForeignKeyField('self', related_name='children', null=True)
    org_assets = ManyToManyField(Asset, through_model=_AssetEntityLink, related_name='entities')
    shotside_id = peewee.IntegerField()
    retired = peewee.BooleanField(default=0)
    data_dict = peewee.TextField(null=True)
    root = peewee.ForeignKeyField('self', null=True)

    prodside_id = peewee.IntegerField(null=True, index=True)
    prodside_type = peewee.CharField(null=True, index=True)
    prodside_server_id = peewee.IntegerField(null=True, index=True)

    @classmethod
    def find(cls, full_entity_name):
        if full_entity_name.isdigit():
            return Entity.get(id=full_entity_name)
        else:
            tokens = filter(bool, full_entity_name.split('/'))  # filter is to remove blanks
            tokens.reverse()  # we want to query starting from the tail

            if not tokens:
                raise ValueError('full_entity_name is invalid')

            # we start off with the last entity
            link_alias = Entity.alias()
            query = link_alias.select().where(link_alias.name == tokens[0])

            link_alias_list = [link_alias]
            # then we handle all the middle entities
            for token in tokens[1:]:
                link_alias = Entity.alias()
                link_alias_list.append(link_alias)
                query = query.join(link_alias).where(link_alias.name == token)

            query = query.select(*link_alias_list).where(link_alias.parent.is_null())
            try:
                return query.get()
            except Entity.DoesNotExist:
                raise EntityNotFound(full_entity_name)

    @property
    def assets(self):
        return self.org_assets.where(Asset.parent.is_null(True))

    def add_asset(self, asset_type_name, asset_name):
        assert asset_type_name is None or isinstance(asset_type_name,
                                                     basestring), 'param asset_type_name must be None or a string'
        assert isinstance(asset_name, basestring), 'param asset_name must be a string'
        asset_names = filter(None, asset_name.split('/'))
        assert len(asset_names) in [1, 2], 'param asset_name can not be decomposed to 1-2 asset names'
        try:
            asset_type = AssetType.get(name=asset_type_name)
        except AssetType.DoesNotExist:
            if asset_type_name is not None:
                raise NameError('Can not find asset type by asset_type_name')
            asset_type = None
        asset = None
        parent = None
        assets = {a.name: a for a in self.assets}

        while True:
            try:
                asset_name = asset_names.pop(0)
            except IndexError:
                break

            try:
                asset = assets[asset_name]
            except KeyError:
                if not asset_type:
                    raise NoSuchAssetInEntity(asset_name, self)
                asset = asset_type.create_asset(asset_name, parent)
                self.org_assets.add(asset)
            else:
                if not asset_names:
                    raise AssetAlreadyExists(asset, self.get_full_name())
                assert asset.parent == parent, "existed asset's parent is different than expected"
            parent = asset
            assets = {a.name: a for a in asset.children}
        return asset


r = Entity.select().where(Entity.name == 'chris').get()
q = Entity.select().where(Entity.name == 'AVN').get()
# show = Entity.select().where(Entity.name == 'AVN').get()
show = Entity.find('AVN')
d = Entity.select().where((Entity.name == 'chris') & (Entity.parent == show)).get()
# print r.name
print d.name
step = d.children[0]
print step.name
step.add_asset(asset_type_name='rig:1', asset_name='test')
# print r.parent.name

# print len(r)
# for x in r.parent:
#     print x.name
