# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
#import os
#import sys
#sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'CLS'
copyright = '2023, Gia Bamrud'
author = 'Gia Bamrud'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
]

# -- Myst options ------------------------------------------------------------
#import myst_parser
myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'smartquotes',
    'html_image',
]

myst_heading_anchors = 3

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'sphinx_rtd_theme'
html_theme = 'furo'
html_theme_options = {
    'light_css_variables': {
        "color-brand-primary": "#783bf3",
        "color-brand-content": "#783bf3",
    },
    'dark_css_variables': {
        "color-brand-primary": "#783bf3",
        "color-brand-content": "#783bf3",
    }
}

html_favicon = './img/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for EPUB output -------------------------------------------------
epub_title = 'CLS docs'
epub_description = 'Documentation for Card Layout Script'
epub_author = 'Gia Bamrud'
epub_copyright = 'copyright 2023, Gia Bamrud'
epub_uid = 'e24fcdfb-690b-4748-bc34-3d8e4b4d39b3'
epub_use_index = False
epub_tocscope = 'includehidden'
epub_guide = (('toc', 'nav.xhtml', 'Table of Contents'),)
