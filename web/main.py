#!/usr/bin/env python3
from html.parser import HTMLParser

import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient


class FrontPageTextGetter(HTMLParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headlining = False
        self.headline = ""

    def handle_starttag(self, tag, attrs):
        is_link = tag == "a"
        is_story = any(attr[0] == "class" and attr[1] == "storylink" for attr in attrs)
        is_first = not self.headline
        if is_link and is_story and is_first:
            self.headlining = True

    def handle_endtag(self, tag):
        self.headlining = False

    def handle_data(self, data):
        if self.headlining:
            self.headline = data


def get_prefix():
    return "The headline is: "


def get_front_page_text(html):
    parser = FrontPageTextGetter()
    parser.feed(html)
    return parser.headline


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        http_client = AsyncHTTPClient()
        response = await http_client.fetch("https://news.ycombinator.com")
        self.write(get_prefix() + get_front_page_text(response.body.decode("utf-8")))


def make_app():
    return tornado.web.Application([(r"/", MainHandler)])


if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
