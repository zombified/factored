Changelog
=========

3.0.3 (2014-04-18)
------------------

- url decode for web server plugins to properly check auth tkt

3.0.2 (2014-04-18)
------------------

- better error handling for web server plugins

3.0.1 (2014-04-17)
------------------

- distribution fixes

3.0 (2014-04-17)
----------------

- better docs
- change script names
- ats and nginx plugins


2.2 (2014-04-16)
----------------

- move all form logic to plugin so everything can be overridden

2.1 (2013-06-04)
----------------

- script and template fixes

2.0rc1 (2013-01-31)
-------------------

- more robust multi-use environment with database connections

- support more algorythms for auth ticket

- refactor so it's more modular

- be able to easily customize all templates

- be able to customize text

- pull out auth_tkt module of paste so we can customize a bit

1.1a2 (2012-03-26)
------------------

- specify appname to customize google auth code entry.

- redirect to original url if possible

- be able to provide "remember me" functionality


1.1a1 (2012-03-26)
------------------

- add auto user finder support

- add ability to send google code reminders. This
  can work well with the autouserfinder


1.0a1 (2012-03-23)
------------------

- Initial release
