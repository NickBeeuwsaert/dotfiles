#!/usr/bin/env python
# Spoon is life
import os
import os.path
import subprocess

ROOT_DIR=os.path.dirname(__file__)
DOTFILES_DIR=os.path.join(ROOT_DIR, "dotfiles")
HOME = os.path.expanduser('~')

def prompt(text, default):
    import sys
    sys.stdout.write(text)
    sys.stdout.flush()
    return sys.stdin.readline().rstrip('\n') or default

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
        #Otherwise see if the file alreadt exists
        elif os.path.lexists(dotfile):
            if os.path.realpath(ourfile) == os.path.realpath(dotfile):
                print("Skipping {}, already symlinked...".format(dotfile)) 
            else:
                print("Uh oh! {} already exists! What would you like to do?".format(dotfile))
                # This choice stuff is ugly, needs a rewrite when I get time
                # Also, for rigt now replacing the file isn't an option
                # Because I want it to be difficult for me to remove a important file
                choices = ["I", "D"]
                while True:
                    choice = prompt("[I]gnore, View [D]iff: ", "I").upper()
                    if choice not in choices:
                        print("Invalid selection")
                    else:
                        break
                if choice == "D":
                    print("Lauching vimdiff...")
                    # TODO: Go back up to choices after this
                    subprocess.call(['vimdiff', ourfile, dotfile])
                elif choice == "I":
                    print("Ignoring collision...")
        else:
            print("symlinking \"{}\" to \"{}\"".format(os.path.abspath(ourfile), dotfile))
            os.symlink(os.path.abspath(ourfile), dotfile)

print("Finished!")
