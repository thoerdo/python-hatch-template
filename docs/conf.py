# pylint: skip-file

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


# -- Project information -----------------------------------------------------

project = "MY SPHINX TEST PROJECT"
copyright = "2024, Thomas Donner"
author = "Thomas Donner"

# The full version, including alpha/beta/rc tags
release = "<tbd: RELEASE>"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",  # For .md files
    "sphinx.ext.duration",  # durations report at the end of  Sphinx build
    "sphinx_rtd_theme",  # Better theme
    #  "sphinxcontrib.images",  # Allows showing tumbnail images
]

# MyST Configuration

# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-header-anchors
myst_heading_anchors = 6

# https://myst-parser.readthedocs.io/en/latest/configuration.html#global-configuration
myst_footnote_transition = False

myst_enable_extensions = ["fieldlist"]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_theme = 'furo'
html_theme = "sphinx_rtd_theme"

# -- 'sphinx_rtd_theme' Configuration
# Show link to source on GitHUb
html_context = {
    "display_github": True,
    "github_host": "cc-github.bmwgroup.net",
    "github_user": "ESDF",
    "github_repo": "<repo>",
    "github_version": "main",
    "conf_py_path": "/project-depot/",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# HTML Configuration
html_title = "MY HTML HEADER"
html_show_copyright = True

exclude_patterns = [".tox"]
