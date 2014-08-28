"""
Small sphinx extension to enable making image sliders.
"""

import os
import random

from sphinx.util.compat import Directive
from docutils import nodes

THIS_DIR = os.path.abspath(os.path.dirname(__file__))

class slider(nodes.raw): pass

def visit_slider_html(self, node):
    #self.body.append(self.starttag(node, 'div', 'slider'))
    self.body.append('<div id="owl-demo" class="owl-carousel">\n')
    # Get gallery dir
    gallery_dir = os.path.join(THIS_DIR, '..', node.dirname)
#     if not os.path.isdir(gallery_dir):
#         return
    # Collect filenames
    filenames = []
    for fname in os.listdir(gallery_dir):
        if not os.path.splitext(fname)[1].lower() in ('.png', '.jpg'):
            continue
        if fname[-5] == '1': 
            continue  # this is how thumbnails are now named :(
        if not 'demo' in fname:
            continue  # only do pretty pictures!
        filenames.append(fname)
    # Add item for each name. We randomize here, because we can't do it
    # in JS (at least not withou modifying the code)
    random.shuffle(filenames)  # in-place
    for fname in filenames:
        filename = '_images/' + fname
        link = 'examples/' + fname.replace('__', '/')[:-4] + '.html'
        line = '<img class="lazyOwl" data-src="%s" alt="Lazy Owl Image">' % filename
        line = '<a href=%s>%s</a>' % (link, line)
        line = '    <div class="item">%s</div>' % line
        self.body.append(line + '\n')
    #for im in node.images:
    #    self.body.append('    <div class="item"><img class="owl-lazy" data-src="%s" alt="Lazy Owl Image"></div>' % im)
    
def depart_slider_html(self, node):
    self.body.append('</div>\n')


class SliderDirective(Directive):
        has_content = True
        def run(self):
            el = slider('')
            el.dirname = self.content[0].strip()
            el.images = [t.strip() for t in self.content]
            return [el]
    

def setup(Sphynx):
    
    Sphynx.add_javascript('owl-carousel/owl.carousel.min.js')
    Sphynx.add_stylesheet('owl-carousel/owl.carousel.css')
    Sphynx.add_stylesheet('owl-carousel/owl.theme.css')
    #Sphynx.add_stylesheet('owl-carousel/owl.transitions.css')
    
    Sphynx.add_node(slider, html=(visit_slider_html, depart_slider_html))
    Sphynx.add_directive('slider', SliderDirective)
