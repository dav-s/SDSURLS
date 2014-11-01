import falcon
import sqlalchemy
import config

app = falcon.API()

import routes as rt

app.add_route("/l/", rt.Link())
app.add_route("/{hash}/", rt.Hash())

