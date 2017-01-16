# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='PicturesDedupeRename',
    version='1.0.4',
    description='Dedupe a set of pictures in a given folder and rename them using the yyyymmdd_HHMMss format',
    url='https://github.com/mina-asham/pictures-dedupe-and-rename',
    license='MIT',
    author='Mina Asham',
    author_email='mina.asham@hotmail.com',
    scripts=['dedupe-rename.py'],
    packages=find_packages(),
    install_requires=['exifread'],
    long_description=open('README.rst').read()
)
