import tornado.ioloop
import tornado.web
from tornado.options import options

from settings import setup_settings, settings


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('Hello, world')

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == '__main__':
    setup_settings()
    options.parse_config_file('settings/server.cfg', final=False)
    options.parse_command_line()

    print settings

    application.listen(8087)
    tornado.ioloop.IOLoop.instance().start()
