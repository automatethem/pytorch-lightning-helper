from setuptools import *

LONG_DESC = """
This is pytorch lightning utilities
"""

setup(name='pytorch-lightning-utils',
	  version='0.0.1',
	  description='Pytorch lightning utilities',
	  long_description=LONG_DESC,
	  author='Sang Ki Kwon',
	  url='https://github.com/automatethem/pytorch-lightning-utils',
	  install_requires=['pytorch-lightning', 'torchsummaryX'],
	  author_email='automatethem@gmail.com',
	  license='MIT',
	  packages=find_packages(),
	  zip_safe=False)
