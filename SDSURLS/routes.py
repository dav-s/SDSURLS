import falcon
from SDSURLS import subdomain_databases, session
from config import subdomains
from utils import to_hash, fix_link


class Main():

    def __init__(self):
        f = open("index.html")
        self.index = f.read()

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = self.index

    def on_post(self, req, resp):
        subd = req.get_param("subdomain")
        if subd not in subdomains:
            resp.status = falcon.HTTP_500
            resp.body = "That subdomain doesn't exist."
            return
        link = req.get_param("link")
        link = fix_link(link)
        if len(link) > 512:
            resp.status = falcon.HTTP_500
            resp.body = "That link was too long."
            return
        subd_obj = subdomain_databases[subdomains.index(subd)]
        hash = to_hash(session.query(subd_obj).count()+1)
        link_obj = subd_obj(hash=hash, link=link)
        session.add(link_obj)
        session.commit()
        host = req.host.partition(".")
        host = host[2] if host[2] is not "" else host[0]
        url = "http://"+subd+"."+host+"/"+hash
        resp.status = falcon.HTTP_200
        resp.body = 'SUCCESS! Here is your new url: <a href="'+url+'">'+url+"</a>"


class Hash():

    def on_get(self, req, resp, hash):
        subd = req.subdomain
        if subd not in subdomains:
            resp.status = falcon.HTTP_404
            resp.body = "Subdomain not found."
            return
        if len(hash) > 10:
            resp.status = falcon.HTTP_404
            resp.body = "Link not found."
            return
        link = session.query(subdomain_databases[subdomains.index(subd)]).get(hash)
        if link is None:
            resp.status = falcon.HTTP_404
            resp.body = "Link not found."
            return
        resp.status = falcon.HTTP_303
        resp.set_header("Location", str(link.link))
        resp.body = "Redirecting you to "+str(link.link)
