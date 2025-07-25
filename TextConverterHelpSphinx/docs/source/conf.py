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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from __future__ import annotations

import importlib.util
import os
import sys
import time
import datetime

from sphinx.application import Sphinx


# -- Project information -----------------------------------------------------

project = 'Text Editor & Converter'
copyright = '2025, Don Spickler'
author = 'Don Spickler'

# The full version, including alpha/beta/rc tags
release = '1.3.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",  # has to be loaded before sphinx_autodoc_typehints
    "sphinx_autodoc_typehints",
    "sphinx.ext.intersphinx",
    #"sphinx_qt_documentation",
    "sphinx_design",
    "sphinx_favicon",
    #"sphinxext.rediraffe",
    #"sphinxcontrib.images",
    #'sphinx.ext.inheritance_diagram',
    # 'sphinxcontrib.spelling'  # commenting out to allow for easy usage locally
    "sphinx.ext.imgmath"
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

templates_path = ['_templates']
html_static_path = ['_static']
html_css_files = ["custom.css"]
html_last_updated_fmt = '%A, %B %d, %Y  -  %I:%M %p'
exclude_patterns = []
master_doc = 'index'

html_show_sourcelink = False
html_show_sphinx = True

# -- Options for HTML output -------------------------------------------------

html_logo = os.path.join("", "ProgramIcon.png")
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "collapse_navigation": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/mathprofdes/Text-Converter",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        }
    ],
#    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navbar_end": ["navbar-icon-links"],
    "footer_start": ["copyright", "last-updated"],
    "footer_end": ["sphinx-version", "theme-version"],
    "navigation_depth": 2,
    "navigation_with_keys": False,
    "secondary_sidebar_items": ["page-toc"],
    "show_toc_level": 3,
    "show_nav_level": 2,
    "use_edit_page_button": False,

    "navbar_align": "left",
    "primary_sidebar_end": [],
    "back_to_top_button": False,
}

html_sidebars = {
  "**": []
}
imgmath_use_preview=True


