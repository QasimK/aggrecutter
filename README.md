# Aggrecutter

A web content/feed aggregator focused on being useful in a content-overloaded environment.

* Aggregate content from more than just RSS/Atom feeds.
* Automatically discover discussions of articles on your forums (e.g. Reddit, Hacker News).
* Allow you to identify and deprioritise low-quality content.
* Make your own notes, categorise/tag, and easily share these.
* Keep track of what you have read like any other feed reader.

## Development

Note that you will likely want `vagrant-notify-forwarder` to watch the filesystem for changes.
* https://www.virtualbox.org/ticket/10660
* https://github.com/facebook/watchman/issues/201
* https://github.com/mhallin/vagrant-notify-forwarder


TODO: Compose for DB, worker.

    $ vagrant up
    $ vagrant ssh
    $ make watch


Note some helpful commands:

    $ docker run -it --rm -p 8080:8080 web
    $ docker system prune -f
