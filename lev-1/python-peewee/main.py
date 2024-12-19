from peewee import SqliteDatabase, CharField, DateField, Model, IntegerField

db = SqliteDatabase('teste.db')

class Leaderboard(Model):
    score = IntegerField()
    name = CharField()
    class Meta:
        database = db

db.connect()
db.create_tables([Leaderboard])

Leaderboard.create(score=23, name='ksk')

for scores in Leaderboard.select():
    print(scores:q
          )

