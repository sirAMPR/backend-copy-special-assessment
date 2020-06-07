#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "aradcliff"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    result = []
    r = re.compile(r".*__\w+__.*")
    for directory in dirname:
        path = os.path.abspath(directory)
        for item in list(filter(r.match, os.listdir(directory))):
            result += [path + '/' + item]
    return result


def copy_to(path_list, dest_dir):
    # your code here
    return


def zip_to(path_list, dest_zip):
    # your code here
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='directories to copy', nargs='+')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    from_dir = ns.from_dir
    todir = ns.todir
    tozip = ns.tozip

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).
    file_list = get_special_paths(from_dir)
    if tozip:
        print("zip -j " + tozip + " " + "".join(file_list))
        subprocess.run(["zip", "-j", tozip] + file_list)
    else:
        for item in file_list:
            if todir:
                os.makedirs(todir, exist_ok=True)
                shutil.copy(item, todir)
            else:
                print(item)


if __name__ == "__main__":
    main(sys.argv[1:])
