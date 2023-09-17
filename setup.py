from setuptools import setup, find_packages

setup(
  name = 'mython',
  version = '0.1.0',
  description = "My first python package",
  license = "MIT",
  author = "ymat2",
  python_requires = '>=3.6',
  packages = find_packages(),
  scripts = ['mython/mython',]
)
