
from django.db import models
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class CnnVectors(DjangoCassandraModel):
    __keyspace__ = "vector_db_keyspace"

    row_id = columns.Text(primary_key=True)
    attributes_blob = columns.Text()
    body_blob = columns.Text()
    vector = columns.Text()

class Answers(DjangoCassandraModel):
    __keyspace__ = "vector_db_keyspace"

    row_id = columns.UUID(primary_key=True)
    session_id = columns.Integer(index=True)
    question = columns.Text()
    answer = columns.Text()
# python manage.py sync_cassandra

# USE vector_sb_keyspace
# DESCRIBE TABLE answers
# SELECT * from answers;