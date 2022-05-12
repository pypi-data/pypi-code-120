import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "schadem-cdk-construct-sfn-test",
    "version": "0.0.14",
    "description": "some description",
    "license": "Apache-2.0",
    "url": "https://github.com/45048633+schadem/schadem-cdk-construct-sfn-test.git",
    "long_description_content_type": "text/markdown",
    "author": "Martin Schade<45048633+schadem@users.noreply.github.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/45048633+schadem/schadem-cdk-construct-sfn-test.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "schadem_cdk_construct_sfn_test",
        "schadem_cdk_construct_sfn_test._jsii"
    ],
    "package_data": {
        "schadem_cdk_construct_sfn_test._jsii": [
            "schadem-cdk-construct-sfn-test@0.0.14.jsii.tgz"
        ],
        "schadem_cdk_construct_sfn_test": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.1.0, <3.0.0",
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
