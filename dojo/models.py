from dojo.connectdatabase import ConnectDatabase
from peewee import *


class FlaskDojo(Model):
    storytitle = CharField()
    userstory = TextField()
    criteria = TextField()
    businessvalue = IntegerField()
    estimation = FloatField()
    status = CharField()

    class Meta:
        database = ConnectDatabase.db
