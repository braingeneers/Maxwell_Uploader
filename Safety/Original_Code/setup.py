from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ephys-upload-gui',
    version='0.0.1',
    description='Braingeneers Upload GUI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/braingeneers/ephys-upload-gui',
    author='Braingeneers',
    classifiers=[
        'Intended Audience :: Braingeneers',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(exclude=()),

    include_package_data=True)