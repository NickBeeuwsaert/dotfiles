#!/usr/bin/env python
import os
import os.path
import subprocess
import argparse
import shutil
import sys

ROOT_DIR=os.path.dirname(__file__)
DOTFILES_DIR=os.path.join(ROOT_DIR, "dotfiles")
HOME = os.path.expanduser('~')

# Like input() but works in python 2 and 3
def readline(prompt=''):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    return sys.stdin.readline().rstrip("\
")

def get_dotfiles(dot_dir=DOTFILES_DIR):
    for dirname, dirs, files in os.walk(dot_dir):
        for fname in files:
            yield os.path.relpath(os.path.join(dirname, fname), dot_dir)

def copyfile(source, dest):
    dest_dir = os.path.dirname(dest)

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    shutil.copy(source, dest)

def view_diff(source, dest):
    subprocess.call([
        "vimdiff",
        source,
        dest
    ])

def link(args):
    for dotfile in get_dotfiles():
        dest_file = os.path.join(args.home_dir, dotfile)
        source_file = os.path.join(args.dot_dir, dotfile)

        if args.force:
            copyfile(source_file, dest_file)
            continue

        if not os.path.exists(dest_file):
            copyfile(source_file, dest_file)
            continue


        if os.path.getmtime(dest_file) > os.path.getmtime(source_file):
            print("WARNING! {} is newer than {}! What do you want to do?".format(dest_file, source_file))
            while True:

                choice = readline("View (D)iff, (C)opy over, (I)gnore: ")

                if choice == "D":
                    view_diff(dest_file, source_file)
                elif choice == "C":
                    copyfile(source_file, dest_file)
                    break
                elif choice == "I":
                    break

def update(args):
    dotfiles = get_dotfiles()

    for dotfile in dotfiles:
        destination_file = os.path.join(args.dot_dir, dotfile)
        source_file = os.path.join(args.home_dir, dotfile)
        
        if not os.path.exists(source_file):
            print("{} doesn't exist! Skipping...".format(source_file))
            continue

        # if the dotfile in ~ is newer than ours, copy the file over our copy
        if os.path.getmtime(source_file) > os.path.getmtime(destination_file):
            print("{} is newer than {}!".format(source_file, destination_file))
            copyfile(source_file, destination_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Link dotfiles")
    parser.add_argument('--dot-dir', '-d', default=DOTFILES_DIR, help="Where to look for dot files")
    parser.add_argument('--home-dir', '-H', default=HOME, help="Where to put the dot files")
    subparsers = parser.add_subparsers()

    link_parser = subparsers.add_parser('link')
    link_parser.add_argument('--force', '-F', action="store_true", help="Don't bother with conflicts")
    link_parser.set_defaults(func=link)

    update_parser = subparsers.add_parser('update')
    update_parser.set_defaults(func=update)

    args = parser.parse_args()

    args.func(args)
