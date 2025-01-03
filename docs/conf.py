# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import sys
import os
sys.path.append(os.path.abspath('..'))

project = 'moduls' 
copyright = '2024, dima' 
author = 'dima'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates'] #путь к шаблонам документации
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']#эти не будут включены

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'nature'#тема оформления
html_static_path = ['_static']#путь к статическим файлам.Напрмер измображением
#которые будет использоватся в документации

