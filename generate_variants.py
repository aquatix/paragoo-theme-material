import os
import stat
import sys
from utilkit import fileutil

PREFIX = 'material-'
BASE = 'material-base'

variants = {
        'green': {'theme_colour': '#1b5e20', 'base_colour': 'green lighten-5',
                'nav_colour': 'green darken-4',
                'header_align': '', 'header_text': 'green-text text-darken-4',
                'card_colour': 'green darken-4', 'card_text': 'white-text',
                'footer_colour': 'green darken-4', 'footer_text': 'green-text text-lighten-4', 'linkblock_text': 'white-text',
                'highlight_colour': 'green-text text-darken-4',
            },
        'grey': {'theme_colour': '#616161', 'base_colour': 'grey lighten-5',
                'nav_colour': 'grey darken-2',
                'header_align': 'center', 'header_text': 'orange-text',
                'card_colour': 'grey darken-2', 'card_text': 'white-text',
                'footer_colour': 'grey darken-2', 'footer_text': 'grey-text text-lighten-4', 'linkblock_text': 'white-text',
                'highlight_colour': 'orange',
            },
        }


templates = ['androidapp', 'base', 'gallery', 'galleryitem', 'news']
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
        fileutil.copytree(os.path.join(base_dir, asset), os.path.join(variant_dir, asset))

    for template in templates:
        with open(os.path.join(base_dir, template + '.html')) as f:
            content = [line.rstrip('\n') for line in f]

            for colour in variants[variant]:
                output = []
                for line in content:
                    output.append(line.replace(colour.upper(), variants[variant][colour]))
                content = output

            with open(os.path.join(variant_dir, template + '.html'), 'w') as fo:
                content = '\n'.join(content)
                fo.write(content)
