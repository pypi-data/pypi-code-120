
# This file was generated by 'versioneer.py' (0.18) from
# revision-control system data, or from the parent directory name of an
# unpacked source archive. Distribution tarballs contain a pre-generated copy
# of this file.

import json

version_json = '''
{
 "date": "2022-05-12T03:27:48+0000",
 "dirty": false,
 "error": null,
 "full-revisionid": "9253fe1dea155288b57d3e9d30b6b897a99cef3e",
 "version": "1.16.0.post.dev503"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
