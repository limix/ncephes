#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath(".."))


def get_version():
    import version

    return version.get()


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]
napoleon_google_docstring = True
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
project = u"Ncephes"
copyright = u"2016, Danilo Horta"
author = u"Danilo Horta"
version = get_version()
release = version
language = None
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "build_ext.py", "libpath.py"]
pygments_style = "sphinx"
todo_include_todos = False
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
htmlhelp_basename = "ncephes-doc"
intersphinx_mapping = {"https://docs.python.org/": None}
