""" Called from vispy_conf.py to generate the examples for the docs from the
example Python files.
"""

from __future__ import print_function, division

import os
import sys
import shutil

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen  # Py3k


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DOC_DIR = os.path.abspath(os.path.join(THIS_DIR, '..'))
EXAMPLES_DIR = os.path.abspath(os.path.join(DOC_DIR, '..', 'examples'))
OUTPUT_DIR = os.path.join(DOC_DIR, 'examples')

IMAGES_DIR = os.path.join(DOC_DIR, '_static', 'images')
THUMBS_DIR = os.path.join(DOC_DIR, '_static', 'thumbs')
CAROUSEL_DIR = os.path.join(DOC_DIR, '_static', 'carousel')

# Get images from github or local
#IMAGES_URL = 'http://raw.github.com/vispy/images/master/gallery/'
#THUMBS_URL = 'http://raw.github.com/vispy/images/master/thumbs/'
IMAGES_URL = os.path.join(DOC_DIR, '..', '_images', 'gallery/')
THUMBS_URL = os.path.join(DOC_DIR, '..', '_images', 'thumbs/')
CAROUSEL_URL = os.path.join(DOC_DIR, '..', '_images', 'carousel/')


def init():
    print('Generating examples.')
    main()


def setup(app):
    init()
    app.connect('build-finished', clean)


def clean(app, *args):
    # Clear images dir
    if os.path.isdir(IMAGES_DIR):
        shutil.rmtree(IMAGES_DIR)
    if os.path.isdir(THUMBS_DIR):
        shutil.rmtree(THUMBS_DIR)
    if os.path.isdir(CAROUSEL_DIR):
        shutil.rmtree(CAROUSEL_DIR)
    # Clear examples dir
    if os.path.isdir(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    # Clean examples file and gallery file
    fname = os.path.join(DOC_DIR, 'examples.rst')
    if os.path.isfile(fname):
        os.remove(fname)
    fname = os.path.join(DOC_DIR, 'gallery.rst')
    if os.path.isfile(fname):
        os.remove(fname)


def main():
    clean(None)
    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    if not os.path.isdir(IMAGES_DIR):
        os.mkdir(IMAGES_DIR)
    if not os.path.isdir(THUMBS_DIR):
        os.mkdir(THUMBS_DIR)
    if not os.path.isdir(CAROUSEL_DIR):
        os.mkdir(CAROUSEL_DIR)

    # Get examples and sort
    examples = list( get_example_filenames(EXAMPLES_DIR) )
    examples.sort(key=lambda x: x[1])
    
    create_examples(examples)
    create_examples_list(examples)
    create_gallery(examples)



def get_example_filenames(examples_dir):
    """ Yield (filename, name) elements for all examples. The examples
    are organized in directories, therefore the name can contain a 
    forward slash.
    """
    for (dirpath, dirnames, filenames) in os.walk(examples_dir):
        for fname in filenames:
            if not fname.endswith('.py'): continue
            filename = os.path.join(dirpath, fname)
            name = filename[len(examples_dir):].lstrip('/\\')[:-3]
            name = name.replace('\\', '/')
            yield filename, name



def create_examples(examples):
    
    # Create doc file for each example
    count = 0
    for filename, name in examples:
        
        # Create title
        lines = [':orphan:', '']
        lines.append(name)
        lines.append('-'*len(lines[-1]))
        lines.append('')
        
        # Get source
        in_gallery = False
        doclines = []
        sourcelines = []
        with open(os.path.join(EXAMPLES_DIR, name+'.py')) as f:
            for line in f.readlines():
                line = line.rstrip()
                if line.startswith('# vispy:') and 'gallery' in line:
                    in_gallery = True
                if not doclines:
                    if line.startswith('"""'):
                        doclines.append(line.lstrip('" '))
                        sourcelines = []
                    else:
                        sourcelines.append('    ' + line)
                elif not sourcelines:
                    if '"""' in line:
                        sourcelines.append('    ' + line.partition('"""')[0])
                    else:
                        doclines.append(line)
                else:
                    sourcelines.append('    ' + line)
        
        # Add desciprion 
        lines.extend(doclines)
        lines.append('')
        
        # Add image if we have it
        if in_gallery:
            image_name = download_image(IMAGES_URL, IMAGES_DIR, name)
            if image_name is not None:
                lines.append('.. image:: /_static/images/%s' % image_name)
                lines.append('')
                lines.append('----')
                lines.append('')
        
        # Add source code
        lines.append('.. code-block:: python')
        lines.append('    ')
        lines.extend(sourcelines)
        lines.append('')
        
        # Write
        output_filename = os.path.join(OUTPUT_DIR, name+'.rst')
        output_dir = os.path.dirname(output_filename)
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)
        with open(output_filename, 'w') as f:
            f.write('\n'.join(lines))
        count += 1
    print('Wrote %s examples' % count)    


def create_gallery(examples):
    
    # Create TOC
    lines = []
    lines.append('Gallery')
    lines.append('='*len(lines[-1]))
    lines.append('')
    
    # Give link to examples list
    lines.append('A full list of all examples is available in :doc:`examples`.')
    lines.append('')
    
    # Init
    line1, line2, line3, line4 = '| ', '| ', '| ', '| '
    COLWIDTH = 100-2
    NCOLS = 3
    done = False
    lines.append( ('+' + '-'*COLWIDTH) * NCOLS + '+' )
    
    # Parse all examples
    example_index = -1
    row = -1
    while not done:
        row += 1
        
        for col in range(NCOLS):
            
            # Get an image
            name = None
            while not name:
                example_index += 1
                if len(examples) <= example_index:
                    done = True
                    break
                filename, name = examples[example_index]
                in_gallery = False
                count = 0
                with open(os.path.join(EXAMPLES_DIR, name+'.py')) as f:
                    count += 1
                    for line in f.readlines():
                        if count > 10: break
                        if line.startswith('# vispy:') and 'gallery' in line:
                            in_gallery = True
                            break
                if in_gallery:
                    # Download thumb
                    download_image(CAROUSEL_URL, CAROUSEL_DIR, name)
                    image_name = download_image(THUMBS_URL, THUMBS_DIR, name)
                    if not image_name:
                        name = None
                else:
                    name = None
            
            # Create lineparts
            if name:
                linepart1 = ':doc:`examples/%s`' % name
                linepart2 = ''
                linepart3 = '.. image:: /_static/thumbs/%s' % image_name
                linepart4 = '   :alt: %s' % name
            else:
                linepart1 = linepart2 = linepart3 = linepart4 = ''
            
            # Add these cells
            line1 += linepart1.ljust(COLWIDTH-2) + ' | '
            line2 += linepart2.ljust(COLWIDTH-2) + ' | '
            line3 += linepart3.ljust(COLWIDTH-2) + ' | '
            line4 += linepart4.ljust(COLWIDTH-2) + ' | '
        
        
        # Close row
        lines.append(line1)
        lines.append(line2)
        lines.append(line3)
        lines.append(line4)
        lines.append( ('+' + '-'*COLWIDTH) * NCOLS + '+' )
        line1, line2, line3, line4 = '| ', '| ', '| ', '| '
    
    
    # Write file
    with open(os.path.join(DOC_DIR, 'gallery.rst'), 'w') as f:
        f.write('\n'.join(lines))



def create_examples_list(examples):
    
    # Create TOC
    lines = []
    lines.append('List of examples')
    lines.append('='*len(lines[-1]))
    lines.append('')
    
    # Add entry for each example that we know
    for _, name in examples:    
        lines.append('* :doc:`examples/%s`' % name)
    
    # Write file
    with open(os.path.join(DOC_DIR, 'examples.rst'), 'w') as f:
        f.write('\n'.join(lines))



def download_image(src, dst, name):
    
    image_name = name.replace('/', '__') + '.png'
    url = src + image_name
    image_filename = None  # Init
    
    
    if src.startswith('http'):
        # From the web
        try:
            remote = urlopen(url, timeout=5.0)
        except IOError:
            print('Image not available online: %s' % image_name)
        else:
            image_filename = os.path.join(dst, image_name)
            local = open(image_filename, 'wb')
            try:
                print('Downloading %s ... ' % image_name, end='')
                sys.stdout.flush()
                shutil.copyfileobj(remote, local)
                print('success')
            except Exception:
                print('failed')
                image_filename = None
            finally:
                local.close()
                remote.close()
    
    else:
        # Local file
        if not os.path.isfile(url):
            print('Image not available: %s' % image_name)
            print(url)
        else:
            image_filename = os.path.join(dst, image_name)
            shutil.copyfile(url, image_filename)
        
    return image_name if image_filename else None


if __name__ == '__main__':
    main()

