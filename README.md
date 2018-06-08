# Aggrecutter

A web content/feed aggregator focused on being useful in a content-overloaded environment.

* Aggregate content from more than just RSS/Atom feeds.
* Automatically discover discussions of articles on your forums (e.g. Reddit, Hacker News).
* Allow you to identify and deprioritise low-quality content.
* Make your own notes, categorise/tag, and easily share these.
* Keep track of what you have read like any other feed reader.

## Development

TODO: Compose for DB, worker.
TODO: Docker reload.

    $ vagrant up
    $ vagrant ssh
    $ docker build -t web . -f Dockerfile.web
    $ docker run -it -p 8080:8080 web

    $ docker system prune -f
