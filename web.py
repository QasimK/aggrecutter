#!/usr/bin/env python3

import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        http_client = AsyncHTTPClient()
        response = await http_client.fetch('https://news.ycombinator.com')
        self.write("Hello, World! And Aliens!")


def make_app():
    return tornado.web.Application([(r"/", MainHandler)])


if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
