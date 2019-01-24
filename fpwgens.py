#!/usr/bin/env python3
# Reads a given file and replaces #RND# with securely generated passwords.

import sys
from prpg import rpg
from prpg.fileRandomizer import FileRandomizer


def show_help():
    print("""File Randomizer
        
    SUMMARY:
        This script reads a given file, and replaces #RND# with randomly 
        generated passwords for use with phone authentication.
        
    SYNTAX:
        frpg.py /path/to/foo [character set options | magic class] [length | pattern]
        
    For all options except for the path, see: prpg.py's help. (Run prpg without any arguments)

    """)


options = sys.argv

if len(options) ==1:
    show_help()
    exit(1)

file = options.pop(1)
r = rpg.Rpg(options)

Randomizer = FileRandomizer(file, r)
Randomizer.set_passwords()


