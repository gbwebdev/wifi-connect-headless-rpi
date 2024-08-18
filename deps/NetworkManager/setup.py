#!/usr/bin/python

from setuptools import setup

setup(name = "python-networkmanager",
      version = "2.2.1",
      author = "Dennis Kaarsemaker",
      author_email = "dennis@kaarsemaker.net",
      url = "http://github.com/seveas/python-networkmanager",
      description = "Easy communication with NetworkManager - patched by gbwebdev",
      py_modules = ["NetworkManager"],
      install_requires = ["dbus-python", "six"],
)