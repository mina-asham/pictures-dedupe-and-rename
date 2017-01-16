***************************
Pictures: Dedupe and Rename
***************************

.. image:: https://travis-ci.org/mina-asham/pictures-dedupe-and-rename.svg?branch=master
    :target: https://travis-ci.org/mina-asham/pictures-dedupe-and-rename

Ever had a shared folder of pictures with friends from one of your travels, and had a ton of weird filenames which made browsing pictures in order impossible?

This is a solution to that! Simply install this package and run a simple command to fix a selected folder by dedupe all pictures and renaming them using the yyyymmdd_HHMMss format.

.. contents:: Table of Contents

Compatibility
*************
Python 2.7+

Installation
************

PyPI (Recommended)
==================
Install using `pip <https://pip.pypa.io/en/stable/installing/>`_::

    pip install PicturesDedupeRename

From Zip
========
Download the latest source from `GitHub repository <https://github.com/mina-asham/pictures-dedupe-and-rename/archive/master.zip>`_.

Extract and run::

    python setup.py install

Usage
*****

Command line
============

Some examples::

    dedupe-rename.py -d /home/pictures/collection
    dedupe-rename.py -d /home/pictures/collection -o dedupe

Show command line options::

    dedupe-rename.py -h

    usage: dedupe-rename.py [-h] -d DIRECTORY [-o OPERATIONS] [-p PATTERNS]

    Dedupe a set of pictures in a given folder and rename them using the yyyymmdd_HHMMss format

    optional arguments:
      -h, --help                              show this help message and exit
      -d DIRECTORY, --directory DIRECTORY     input directory for all pictures
      -o OPERATIONS, --operations OPERATIONS  the operatiosn to perform (dedupe, rename, or both) (default: both)
      -p PATTERNS, --patterns PATTERNS        the glob patterns for pictures (default: *.jpeg,*.jpg,*.png)

Python Script
=============

Sample::

    from pictures import dedupe, rename
    files = load_files_to_dedupe()
    dedupe(files)
    files = load_files_to_rename()
    rename(files)

