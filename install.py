#!/usr/bin/env python
# Spoon is life
import os
import os.path
import subprocess

ROOT_DIR=os.path.dirname(__file__)
DOTFILES_DIR=os.path.join(ROOT_DIR, "dotfiles")
HOME = os.path.expanduser('~')

def prompt(text, default = None):
    import sys
    sys.stdout.write(text)
    sys.stdout.flush()
    return sys.stdin.readline().rstrip('\n') or default

def launch_diff(filea, fileb):
    subprocess.call(['vimdiff', ourfile, dotfile])

def choice(p, choices):
    while True:
        choice = prompt(p);
        if choice not in choices:
            print("Try again.")
            continue
        if choices[choice](): break

for dirpath, dirnames, filenames in os.walk(DOTFILES_DIR):
    for filename in filenames:
        ourfile = os.path.join(dirpath, filename)
        # this could probably be cleaned up...
        dotfile = os.path.join(HOME, os.path.relpath(ourfile, DOTFILES_DIR))
        dotfile_path = os.path.dirname(dotfile)

        #Check to see if we need to create the directory for the file
        if not os.path.exists(dotfile_path):
            print("Creating \"{}\"...".format(dotfile_path))
            os.makedirs(dotfile_path)
        #Otherwise see if the file already exists
        elif os.path.lexists(dotfile):
            if os.path.realpath(ourfile) == os.path.realpath(dotfile):
                print("Skipping {}, already symlinked...".format(dotfile)) 
            else:
                print("Uh oh! {} already exists! What would you like to do?".format(dotfile))
                # for right now, simply replacing the file isn't an option
                # Because I want it to be difficult for me to remove a important file
                # And I could probably merge over the relevant lines in vimdiff anyway
                choice("[I]gnore it, View the [D]iff: ", {
                    'I': lambda: True,
                    'D': lambda: launch_diff(ourfile, dotfile)
                })
        # File doesn't exist, symlink it!
        else:
            print("symlinking \"{}\" to \"{}\"".format(os.path.abspath(ourfile), dotfile))
            os.symlink(os.path.abspath(ourfile), dotfile)

print("Finished!")
