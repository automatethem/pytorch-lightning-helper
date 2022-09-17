import os
from setuptools import *

def requirements():
    with open(os.path.join(os.path.dirname(__file__), 'requirements.txt'), encoding='utf-8') as f:
        return f.read().splitlines()

LONG_DESC = """
This is pytorch lightning helper
"""

setup(name='pytorch-lightning-helper',
	  version='0.0.5',
	  description='Pytorch lightning helper',
	  long_description=LONG_DESC,
	  author='Sang Ki Kwon',
	  url='https://github.com/automatethem/pytorch-lightning-helper',
	  install_requires=requirements(),
	  install_requires=[],
	  author_email='automatethem@gmail.com',
	  license='MIT',
	  packages=find_packages(),
	  zip_safe=False)
