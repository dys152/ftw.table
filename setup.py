from setuptools import setup, find_packages
import os

version = '1.22.1.dev0'
maintainer = 'Jonas Baumann'

tests_require = [
    'ftw.builder',
    'ftw.testing',
    'plone.app.contenttypes',
    'plone.app.testing',
    'plone.mocktestcase',
    ]

setup(name='ftw.table',
      version=version,
      description='Table generator utility for use within zope.',
      long_description=open(
          "README.rst").read() + "\n" + open(
          os.path.join("docs", "HISTORY.txt")).read(),

      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers

      classifiers=[
          'Framework :: Plone',
          'Framework :: Plone :: 4.3',
          'Framework :: Plone :: 5.1',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],

      keywords='ftw table generator',
      author='4teamwork AG',
      author_email='mailto:info@4teamwork.ch',
      maintainer=maintainer,
      url='https://github.com/4teamwork/ftw.table',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
          'Plone',
          'five.globalrequest',
          'ftw.upgrade',
          'setuptools',
          # -*- Extra requirements: -*-
          ],

      tests_require=tests_require,
      extras_require={
          'extjs': ['collective.js.extjs'],
          'tests': tests_require},

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
