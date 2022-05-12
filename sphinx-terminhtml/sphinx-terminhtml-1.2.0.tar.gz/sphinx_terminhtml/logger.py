import logging
import sys
from enum import Enum

from pydantic import BaseSettings, validator
from rich.logging import RichHandler


class LogLevel(str, Enum):
    INFO = "INFO"
    DEBUG = "DEBUG"


class LoggingConfig(BaseSettings):
    level: LogLevel = LogLevel.INFO

    class Config:
        env_prefix = "SPHINX_TERMINHTML_LOG_"

    @validator("level", pre=True)
    def cast_log_level(cls, v):
        if isinstance(v, LogLevel):
            return v
        level = str(v).casefold().strip()
        if level == "info":
            return LogLevel.INFO
        elif level == "debug":
            return LogLevel.DEBUG
        raise ValueError(f"invalid log level {level}")


LOGGING_CONFIG = LoggingConfig()

log = logging.getLogger("capiq-customer-supplier")
log.setLevel(LOGGING_CONFIG.level.value)
formatter = logging.Formatter("%(message)s", datefmt="[%X]")

ch = logging.StreamHandler(stream=sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

log.handlers = []
log.addHandler(ch)
log.addHandler(RichHandler(rich_tracebacks=True))


if __name__ == "__main__":
    log.info("info level")
    log.debug("debug level")
    try:
        raise ValueError("exception")
    except ValueError as e:
        log.exception(e)
