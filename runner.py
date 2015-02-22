from SDSURLS import app
import config

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server(config.host, config.port, app)
    httpd.serve_forever()