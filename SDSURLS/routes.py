import falcon


class Hash():

    def on_get(self, req, resp, hash):
        resp.status = falcon.HTTP_200
        resp.body = "%s %s\n" % (req.get_header("host"), hash)


class Link():

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "%s %s\n" % (req.get_header("host"), req.get_header("link-url"))