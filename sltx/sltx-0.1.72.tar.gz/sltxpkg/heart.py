import os  # list directory
import sys  # cmd line args

import sltxpkg.config as sc
from sltxpkg import globals as sg
from sltxpkg.cmd_line_args import parser, sub_parser
from sltxpkg.globals import DEFAULT_CONFIG, LOCAL_CONFIG
from sltxpkg.log_control import LOGGER, log_set_file_handler


def autoload_config(path: str, name: str):
    if os.path.isfile(path):
        LOGGER.info("Auto-load %s-config: '%s'", name, path)
        sc.load_configuration(path)


def retrieve_by_alias(tc: str):
    return [alias[0] for alias in sub_parser.cmds.items() if tc in alias[1][0][1]][0]


def _file_guard():
    if hasattr(sg.args, 'files') and not sg.args.files:
        if sg.args.verbose:
            LOGGER.info("Set default files to: " +
                        str(sg.configuration[sg.C_DEFAULT_FILES]))
        sg.args.files = sg.configuration[sg.C_DEFAULT_FILES]
        if not sg.args.files:
            LOGGER.error("No files supplied")
            exit(1)


def run(args=None):
    if args is None:
        args = sys.argv[1:]
    if len(args) < 1:
        parser.parse_args(['-h'])
    sg.args = parser.parse_args(args)

    if sg.args.log:
        log_set_file_handler()

    if not sg.args.command:
        parser.parse_args(['-h'])

    autoload_config(DEFAULT_CONFIG, 'default')
    autoload_config(LOCAL_CONFIG, 'local')

    _file_guard()

    if sg.args.threads < 0:
        if sg.args.verbose:
            LOGGER.info("Set default thread-count to: %d",
                        sg.configuration[sg.C_DEFAULT_THREADS])
        sg.args.threads = sg.configuration[sg.C_DEFAULT_THREADS]

    if sg.args.config is not None:
        sc.load_configuration(sg.args.config)

    cmd = None
    try:
        tc = sg.args.command.lower()
        cmd = sub_parser.cmds[tc if tc in sub_parser.cmds else retrieve_by_alias(
            tc)]
    except KeyError:
        LOGGER.error("The supplied command: %s is unknown. Choose one of: %s",
                     sg.args.command, list(sub_parser.cmds.keys()))
        exit(1)

    cmd[0][0]()
