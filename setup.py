from setuptools import *

LONG_DESC = """
A bunch of utilities for making training models easier. Also contains useful
modules to make building models easier. Can be used in a jupyter notebook. Also
contains a module which integrates with the package `sacred`.
"""

setup(name='pytorch_lightning_utils',
	  version='0.0.1',
	  description='Pytorch lightning utilities',
	  long_description=LONG_DESC,
	  author='Sang Ki Kwon',
	  url='https://github.com/automatethem/pytorch_lightning_utils',
	  install_requires=['pytorch_lightning'],
	  author_email='automatethem@gmail.com',
	  license='MIT',
	  packages=find_packages(),
	  zip_safe=False)
