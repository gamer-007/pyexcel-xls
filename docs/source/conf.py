# -*- coding: utf-8 -*-
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

intersphinx_mapping = {
    'pyexcel': ('http://pyexcel.readthedocs.org/en/latest/', None)
}

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'pyexcel-xls'
copyright = u'2015-2016 Onni Software Ltd.'
version = '0.2.0'
release = '0.2.0'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'pyexcel-xlsdoc'
latex_elements = {}
latex_documents = [
    ('index', 'pyexcel-xls.tex', u'pyexcel-xls Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'pyexcel-xls', u'pyexcel-xls Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'pyexcel-xls', u'pyexcel-xls Documentation',
     'Onni Software Ltd.', 'pyexcel-xls', 'One line description of project.',
     'Miscellaneous'),
]
