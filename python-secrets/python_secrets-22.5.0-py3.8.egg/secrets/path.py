# -*- coding: utf-8 -*-

"""
Return path to secrets file.
"""

import logging

from cliff.command import Command
from psec.secrets_environment import SecretsEnvironment


class SecretsPath(Command):
    """
    Return path to secrets file.

    If no arguments are present, the path to the secrets for the default
    environment is returned. If you want to get the secrets path for a specific
    environment, specify it as the argument to this command.
    """

    logger = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        try:
            default = self.app_args.environment
        except AttributeError:
            default = None
        parser = super().get_parser(prog_name)
        parser.add_argument(
            'environment',
            nargs='?',
            default=default
        )
        return parser

    def take_action(self, parsed_args):
        e = SecretsEnvironment(environment=parsed_args.environment)
        print(e.get_secrets_file_path())


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
