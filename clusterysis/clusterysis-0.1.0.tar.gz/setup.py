from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='clusterysis',
    packages=find_packages(include=['clusterysis']),
    version='0.1.0',
    description='A library for visualizing clusters.',
    #long_description=long_description,
    long_description_content_type='text/markdown',
    long_description="Clusterysis",
    author='Gabriel Di Pardi Arruda',
)
