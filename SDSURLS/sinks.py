import falcon


def sink404(req, resp):
    resp.body = "Page not found."
    resp.status = falcon.HTTP_404
