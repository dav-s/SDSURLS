import falcon
import sqlalchemy
import config

app = falcon.API(media_type="text/html")

import routes as rt
import sinks
import hooks

app.add_sink(sinks.sink404)

app.add_route("/{hash}/", rt.Hash())
app.add_route("/l/", rt.Link())
app.add_route("/", rt.Main())

