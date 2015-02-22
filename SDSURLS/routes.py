import falcon
from SDSURLS import subdomain_databases, session, Base


class Main():

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "Welcome to Unkier.com"


class Hash():

    def on_get(self, req, resp, hash):
        resp.status = falcon.HTTP_303
        resp.set_header("Location", "http://daviskr.com")
        resp.body = "Redirecting..."


class Link():

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "%s %s\n" % (req.get_header("host"), req.get_header("link-url"))
