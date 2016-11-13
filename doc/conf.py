#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__import__('sphinx_rtd_theme')

try:
    import ncephes
    version = ncephes.__version__
except ImportError:
    version = 'unknown'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinxcontrib.programoutput'
]
napoleon_google_docstring = True
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'nCephes'
copyright = u'2016, Danilo Horta'
author = u'Danilo Horta'
release = version
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes", ]
htmlhelp_basename = 'ncephes-doc'
latex_elements = {}
latex_documents = [
    (master_doc, 'nCephes.tex', u'nCephes Documentation',
     u'Danilo Horta', 'manual'),
]
man_pages = [
    (master_doc, 'ncephes', u'nCephes Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'nCephes', u'nCephes Documentation',
     author, 'nCephes', 'One line description of project.',
     'Miscellaneous'),
]
intersphinx_mapping = {'https://docs.python.org/': None}
