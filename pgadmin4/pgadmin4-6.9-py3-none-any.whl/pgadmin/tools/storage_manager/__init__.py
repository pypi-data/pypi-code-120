##########################################################################
#
# pgAdmin 4 - PostgreSQL Tools
#
# Copyright (C) 2013 - 2022, The pgAdmin Development Team
# This software is released under the PostgreSQL Licence
#
##########################################################################

"""A blueprint module implementing the storage manager functionality"""

from flask import url_for, Response, render_template
from flask_babel import gettext as _
from flask_security import login_required

from pgadmin.utils import PgAdminModule
from pgadmin.utils.ajax import bad_request
from pgadmin.utils.constants import MIMETYPE_APP_JS

MODULE_NAME = 'storage_manager'


class StorageManagerModule(PgAdminModule):
    """
    class StorageManagerModule(PgAdminModule)

        A module class for manipulating file operation which is derived from
        PgAdminModule.
    """

    LABEL = _('Storage Manager')

    def get_own_javascripts(self):
        """"
        Returns:
            list: js files used by this module
        """
        scripts = list()
        for name, script in [
            ['pgadmin.tools.storage_manager', 'js/storage_manager']
        ]:
            scripts.append({
                'name': name,
                'path': url_for('storage_manager.index') + script,
                'when': None
            })

        return scripts


blueprint = StorageManagerModule(MODULE_NAME, __name__)


@blueprint.route("/")
@login_required
def index():
    return bad_request(errormsg=_("This URL cannot be called directly."))


@blueprint.route("/js/storage_manager.js")
@login_required
def script():
    """render the import/export javascript file"""
    return Response(
        response=render_template("storage_manager/js/storage_manager.js", _=_),
        status=200,
        mimetype=MIMETYPE_APP_JS
    )
