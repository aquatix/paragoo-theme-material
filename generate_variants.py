import os
import stat
import sys
import datetime
from utilkit import fileutil, datetimeutil

PREFIX = 'material-'
BASE = 'material-base'
TIMESTAMP = datetime.datetime.now()
CACHEBUSTER = str(int(datetimeutil.python_to_unix(TIMESTAMP)))

files_to_rename = {'style.css': 'style_' + CACHEBUSTER + '.css'}

variants = {
        'green': {'theme_colour': '#1b5e20', 'base_colour': 'green lighten-5', 'base_text': 'black',
                'nav_colour': 'green darken-4',
                'header_align': '', 'header_text': 'green-text text-darken-4',
                'card_colour': 'green darken-4', 'card_text': 'white-text',
                'footer_colour': 'green darken-4', 'footer_text': 'green-text text-lighten-4', 'linklist_text': 'white-text',
                'highlight_colour': 'green-text text-darken-4',
                'link_text': '#ff9800', 'block_colour': '#c8e6c9', 'block_text': '#000',
            },
        'grey': {'theme_colour': '#616161', 'base_colour': 'grey lighten-5', 'base_text': 'black',
                'nav_colour': 'grey darken-2',
                'header_align': 'center', 'header_text': 'orange-text',
                'card_colour': 'grey darken-2', 'card_text': 'white-text',
                'footer_colour': 'grey darken-2', 'footer_text': 'grey-text text-lighten-4', 'linklist_text': 'white-text',
                'highlight_colour': 'orange',
                'link_text': '#2196f3', 'block_colour': '#ddd', 'block_text': '#000',
            },
        'graphite': {'theme_colour': '#424242', 'base_colour': 'grey darken-2', 'base_text': 'grey-text text-lighten-2',
                'nav_colour': 'grey darken-4',
                'header_align': '', 'header_text': 'orange-text',
                'card_colour': 'teal darken-4', 'card_text': 'white-text',
                'footer_colour': 'grey darken-4', 'footer_text': 'grey-text text-lighten-4', 'linklist_text': 'white-text',
                'highlight_colour': 'teal-text text-lighten-3',
                'link_text': '#ffab40', 'block_colour': '#212121', 'block_text': '#e0e0e0',
            },
        }


templates = ['androidapp.html', 'base.html', 'gallery.html', 'galleryitem.html', 'news.html', 'css/style.css']
assets = ['css', 'js']

current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(current_dir, BASE)
build_dir = os.path.join(current_dir, 'build')

fileutil.ensure_dir_exists(build_dir)

for variant in variants:
    # Loop over the colour variants and generate their respective themes
    variant_dir = os.path.join(build_dir, PREFIX + variant)
    print(variant_dir)
    fileutil.archive_if_exists(variant_dir)
    fileutil.ensure_dir_exists(variant_dir, fullpath=True)

    for asset in assets:
        fileutil.copytree(os.path.join(base_dir, asset), os.path.join(variant_dir, asset), rename=files_to_rename)

    for template in templates:
        with open(os.path.join(base_dir, template)) as f:
            content = [line.rstrip('\n') for line in f]

            variants[variant]['cachebuster'] = CACHEBUSTER

            for colour in variants[variant]:
                output = []
                for line in content:
                    output.append(line.replace(colour.upper(), variants[variant][colour]))
                content = output

            for asset in assets:
                if template.endswith('.' + asset):
                    template = fileutil.filename_addstring(template, '_' + CACHEBUSTER)
            with open(os.path.join(variant_dir, template), 'w') as fo:
                content = '\n'.join(content)
                fo.write(content)
