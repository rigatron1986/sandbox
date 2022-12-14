from peewee_main import cpeewee as peewee
import re
import uuid

# from versions import Version as GenericVersion

mysql_db = peewee.MySQLDatabase('ple_assets', user='pi', password='admin@321',
                                host='192.168.101.171', port=3306)

print (mysql_db)


class AssetBase(peewee.Model):
    valid_name_matcher = re.compile(r'^[.\-_a-zA-Z0-9]+$')

    class Meta:
        database = mysql_db


class AssetType(AssetBase):
    name = peewee.CharField(max_length=64, unique=True)

    class Meta:
        db_table = 'asset_type'

    def create_asset(self, name, parent=None):
        # assert isinstance(name, basestring), 'parm name must be a string'
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
    label = peewee.CharField(max_length=64)
    new_version_type = peewee.ForeignKeyField(AssetType, on_delete='CASCADE',
                                              on_update='CASCADE', null=True)
    directory = peewee.CharField(unique=True, max_length=128)
    parent = peewee.ForeignKeyField('self', related_name='children', null=True, on_delete='CASCADE',
                                    on_update='CASCADE')

    class Meta:
        db_table = 'assets'
    def __repr__(self):
        if not self:
            return '%s()' %(self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))


class Version(AssetBase):
    asset = peewee.ForeignKeyField(Asset, related_name="versions", on_delete='CASCADE',
                                   on_update='CASCADE')
    asset_type = peewee.ForeignKeyField(AssetType, on_delete='CASCADE', on_update='CASCADE')
    name = peewee.CharField(max_length=64)
    metadata = peewee.TextField(null=True)
    notes = peewee.TextField(null=True)
    status = peewee.CharField(max_length=3, default='WIP')
    date_created = peewee.DateTimeField()
    date_published = peewee.DateTimeField(null=True)

    class Meta:
        indexes = ((['asset', 'name'], True))

    def __repr__(self):
        if not self:
            return '%s()' %(self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))


R = Version.select().join(Asset).where(Asset.name == 'test')
print(Version)
print(dir(R))
print(R)
print(len(R))
for r in R:
    print(r.name)
