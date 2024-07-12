# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Flask Русская документация'
copyright = '2024, RoboInterativo'
author = 'RoboInterativo'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = ['sphinx_tabs.tabs']
# extensions.append("sphinx_wagtail_theme")
# html_theme = 'sphinx_wagtail_theme'

templates_path = ['_templates']
# html_theme = "classic"
# html_theme = 'bizstyle'
html_theme ='press'
# 'sphinx_rtd_theme'

# html_theme_options = {
#     "sidebarbgcolor": "black"
#
# }
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_static_path = ['_static']
