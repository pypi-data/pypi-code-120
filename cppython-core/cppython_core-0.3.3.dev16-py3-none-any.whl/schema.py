"""
Data types for CPPython that encapsulate the requirements between the plugins and the core library
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from logging import Logger, getLogger
from pathlib import Path
from typing import Optional, Type, TypeVar

from packaging.requirements import InvalidRequirement, Requirement
from pydantic import BaseModel, Extra, Field, validator


class TargetEnum(Enum):
    """
    The C++ build target type
    """

    EXE = "executable"
    STATIC = "static"
    SHARED = "shared"


class PEP621(BaseModel):
    """
    CPPython relevant PEP 621 conforming data
    Because only the partial schema is used, we ignore 'extra' attributes
        Schema: https://www.python.org/dev/peps/pep-0621/
    """

    dynamic: list[str] = Field(default=[], description="https://peps.python.org/pep-0621/#dynamic")
    name: str = Field(description="https://peps.python.org/pep-0621/#name")
    version: Optional[str] = Field(default=None, description="https://peps.python.org/pep-0621/#version")
    description: str = Field(default="", description="https://peps.python.org/pep-0621/#description")

    @validator("version")
    def validate_version(value, values):  # pylint: disable=E0213
        """
        TODO
        """

        if "version" in values["dynamic"]:
            assert value is None
        else:
            assert value is not None

        return value


def _default_install_location() -> Path:

    return Path.home() / ".cppython"


class PEP508(Requirement):
    """
    PEP 508 conforming string
    """

    @classmethod
    def __get_validators__(cls):
        """
        TODO
        """
        yield cls.validate

    @classmethod
    def validate(cls, value):
        """
        TODO
        """
        if not isinstance(value, str):
            raise TypeError("string required")

        # TODO: Manage Requirement specifics

        try:
            definition = Requirement(value)
        except InvalidRequirement as invalid:
            raise ValueError from invalid

        return definition


class CPPythonData(BaseModel, extra=Extra.forbid):
    """
    Data required by the tool
    """

    target: TargetEnum
    dependencies: list[PEP508] = []
    install_path: Path = Field(default=_default_install_location(), alias="install-path")
    tool_path: Path = Field(default=Path("tool/cppython"), alias="tool-path")
    build_path: Path = Field(default=Path("build"), alias="build-path")


class ToolData(BaseModel):
    """
    Tool entry
    This schema is not under our control. Ignore 'extra' attributes
    """

    cppython: Optional[CPPythonData]


class PyProject(BaseModel):
    """
    pyproject.toml schema
    This schema is not under our control. Ignore 'extra' attributes
    """

    project: PEP621
    tool: Optional[ToolData]


class Plugin(ABC):
    """
    Abstract plugin type
    """

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    @abstractmethod
    def name() -> str:
        """
        The name of the plugin, canonicalized
        """
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def group() -> str:
        """
        The plugin group name as used by 'setuptools'
        """
        raise NotImplementedError()

    @classmethod
    @property
    def logger(cls) -> Logger:
        """
        Returns the plugin specific sub-logger
        """

        if not hasattr(cls, "_logger"):
            cls._logger = getLogger(f"cppython.{cls.group()}.{cls.name()}")

        return cls._logger


@dataclass
class InterfaceConfiguration:
    """
    Base class for the configuration data that is passed to the interface
    """


@dataclass
class GeneratorConfiguration:
    """
    Base class for the configuration data that is set by the project for the generator
    """


class GeneratorData(BaseModel, extra=Extra.forbid):
    """
    Base class for the configuration data that will be read by the interface and given to the generator
    """


class Interface(Plugin):
    """
    Abstract type to be inherited by CPPython interfaces
    """

    @abstractmethod
    def __init__(self, configuration: InterfaceConfiguration) -> None:
        """
        TODO
        """
        self._configuration = configuration

        super().__init__()

    @property
    def configuration(self) -> InterfaceConfiguration:
        """
        TODO
        """
        return self._configuration

    @staticmethod
    @abstractmethod
    def name() -> str:
        """
        The name of the plugin, canonicalized
        """
        raise NotImplementedError()

    @staticmethod
    def group() -> str:
        """
        The plugin group name as used by 'setuptools'
        """
        return "interface"

    @abstractmethod
    def write_pyproject(self) -> None:
        """
        Called when CPPython requires the interface to write out pyproject.toml changes
        """
        raise NotImplementedError()


class Generator(Plugin):
    """
    Abstract type to be inherited by CPPython Generator plugins
    """

    @abstractmethod
    def __init__(self, configuration: GeneratorConfiguration, pyproject: PyProject) -> None:
        """
        Allows CPPython to pass the relevant data to constructed Generator plugin
        """
        self._configuration = configuration
        self._pyproject = pyproject

        super().__init__()

    @property
    def configuration(self) -> GeneratorConfiguration:
        """
        TODO
        """
        return self._configuration

    @property
    def pyproject(self) -> PyProject:
        """
        TODO
        """
        return self._pyproject

    @staticmethod
    def group() -> str:
        """
        The plugin group name as used by 'setuptools'
        """
        return "generator"

    @staticmethod
    @abstractmethod
    def name() -> str:
        """
        The string that is matched with the [tool.cppython.generator] string
        """
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def data_type() -> Type[GeneratorData]:
        """
        Returns the pydantic type to cast the generator configuration data to
        """
        raise NotImplementedError()

    @abstractmethod
    def generator_downloaded(self, path: Path) -> bool:
        """
        Returns whether the generator needs to be downloaded
        """
        raise NotImplementedError()

    @abstractmethod
    def download_generator(self, path: Path) -> None:
        """
        Installs the external tooling required by the generator
        """
        raise NotImplementedError()

    @abstractmethod
    def update_generator(self, path: Path) -> None:
        """
        Update the tooling required by the generator
        """
        raise NotImplementedError()

    @abstractmethod
    def install(self) -> Path:
        """
        Called when dependencies need to be installed from a lock file.

        @returns - A Path to the CMake Toolchain file
        """
        raise NotImplementedError()

    @abstractmethod
    def update(self) -> Path:
        """
        Called when dependencies need to be updated and written to the lock file.

        @returns - A Path to the CMake Toolchain file
        """
        raise NotImplementedError()


GeneratorDataT = TypeVar("GeneratorDataT", bound=GeneratorData)
PluginT = TypeVar("PluginT", bound=Plugin)
InterfaceT = TypeVar("InterfaceT", bound=Interface)
GeneratorT = TypeVar("GeneratorT", bound=Generator)

PyProjectT = TypeVar("PyProjectT", bound=PyProject)
