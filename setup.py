from setuptools import setup, find_packages

setup(
    name = "FreeCite",
    version = "0.1",
    py_modules = ['freecite'],
    #install requirements
    install_requires = [            
            'requests==1.1.0'
    ],

    #author details
    author = "James Ravenscroft",
    author_email = "ravenscroftj@gmail.com",
    description = "A wrapper around the FreeCite REST API",
    url = "http://wwww.github.com/ravenscroftj/freecite"
)
