import peewee

db = peewee.SqliteDatabase(r'D:\scripts\sandbox\peewee_test\ple_db.db')


class BassetType(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = db

    def create_asset(self, name, parent=None):
        # assert isinstance(name, basestring), 'parm name must be a string'
        assert parent is None or isinstance(parent, Basset), 'param parent must be None or a instance of Asset'
        basset = Basset()
        basset.name = name
        basset.new_version_type = self
        basset.parent = parent
        basset.save()
        return basset


class Basset(peewee.Model):
    name = peewee.CharField()
    parent = peewee.ForeignKeyField('self', related_name='children', null=True)
    basset_type = peewee.ManyToManyField(BassetType)

    class Meta:
        database = db


# will have all show, asset, shot, task
class Entity(peewee.Model):
    name = peewee.CharField()
    parent = peewee.ForeignKeyField('self', related_name='children', null=True)
    org_assets = peewee.ManyToManyField(Basset)

    class Meta:
        database = db

    @property
    def assets(self):
        return self.org_assets.where(Basset.parent.is_null(True))

    def add_asset(self, asset_type_name, asset_name):
        assert asset_type_name is None or isinstance(asset_type_name,
                                                     basestring), 'param asset_type_name must be None or a string'
        assert isinstance(asset_name, basestring), 'param asset_name must be a string'
        asset_names = filter(None, asset_name.split('/'))
        assert len(asset_names) in [1, 2], 'param asset_name can not be decomposed to 1-2 asset names'
        try:
            asset_type = BassetType.get(name=asset_type_name)
        except BassetType.DoesNotExist:
            if asset_type_name is not None:
                raise NameError('Can not find asset type by asset_type_name')
            asset_type = None
        asset = None
        parent = None
        assets = {a.name: a for a in self.assets}
        print asset_type.name
        print assets
        print asset_name
        print asset_names

        while True:
            # try:
            #     asset_name = asset_names.pop(0)
            # except IndexError:
            #     break
            print asset_name
            try:
                asset = assets[asset_name]
            except KeyError:
                if not asset_type:
                    raise asset_name
                asset = asset_type.create_asset(asset_name, parent)
                self.org_assets.add(asset)
            else:
                if not asset_names:
                    raise asset  # , self.get_full_name()
                assert asset.parent == parent, "existed asset's parent is different than expected"
            parent = asset
            assets = {a.name: a for a in asset.children}
        return asset


basset_ent = Basset.basset_type.get_through_model()
db.connect()
"""
# db.create_tables([BassetType, Basset, Entity, basset_ent])

# create show
# show = Entity(name='AVN')
# show.save()

# create asset and parent to show
# show = Entity.get(name='AVN')
# asset = Entity(name='roger', parent=show)
# asset.save()

# create task and parent to asset
# asset = Entity.get(name='chris')
# task = Entity(name='rig', parent=asset)
# task.save()
# task = Entity(name='mod', parent=asset)
# task.save()

# create default basset types
# basset_type = BassetType(name='mod:1')
# basset_type.save()
# basset_type = BassetType(name='rig:1')
# basset_type.save()
"""
# create basset with basset type and parent to task
# tasks = Entity.get(name='mod')
# asset = Entity.get(name='chris')
# tasks = Entity.select().where((Entity.name == 'rig') & (Entity.parent == asset)).get()
# print tasks
# basset_type = BassetType.get(name='rig:1')
# print basset_type
# basset = Basset(name='master', parent=tasks)
# basset.save()
# basset.basset_type.add(basset_type)
# basset.save()
tt = Entity.get(name='chris')
print tt
tt.add_asset(asset_type_name='rig:1', asset_name='test')
print dir(tt)
