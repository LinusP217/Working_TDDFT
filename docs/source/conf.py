# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tiempoDFT'
copyright = '2024, Zuehlsdorff Group'
author = 'Zuehlsdorff Group'
html_scaled_image_link = False

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [ 'sphinx.ext.autodoc',
                'sphinx.ext.doctest',
                'sphinx.ext.autosummary',
                'sphinx.ext.intersphinx',
                'sphinx_design',
                'sphinxcontrib.images',
               ]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
#html_logo = 'figures/den_compare_blue.png'
