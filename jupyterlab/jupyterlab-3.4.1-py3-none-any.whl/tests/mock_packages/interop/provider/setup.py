import json
import os.path as osp
from glob import glob

name = "jlab_mock_provider"
HERE = osp.abspath(osp.dirname(__file__))

with open(osp.join(HERE, "package.json")) as fid:
    data = json.load(fid)

from setuptools import setup

js_name = data["name"]

setup(
    name=name,
    version=data["version"],
    py_modules=[name],
    data_files=[
        (f"share/jupyter/labextensions/{js_name}", glob("static/package.json")),
        (f"share/jupyter/labextensions/{js_name}/static", glob("static/static/*")),
    ],
)
