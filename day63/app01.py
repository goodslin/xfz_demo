import tornado.ioloop
import tornado.web


settings = {
    'template_path': 'templates',
    'static_path': 'static',
}


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class Loginandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login.html", Loginandler),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
