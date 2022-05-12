import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-watchful",
    "version": "0.6.116",
    "description": "Watching your CDK apps since 2019",
    "license": "Apache-2.0",
    "url": "https://github.com/eladb/cdk-watchful.git",
    "long_description_content_type": "text/markdown",
    "author": "Elad Ben-Israel<elad.benisrael@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/eladb/cdk-watchful.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_watchful",
        "cdk_watchful._jsii"
    ],
    "package_data": {
        "cdk_watchful._jsii": [
            "cdk-watchful@0.6.116.jsii.tgz"
        ],
        "cdk_watchful": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.0.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.58.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
