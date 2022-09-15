from setuptools import *

LONG_DESC = """
This is pytorch lightning utilities
"""

setup(name='pytorch_lightning_utils',
	  version='0.0.1',
	  description='Pytorch lightning utilities',
	  long_description=LONG_DESC,
	  author='Sang Ki Kwon',
	  url='https://github.com/automatethem/pytorch_lightning_utils',
	  install_requires=['pytorch_lightning', 'torchsummaryX'],
	  author_email='automatethem@gmail.com',
	  license='MIT',
	  packages=find_packages(),
	  zip_safe=False)
