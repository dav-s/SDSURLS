import falcon
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import config

engine = sqlalchemy.create_engine(config.db_name)
Base = declarative_base()

import models

subdomain_databases = [models.gen_subdomain_table(sd) for sd in config.subdomains]
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

app = falcon.API(media_type="text/html")

import routes as rt
import sinks
import hooks

app.add_sink(sinks.sink404)

app.add_route("/{hash}/", rt.Hash())
app.add_route("/", rt.Main())

