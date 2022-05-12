"""Module containing the logic for utilities."""

import re

import subprocess
from copy import deepcopy

from pathlib import Path
from pathlib import PurePath
from pathlib import WindowsPath
from datetime import datetime

from textwrap import wrap

from argparse import ArgumentParser

import yaml

import typing

from io import StringIO

from textfsm import TextFSM

from dgspoc.exceptions import UtilsParsedTemplateError

from dgspoc.constant import ECODE


class Text(str):
    def __new__(cls, *args, **kwargs):
        if not args and not kwargs:
            return str.__new__(cls, '')
        encoding = kwargs.get('encoding', 'utf-8')
        errors = kwargs.get('errors', 'strict')
        obj = kwargs.get('object', '')
        if args:
            if len(args) == 1:
                obj = args[0]
                if isinstance(obj, bytes):
                    return str.__new__(cls, obj, encoding=encoding, errors=errors)
                elif isinstance(obj, BaseException):
                    return str.__new__(cls, '{}: {}'.format(type(obj).__name__, obj))
                else:
                    return str.__new__(cls, obj)
            else:
                return str.__new__(cls, *args, **kwargs)
        else:
            if isinstance(obj, bytes):
                return str.__new__(cls, obj, encoding=encoding, errors=errors)
            elif isinstance(obj, BaseException):
                return str.__new__(cls, '{}: {}'.format(type(obj).__name__, obj))
            else:
                return str.__new__(cls, obj)


class Printer:
    """A printer class.

    Methods
    Printer.get(data, header='', footer='', failure_msg='', width=80, width_limit=20) -> str
    Printer.print(data, header='', footer='', failure_msg='', width=80, width_limit=20, print_func=None) -> None
    """
    @classmethod
    def get(cls, data, header='', footer='',
            width=80, width_limit=20, failure_msg=''):
        """Decorate data by organizing header, data, footer, and failure_msg

        Parameters
        ----------
        data (str, list): a text or a list of text.
        header (str): a header text.  Default is empty.
        footer (str): a footer text.  Default is empty.
        width (int): width of displayed text.  Default is 80.
        width_limit (int): minimum width of displayed text.  Default is 20.
        failure_msg (str): a failure message.  Default is empty.
        """
        headers = str(header).splitlines()
        footers = str(footer).splitlines()
        data = data if Misc.is_mutable_sequence(data) else [data]
        lst = []
        result = []

        right_bound = width - 4

        for item in data:
            if width >= width_limit:
                for line in str(item).splitlines():
                    lst.extend(wrap(line, width=right_bound))
            else:
                lst.extend(line.rstrip() for line in str(item).splitlines())
        length = max(len(str(i)) for i in lst + headers + footers)

        if width >= width_limit:
            length = right_bound if right_bound > length else length

        result.append('+-{}-+'.format('-' * length))
        if header:
            for item in headers:
                result.append('| {} |'.format(item.ljust(length)))
            result.append('+-{}-+'.format('-' * length))

        for item in lst:
            result.append('| {} |'.format(item.ljust(length)))
        result.append('+-{}-+'.format('-' * length))

        if footer:
            for item in footers:
                result.append('| {} |'.format(item.ljust(length)))
            result.append('+-{}-+'.format('-' * length))

        if failure_msg:
            result.append(failure_msg)

        txt = '\n'.join(result)
        return txt

    @classmethod
    def print(cls, data, header='', footer='',
              width=80, width_limit=20, failure_msg='', print_func=None):
        """Decorate data by organizing header, data, footer, and failure_msg

        Parameters
        ----------
        data (str, list): a text or a list of text.
        header (str): a header text.  Default is empty.
        footer (str): a footer text.  Default is empty.
        width (int): width of displayed text.  Default is 80.
        width_limit (int): minimum width of displayed text.  Default is 20.
        failure_msg (str): a failure message.  Default is empty.
        print_func (function): a print function.  Default is None.
        """

        txt = Printer.get(data, header=header, footer=footer,
                          failure_msg=failure_msg, width=width,
                          width_limit=width_limit)

        print_func = print_func if callable(print_func) else print
        print_func(txt)

    @classmethod
    def get_message(cls, fmt, *args, style='format', prefix=''):
        """Get a message

        Parameters
        ----------
        fmt (str): string format.
        args (tuple): list of parameters for string interpolation.
        style (str): either format or %.
        prefix (str): a prefix.

        Returns
        -------
        str: a message.
        """

        if args:
            message = fmt.format(*args) if style == 'format' else fmt % args
        else:
            message = fmt

        message = '{} {}'.format(prefix, message) if prefix else message
        return message

    @classmethod
    def print_message(cls, fmt, *args, style='format', prefix='', print_func=None):
        """Print a message

        Parameters
        ----------
        fmt (str): string format.
        args (tuple): list of parameters for string interpolation.
        style (str): either format or %.
        prefix (str): a prefix.
        print_func (function): a print function.
        """
        message = cls.get_message(fmt, *args, style=style, prefix=prefix)
        print_func = print_func if callable(print_func) else print
        print_func(message)


class File:
    message = ''

    @classmethod
    def is_exist(cls, filename):
        """Check file existence

        Parameters
        ----------
        filename (str): a file name

        Returns
        -------
        bool: True if existed, otherwise False
        """
        try:
            file_obj = Path(filename)
            return file_obj.exists()
        except Exception as ex:
            cls.message = Text(ex)
            return False

    @classmethod
    def create(cls, filename, showed=True):
        """Check file existence

        Parameters
        ----------
        filename (str): a file name
        showed (bool): showing the message of creating file

        Returns
        -------
        bool: True if created, otherwise False
        """
        filename = cls.get_path(str(filename).strip())
        if cls.is_exist(filename):
            cls.message = 'File is already existed.'
            return True

        try:
            file_obj = Path(filename)
            if not file_obj.parent.exists():
                file_obj.parent.mkdir(parents=True, exist_ok=True)
            file_obj.touch()
            fmt = '{:%Y-%m-%d %H:%M:%S.%f} - {} file is created.'
            showed and print(fmt.format(datetime.now(), filename))
            cls.message = '{} file is created.'.format(filename)
            return True
        except Exception as ex:
            cls.message = Text(ex)
            return False

    @classmethod
    def get_path(cls, *args, is_home=False):
        """Create a file path

        Parameters
        ----------
        args (tuple): a list of file items
        is_home (bool): True will include Home directory.  Default is False.

        Returns
        -------
        str: a file path.
        """
        lst = [Path.home()] if is_home else []
        lst.extend(list(args))
        file_path = str(Path(PurePath(*lst)).expanduser().absolute())
        return file_path

    @classmethod
    def get_dir(cls, file_path):
        """get directory from existing file path

        Parameters
        ----------
        file_path (string): file path

        Returns
        -------
        str: directory
        """
        file_obj = Path(file_path).expanduser().absolute()
        if file_obj.is_dir():
            return str(file_obj)
        elif file_obj.is_file():
            return str(file_obj.parent)
        else:
            fmt = 'FileNotFoundError: No such file or directory "{}"'
            cls.message = fmt.format(file_path)
            return ''

    @classmethod
    def get_content(cls, file_path):
        """get content of file

        Parameters
        ----------
        file_path (string): file path

        Returns
        -------
        str: content of file
        """
        filename = cls.get_path(file_path)
        try:
            with open(filename) as stream:
                content = stream.read()
                return content
        except Exception as ex:
            cls.message = Text(ex)
            return ''

    @classmethod
    def get_result_from_yaml_file(cls, file_path, base_dir='',
                                  is_stripped=True,
                                  dot_datatype=False,
                                  default=dict(),  # noqa
                                  var_substitution=False,
                                  root_var_name='self'
                                  ):
        """get result of YAML file

        Parameters
        ----------
        file_path (string): file path
        base_dir (str): a based directory
        is_stripped (bool): removing leading or trailing space.  Default is True.
        dot_datatype (bool): convert a return_result to DotObject if
                return_result is dictionary.  Default is False.
        default (object): a default result file is not found.  Default is empty dict.
        var_substitution (bool): internal variable substitution.  Default is False.
        root_var_name (str): root variable of data structure for
                variable substitution.  Default is self.

        Returns
        -------
        object: YAML result
        """

        yaml_result = default

        try:
            if base_dir:
                filename = cls.get_path(cls.get_dir(base_dir), file_path)
            else:
                filename = cls.get_path(file_path)

            with open(filename) as stream:
                content = stream.read()
                if is_stripped:
                    content = content.strip()

                if content:
                    yaml_result = yaml.safe_load(content)
                    cls.message = 'loaded {}'.format(filename)
                else:
                    cls.message = '"{}" file is empty.'.format(filename)

        except Exception as ex:
            cls.message = Text(ex)

        if var_substitution:
            yaml_result = Misc.substitute_variable(yaml_result,
                                                   root_var_name=root_var_name)

        if Misc.is_dict(yaml_result) and dot_datatype:
            dot_result = DotObject(yaml_result)
            return dot_result
        else:
            return yaml_result

    @classmethod
    def save(cls, filename, data):
        """save data to file

        Parameters
        ----------
        filename (str): filename
        data (str): data.

        Returns
        -------
        bool: True if successfully saved, otherwise, False
        """
        try:
            if Misc.is_list(data):
                content = '\n'.join(str(item) for item in data)
            else:
                content = str(data)

            filename = cls.get_path(filename)
            if not cls.create(filename):
                return False

            file_obj = Path(filename)
            file_obj.touch()
            file_obj.write_text(content)
            cls.message = 'Successfully saved data to "{}" file'.format(filename)
            return True
        except Exception as ex:
            cls.message = Text(ex)
            return False

    @classmethod
    def delete(cls, filename):
        """Delete file

        Parameters
        ----------
        filename (str): filename

        Returns
        -------
        bool: True if successfully deleted, otherwise, False
        """
        try:
            filepath = File.get_path(filename)
            file_obj = Path(filepath)
            if file_obj.is_dir():
                file_obj.rmdir()
            else:
                file_obj.unlink()
            cls.message = 'Successfully deleted "{}" file'.format(filename)
            return True
        except Exception as ex:
            cls.message = Text(ex)
            return False

    @classmethod
    def change_home_dir_to_generic(cls, filename):
        """change HOME DIRECTORY in filename to generic name
        ++++++++++++++++++++++++++++++++++++++++++++++
        Note: this function only uses for displaying.
        ++++++++++++++++++++++++++++++++++++++++++++++
        """
        node = Path.home()
        home_dir = str(node)
        if isinstance(node, WindowsPath):
            replaced = '%HOMEDRIVE%\\%HOMEPATH%'
        else:
            replaced = '${HOME}'
        new_name = filename.replace(home_dir, replaced)
        return new_name


class Misc:

    message = ''

    @classmethod
    def is_dict(cls, obj):
        return isinstance(obj, typing.Dict)

    @classmethod
    def is_mapping(cls, obj):
        return isinstance(obj, typing.Mapping)

    @classmethod
    def is_list(cls, obj):
        return isinstance(obj, typing.List)

    @classmethod
    def is_mutable_sequence(cls, obj):
        return isinstance(obj, (typing.List, typing.Tuple, typing.Set))

    @classmethod
    def is_sequence(cls, obj):
        return isinstance(obj, typing.Sequence)

    @classmethod
    def try_to_get_number(cls, obj, return_type=None):
        """Try to get a number

        Parameters
        ----------
        obj (object): a number or text number.
        return_type (int, float, bool): a referred return type.

        Returns
        -------
        tuple: status of number and value of number per referred return type
        """
        chk_lst = [int, float, bool]

        if cls.is_string(obj):
            data = obj.strip()
            try:
                if data.lower() == 'true' or data.lower() == 'false':
                    result = True if data.lower() == 'true' else False
                else:
                    result = float(data) if '.' in data else int(data)

                num = return_type(result) if return_type in chk_lst else result
                return True, num
            except Exception as ex:     # noqa
                cls.message = Text(ex)
                return False, obj
        else:
            is_number = cls.is_number(obj)
            num = return_type(obj) if return_type in chk_lst else obj

            if not is_number:
                txt = obj if cls.is_class(obj) else type(obj)
                cls.message = 'Expecting number type, but got {}'.format(txt)
            return is_number, num

    @classmethod
    def is_integer(cls, obj):
        return isinstance(obj, int)

    @classmethod
    def is_boolean(cls, obj):
        return isinstance(obj, bool)

    @classmethod
    def is_float(cls, obj):
        return isinstance(obj, float)

    @classmethod
    def is_number(cls, obj):
        result = cls.is_boolean(obj)
        result |= cls.is_float(obj)
        return result

    @classmethod
    def is_string(cls, obj):
        return isinstance(obj, typing.Text)

    @classmethod
    def is_class(cls, obj):
        return isinstance(obj, typing.Type)     # noqa

    @classmethod
    def is_callable(cls, obj):
        return isinstance(obj, typing.Callable)

    @classmethod
    def is_iterator(cls, obj):
        return isinstance(obj, typing.Iterator)

    @classmethod
    def is_generator(cls, obj):
        return isinstance(obj, typing.Generator)

    @classmethod
    def is_iterable(cls, obj):
        return isinstance(obj, typing.Iterable)

    @classmethod
    def join_string(cls, *args, **kwargs):
        if not args:
            return ''
        if len(args) == 1:
            return str(args[0])

        sep = kwargs.get('separator', '')
        sep = kwargs.get('sep', sep)
        return sep.join(str(item) for item in args)

    @classmethod
    def skip_first_line(cls, data):
        if not cls.is_string(data):
            return data
        else:
            new_data = '\n'.join(data.splitlines()[1:])
            return new_data

    @classmethod
    def substitute_variable(cls, data, root_var_name='self'):
        """substitute variable within data structure if there

        Parameters
        ----------
        data (dict): a dictionary.
        root_var_name (str): root variable of data structure for
                variable substitution.  Default is self.

        Returns
        -------
        dict: a new dictionary if substituted, otherwise, the given data.

        """
        def replace(txt, **kwargs):
            if len(kwargs) == 1:
                var_name = list(kwargs)[0]
                pattern = r'(?i)[{]%s([.][a-z]\w*)+[}]' % var_name
            else:
                pattern = r'(?i)[{][a-z]\w*([.][a-z]\w*)+[}]'
            lines = txt.splitlines()
            for index, line in enumerate(lines):
                if line.strip():
                    lst = []
                    start = 0
                    for match in re.finditer(pattern, line):
                        lst.append(line[start:match.start()])
                        start = match.end()
                        matched_result = match.group()
                        try:
                            val = matched_result.format(**kwargs)
                            lst.append(val)
                        except Exception as ex:     # noqa
                            lst.append(matched_result)
                    else:
                        if lst:
                            lst.append(line[start:])
                            lines[index] = ''.join(lst)

            new_txt = '\n'.join(lines)
            return new_txt

        def substitute(node, variables_):
            if cls.is_dict(node):
                for key, val in node.items():
                    if cls.is_dict(val) or cls.is_list(val):
                        substitute(val, variables_)
                    else:
                        if cls.is_string(val):
                            new_val = replace(val, **variables_)
                            node[key] = new_val
            elif cls.is_list(node):
                for index, item in enumerate(node):
                    if cls.is_dict(item) or cls.is_list(item):
                        substitute(item, variables_)
                    else:
                        if cls.is_string(item):
                            new_item = item.format(obj=variables_)
                            node[index] = new_item
            else:
                return

        if not cls.is_dict(data):
            return data

        new_data = deepcopy(data)
        variables = {root_var_name: DotObject(deepcopy(new_data))}
        substitute(new_data, variables)
        return new_data


class MiscArgs:
    @classmethod
    def get_parsed_result_as_data_or_file(cls, *kwflags, data=''):
        try:
            parser = ArgumentParser(exit_on_error=False)
        except Exception as ex:     # noqa
            parser = ArgumentParser()

        parser.add_argument('val1', nargs='*')
        parser.add_argument('--file', type=str, default='')
        parser.add_argument('--filename', type=str, default='')
        parser.add_argument('--file-name', type=str, default='')
        for flag in kwflags:
            parser.add_argument(flag, type=str, default='')
        parser.add_argument('val2', nargs='*')

        data = str(data).strip()
        first_line = '\n'.join(data.splitlines()[:1])
        pattern = '(?i)file(_?name)?$'

        result = DotObject(
            is_parsed=False, is_data=False, data=data,
            is_file=False, filename='', failure=''
        )

        try:
            options = parser.parse_args(re.split(r' +', first_line))
            result.is_parsed = True
            for flag, val in vars(options).items():
                if re.match(pattern, flag) and val.strip():
                    result.is_file = True
                    result.filename = val.strip()
                else:
                    if flag != 'val1' or flag != 'val2':
                        if val.strip():
                            result.is_data = True
                            result.data = val.strip()
                            return result

            if result.val1 or result.val2:
                result.is_data = True
                return result
            else:
                result.is_parsed = False
                result.failure = 'Invalid data'
                return result

        except Exception as ex:
            result.failure = '{}: {}'.format(type(ex).__name__, ex)
            result.is_parsed = False
            return result


class MiscOutput:
    @classmethod
    def execute_shell_command(cls, cmdline):
        exit_code, output = subprocess.getstatusoutput(cmdline)
        result = DotObject(
            output=output,
            exit_code=exit_code,
            is_success=exit_code == ECODE.SUCCESS
        )
        return result


class DictObject(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(*args, **kwargs)

    def __setattr__(self, attr, value):
        super().__setattr__(attr, value)
        self.update(**{attr: value, 'is_updated_attr': False})

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.update({key: value})

    def update(self, *args, is_updated_attr=True, **kwargs):
        obj = dict(*args, **kwargs)
        super().update(obj)
        if is_updated_attr:
            for attr, value in obj.items():
                if Misc.is_string(attr) and re.match(r'(?i)[a-z]\w*$', attr):
                    setattr(self, attr, value)


class DotObject(DictObject):
    def __getattribute__(self, attr):
        value = super().__getattribute__(attr)
        return DotObject(value) if Misc.is_dict(value) else value

    def __getitem__(self, key):
        value = super().__getitem__(key)
        return DotObject(value) if Misc.is_dict(value) else value


def parse_template_result(test_data='', test_file='',
                          template_data='', template_file=''):

    if not any([test_data, test_file]):
        failure = 'Neither test_data nor test_file CANT be empty.'
        raise UtilsParsedTemplateError(failure)
    else:
        if not test_data:
            if File.is_exist(test_file):
                test_data = File.get_content(test_file)
            else:
                failure = '%r test data file is not existed.' % test_file
                raise UtilsParsedTemplateError(failure)

    if not any([template_data, template_file]):
        failure = 'Neither template_data nor template_file CANT be empty.'
        raise UtilsParsedTemplateError(failure)
    else:
        if template_data:
            template = template_data
        else:
            if File.is_exist(template_file):
                template = File.get_content(template_file)
            else:
                failure = '%r template file is not existed.' % template_file
                raise UtilsParsedTemplateError(failure)

    try:
        stream = StringIO(template)
        parser = TextFSM(stream)
        rows = parser.ParseTextToDicts(test_data)

        result = DotObject(
            test_data=test_data, template=template,
            records=rows, records_count=len(rows)
        )
        return result
    except Exception as ex:
        failure = 'BAD-TEMPLATE ({})'.format(Text(ex))
        raise UtilsParsedTemplateError(failure)
