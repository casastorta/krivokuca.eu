# Krivokuca.eu showcase project #
This project is written to demonstrate author's skills in modern technologies
(Django MVC Python web framework, mobile-first adaptive design methodology,
understanding of relational and nosql database concepts, comfortability
of working with modern javascript libraries like jQuery...)

It is also made to show off how I'm more cool than you, hence what I read
is way more cool than your recently-read library. :-)

## Subprojects ##
Currently, there is only one project under this repository. It is a **Quotes
database**, instance of which is running on
[this site](http://quotes.krivokuca.eu "Quotes").

### Quotes ###
Quotes is an application for holding (and showing off) quotes from various
authors and their books. It can also be used as a small personal database
of books and authors (for any non-personal use, I guess lot of features
would have to be added).

It is basically a showcase of moderately complex Django ORM usage (small
database with couple of many-to-many relations and a few foreign keys).

It contains usable search engine (thanks to Haystack and Whoosh).

To see some of it's features go to:

* [random quote from the database](http://quotes.krivokuca.eu/q/quotes)

  (this is cached for couple of seconds each time to avoid easy DoS
  attacks).

* [single quote view](http://quotes.krivokuca.eu/q/quote/3)

* [sorted database of authors](http://quotes.krivokuca.eu/q/authors)

* [author page](http://quotes.krivokuca.eu/q/author/oscar-wilde)

* [sorted database of books](http://quotes.krivokuca.eu/q/books)

* [single book page](http://quotes.krivokuca.eu/q/the-upgrade)

* [search example](http://quotes.krivokuca.eu/q/search/?q=poem)

* ...and the last but not least, [frontpage](http://quotes.krivokuca.eu/)

## Trying it on your own ##
Sure, you can. [Just follow the wiki instructions](https://github.com/casastorta/krivokuca.eu/wiki/Prerequisites).

### Moving to production environment ###
There are **a lot** of resources but also approaches on migrating
Django site to production. I am not going to suggest you the right way
(this site should work in mostly all scenarios), but
[here is the general idea](https://github.com/casastorta/krivokuca.eu/wiki/Deploying).

## Other opensource projects used in this project ##
This project depends on a lot of other opensource projects. Starting from
the system level up:

* It's running on [Debian](http://debian.org) and
  it's developed on [Fedora](http://fedoraproject.org) linux distributions.

* Obviously, it's written in [Python](http://python.org).

* [Git](http://git-scm.com/) and [git-flow](https://github.com/nvie/gitflow)
  are used in it's development process.

* Code is being edited with [vim](http://www.vim.org/).

* Framework for the site development is
  [Django](https://www.djangoproject.com/).

* Search engine is powered by
  [Whoosh](https://bitbucket.org/mchaput/whoosh/wiki/Home)
  for indexing and keeping the data and
  [Haystack](http://haystacksearch.org/) for the search engine itself.

* For caching purposes, there is [memcached](http://memcached.org/).
  Tools for integrating it into this app are
  [Python memcached mdule](https://github.com/linsomniac/python-memcached)
  and [Django memcache status](https://github.com/bartTC/django-memcache-status)
  3rd party Django component.

* Database schema migrations are always the bitch. Using
  [South](http://south.aeracode.org/) to ease up on those for myself.

* And the web interface frontend relies on
 [Bootstrap](http://getbootstrap.com/) and [jQuery](http://jquery.com/).

## Where is the example site hosted? ##
All of my recommendations (if you're looking for Linux virtual servers
hosting) go to
[Linode](http://www.linode.com/?r=cc319dc896bb711b6c95c54ea42507d982c8a636).

# Plans for the future #
Well, currently I can set the roadmap to couple of features for
[Quotes](http://quotes.krivokuca.eu/) application, you'll see them
as they come.

# Changelog #
[Check the changelog here](https://github.com/casastorta/krivokuca.eu/wiki/Whatsnew).
