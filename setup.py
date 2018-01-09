# coding: utf-8

from setuptools import setup, find_packages


NAME = "whistle"
VERSION = "0.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = open("requirements.txt").readlines()

setup(
    name=NAME,
    version=VERSION,
    description="",
    author_email="",
    url="",
    py_modules=["whistle"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
)
