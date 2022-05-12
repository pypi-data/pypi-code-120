
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vfo", # Replace with your own username
    version="0.0.4",
    author="anurag upadhyay",
    author_email="iitg.anurag@gmail.com",
    description="A package for openseespy visualization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/u-anurag/vfo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)