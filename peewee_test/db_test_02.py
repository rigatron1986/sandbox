import peewee

db = peewee.SqliteDatabase('ple_db.db')


class BassetType(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = db


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

    class Meta:
        database = db


basset_ent = Basset.basset_type.get_through_model()
db.connect()
db.create_tables([BassetType, Basset, Entity, basset_ent])

# create show
show = Entity(name='AVN')
show.save()

# create asset and parent to show
show = Entity.get(name='AVN')
asset = Entity(name='roger', parent=show)
asset.save()

# create task and parent to asset
asset = Entity.get(name='roger')
task = Entity(name='rig', parent=asset)
task.save()
task = Entity(name='mod', parent=asset)
task.save()

# create default basset types
basset_type = BassetType(name='mod:1')
basset_type.save()
basset_type = BassetType(name='rig:1')
basset_type.save()
#create basset with basset type and parent to task
tasks = Entity.get(name='mod')
asset = Entity.get(name='roger')
tasks = Entity.select().where((Entity.name == 'rig') & (Entity.parent == asset)).get()
print(tasks)
basset_type = BassetType.get(name='rig:1')
print(basset_type)
basset = Basset(name='master', parent=tasks)
basset.save()
basset.basset_type.add(basset_type)
basset.save()
