"""
Small sphinx extension to enable making image sliders.
"""

import os
import random

from sphinx.util.compat import Directive
from docutils import nodes

THIS_DIR = os.path.abspath(os.path.dirname(__file__))


class slider(nodes.raw):
    pass


blank = ('data:image/gif;base64,'
         'R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==')


def visit_slider_html(self, node):
    self.body.append('\n<div id="carousel" class="carousel" data-mixed>\n')
    arrows = ['  <a class="{0}" data-{0}><img src="{1}" '
              'width=56 height=56></a>\n'.format(t, blank)
              for t in ['prev', 'next']]
    self.body.append(arrows[0])
    self.body.append('  <ul>\n')
    # Get gallery dir
    gallery_dir = os.path.join(THIS_DIR, '..', node.dirname)
    # Collect filenames
    filenames = []
    for fname in os.listdir(gallery_dir):
        if not os.path.splitext(fname)[1].lower() == '.png':
            continue
        if not 'demo' in fname:
            continue  # only do pretty pictures!
        filenames.append(fname)
    # Add item for each name. We randomize here, because we can't do it
    # in JS (at least not withou modifying the code)
    random.shuffle(filenames)  # in-place
    for fname in filenames:
        filename = '_static/carousel/' + fname
        link = 'examples/' + fname.replace('__', '/')[:-4] + '.html'
        line = '<img data-src="%s" src="%s">' % (filename, blank)
        line = '<a href=%s>%s</a>' % (link, line)
        line = ('    <li><div class="wrap"><figure>%s</figure></div></li>'
                % line)
        self.body.append(line + '\n')
    self.body.append('  </ul>\n')
    self.body.append(arrows[1])


def depart_slider_html(self, node):
    self.body.append('</div>\n\n')


class SliderDirective(Directive):
        has_content = True

        def run(self):
            el = slider('')
            el.dirname = self.content[0].strip()
            el.images = [t.strip() for t in self.content]
            return [el]


def setup(Sphynx):
    Sphynx.add_javascript('js/jquery.anoslide.js')
    Sphynx.add_javascript('js/carousel.js')
    Sphynx.add_node(slider, html=(visit_slider_html, depart_slider_html))
    Sphynx.add_directive('slider', SliderDirective)
