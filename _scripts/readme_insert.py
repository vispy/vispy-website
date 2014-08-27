"""
Small sphinx extension to insert content from a readme.rst
"""

import os
import random

from sphinx.util.compat import Directive
from docutils import nodes
from docutils.core import publish_string, publish_parts

THIS_DIR = os.path.abspath(os.path.dirname(__file__))

class readme_insert(nodes.raw): pass

def visit_readme_insert_html(self, node):
    #self.body.append('<h1> %r</h1>' % node.filename)
    filename = os.path.join(THIS_DIR, '..', node.filename)
    rst = open(filename, 'rb').read().decode('utf-8')
    rst = rst.split('\n----\n')[1]
    html = publish_parts(rst, writer_name='html')['body']
    self.body.append(html)

def depart_readme_insert_html(self, node):
    pass

class ReadmeInsertDirective(Directive):
        has_content = True
        def run(self):
            el = readme_insert('')
            el.filename = self.content[0].strip()
            return [el]

def setup(Sphynx):
    
    Sphynx.add_node(readme_insert, html=(visit_readme_insert_html,
                                         depart_readme_insert_html))
    Sphynx.add_directive('readme_insert', ReadmeInsertDirective)
