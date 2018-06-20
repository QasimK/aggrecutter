# Aggrecutter

A web content/feed aggregator focused on being useful in a content-overloaded environment.

* Aggregate content from more than just RSS/Atom feeds.
* Automatically discover discussions of articles on your forums (e.g. Reddit, Hacker News).
* Allow you to identify and deprioritise low-quality content.
* Make your own notes, categorise/tag, and easily share these.
* Keep track of what you have read like any other feed reader.

## Development

Note that you will likely want `vagrant-notify-forwarder` to watch the filesystem for changes.

* Virtualbox issues: https://www.virtualbox.org/ticket/10660
* Poll mode: https://github.com/facebook/watchman/issues/201
* Resolve virtualbox issues: https://github.com/mhallin/vagrant-notify-forwarder
* But actually not fully: https://github.com/mhallin/vagrant-notify-forwarder/issues/15
* Alternative: https://github.com/gorakhargosh/watchdog


TODO: Compose for DB, worker.

    $ vagrant up
    $ vagrant ssh
    $ make watch


Note some helpful commands:

    # docker run -d -p 8080:8080 --rm web
    $ docker run -it -p 8080:8080 --rm web
    $ docker run -it --rm web /bin/sh
    $ docker system prune -f
    $ docker logs web
    $ docker attach --sig-proxy=false web

(Recall telnet control character is `Ctrl+]`.)
(Docker's quit sequence is `Ctrl+p Ctrl+q`.)
