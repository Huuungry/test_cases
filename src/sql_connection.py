from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from model import Base
from os import environ


db_server = environ.get('DATABASE_SERVER', "127.0.0.1:65432")

postgres = f"postgres://user:password@{db_server}/test_cases"

def sql_connection():
    engine = create_engine(postgres, echo=False, pool_recycle=2)
    connection = engine.connect()
    meta = MetaData()
    meta.reflect(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return connection, meta, session, engine


connection, meta, session, engine = sql_connection()
metadata = MetaData()
Base.metadata.create_all(engine)
