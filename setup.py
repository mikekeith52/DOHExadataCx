
from setuptools import setup, find_packages

setup(
  name = 'DOHExadataCx',
  version = '0.1.2',
  license='MIT',        # https://help.github.com/articles/licensing-a-repository
  short_description = '',
  long_description='',
  author = 'Michael Keith',
  author_email = 'michaelkeith@utah.gov',
  packages=find_packages('src'),
  package_dir={'': 'src'},
  url = 'https://github.com/mikekeith52/DOHExadataCx',
  install_requires = ['cx-Oracle'],
)
