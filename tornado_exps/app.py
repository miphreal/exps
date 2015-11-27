import tornado.ioloop
import tornado.web
from tornado.options import options

from tornado_conf import setup_settings, settings


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("You requested the main page")


class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)


class MyFormHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/myform" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_argument("message"))


class TmplHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render('templates/tmpl.html', title='Title', items=['1', '2'])


if __name__ == '__main__':
    setup_settings('settings')
    options.parse_config_file('settings/server.cfg', final=False)
    options.parse_command_line()

    print settings.SETTING, settings.setting1

    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/story/([0-9]+)/?", StoryHandler),
        (r'/myform/?', MyFormHandler),
        (r'/template/?', TmplHandler),
    ], **settings)

    application.listen(8087)
    tornado.ioloop.IOLoop.instance().start()
