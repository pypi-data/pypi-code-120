"""
This script is used to install atlasify and all its dependencies. Run

    python setup.py install
or
    python3 setup.py install

to install the package.
"""

# Copyright (C) 2019-2022 Frank Sauerburger

from setuptools import setup

def load_long_description(filename):
    """
    Loads the given file and returns its content.
    """
    with open(filename, encoding="utf-8") as readme_file:
        content = readme_file.read()
        return content

setup(name='atlasify',
      version='0.7.2',  # Also change in module
      packages=["atlasify", "atlasify.tests"],
      package_data={'atlasify': ['fonts/*.ttf']},
      install_requires=["matplotlib", "packaging"],  # Also add in requirements.txt
      test_suite='atlasify.tests',
      description="Applies ATLAS style to matplotlib plots",  # Short description
      long_description=load_long_description("README.rst"),
      url="https://gitlab.cern.ch/fsauerbu/atlasify",
      author="Frank Sauerburger",
      author_email="f.sauerburger@cern.ch",
      classifiers=["Intended Audience :: Science/Research",
                   "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 3.7",
                   "Programming Language :: Python :: 3.8",
                   "Programming Language :: Python :: 3.9",
                   "Programming Language :: Python :: 3.10",
                   "Topic :: Scientific/Engineering :: Physics"],
      license="AGPL-3.0")
