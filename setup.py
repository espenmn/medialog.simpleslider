# -*- coding: utf-8 -*-
"""
This module contains the tool of medialog.simpleslider
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.1'

long_description = (
    read('README.txt')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    'Download\n'
    '********\n')

setup(name='medialog..simpleslider',
      version=version,
      description="Adds a viewlet to display a slider",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        ],
      keywords='',
      author='',
      author_email='',
      url='http://github.com/espenmn/.simpleslider',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['medialog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        ],
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
