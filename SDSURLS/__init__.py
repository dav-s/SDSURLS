import falcon
import sqlalchemy
import config

app = falcon.API(media_type="application/json")

import routes as rt

app.add_route("/{hash}/", rt.Hash())
app.add_route("/l/", rt.Link())

