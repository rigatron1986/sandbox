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


db.connect()
asset = Entity.get(name='roger')
tasks = Entity.select().where((Entity.name == 'rig') & (Entity.parent == asset)).get()
print(tasks)
print(tasks.parent.name)
print(dir(tasks))
