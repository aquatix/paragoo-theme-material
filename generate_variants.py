import os
import stat
import sys
from utilkit import fileutils

variants = {
        'grey': {'theme-colour': '#616161', 'base_colour': 'grey', 'highlight_colour': 'orange'}
        }


for variant in variants:
    # Loop over the colour variants and generate their respective themes
    if utilkit.dir_exists(variant):
        pass
