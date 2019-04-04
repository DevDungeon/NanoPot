NanoPot Quickstart
==================

NanoPot is a simple TCP honeypot written in Python 3.

Installation
------------

    python -m pip install nanopot

Running
-------

    python -m nanopot


Debian package
--------------

Dowload the package from GitHub release, or
build the Debian package with:

    dpkg-deb --build ./deb nanopot-1.0.0.deb


Install the Debian package with:

    sudo dpkg -i nanopot-1.0.0.deb

Config defaults to `/etc/nanopot.ini`.
Logs will be available in `/var/log/nanopot.log`.

Source Code
-----------

https://github.com/DevDungeon/NanoPot

PyPI package
------------

https://pypi.org/project/nanopot/

Documentation
-------------

https://nanopot.rtfd.io
