import peewee
import re
from playhouse import fields
import uuid

# import sqlite3
db = peewee.SqliteDatabase(r'D:\scripts\sandbox\peewee_test\test.db')
mysql_db = peewee.MySQLDatabase('ple_assets', user='pi', password='admin@321',
                                host='192.168.101.171', port=3306)
_AssetEntityLink = peewee.Proxy()


class AssetType(peewee.Model):
    name = peewee.CharField(max_length=64, unique=True)

    class Meta:
        database = db

    def create_asset(self, name, parent=None):
        """Create a new asset"""
        assert isinstance(name, basestring), 'param name must be a string'
        assert parent is None or isinstance(parent, Asset), 'param parent must be None or a instance of Asset'
        asset = Asset()
        asset.name = name
        asset.new_version_type = self
        asset.parent = parent
        # asset.directory = uuid.uuid1().hex
        asset.save()

        return asset


class Asset(peewee.Model):
    name = peewee.CharField()
    parent = peewee.ForeignKeyField('self', related_name='children', null=True)
    new_version_type = peewee.ManyToManyField(AssetType)

    class Meta:
        database = db


class Entity(peewee.Model):
    name = peewee.CharField()
    parent = peewee.ForeignKeyField('self', related_name='children', null=True)

    org_assets = peewee.ManyToManyField(Asset)

    class Meta:
        database = db

    @property
    def assets(self):
        # print dir(self.org_assets)
        return self.org_assets.where(Asset.parent.is_null(True))

    def add_basset(self, asset_type_name, basset_name):
        print 'came to add_asset'
        assert asset_type_name is None or isinstance(asset_type_name,
                                                     basestring), 'param asset_type_name must be None or a string'
        assert isinstance(basset_name, basestring), 'param asset_name must be a string'
        asset_names = filter(None, basset_name.split('/'))
        assert len(asset_names) in [1, 2], 'param asset_name can not be decomposed to 1-2 asset names'
        try:
            asset_type = AssetType.get(name=asset_type_name)
        except AssetType.DoesNotExist:
            if asset_type_name is not None:
                raise NameError('Can not find asset type by asset_type_name')
            asset_type = None
        asset = None
        parent = None
        print asset_type
        print asset_names
        # print self.assets
        assets = {a.name: a for a in self.assets}
        print assets


entity_asset_through = Entity.org_assets.get_through_model()
asset_asset_type_through = Asset.new_version_type.get_through_model()
db.connect()
# db.create_tables([Entity])
db.create_tables([Entity, Asset, AssetType, entity_asset_through, asset_asset_type_through])
#
# show_name = Entity(name='AVN')
# show_name.save()
# asset_name = Entity(name='chris', parent=show_name)
# asset_name.save()
# # s_asset = Entity.select().where(Entity.name == 'chris')
# step_name = Entity(name='rig', parent=asset_name)
# step_name.save()
# #
# asset_type1 = AssetType(name='rig:1')
# asset_type1.save()
# asset_type2 = AssetType(name='comp:1')
# asset_type2.save()
#
# # print show_name.children
# # print show_name.children[0].name
# s_asset = Entity.select().where(Entity.name == 'chris')
steps = Entity.select().where(Entity.name == 'rig')
print steps
# print steps[0]
# basset = Asset(name='hand', parent=steps)
# basset.save()

# print dir(steps[0])
asset_type = AssetType.get(name='rig:1')
asset_type.create_asset('body')
# print asset_type.name
# basset_name = Asset(name='hand', parent=steps[0])
# # basset_name.new_version_type.add(asset_type)
# basset_name.save()

# steps[0].org_assets.add(basset_name)
# steps[0].save()

"""

"""
