# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='pictures-dedupe-and-rename',
    version='1.0.0',
    description='Dedupe a set of pictures in a given folder and rename them using the yyyymmdd_HHMMss format',
    url='https://github.com/mina-asham/pictures-dedupe-and-rename',
    license='MIT',
    author='Mina Asham',
    author_email='mina.asham@hotmail.com',
    packages=find_packages(),
    install_requires=['exifread'],
    long_description=open('README.md').read()
)
