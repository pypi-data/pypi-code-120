from __future__ import annotations

import re

from pyderman.util import downloader

_stable = "https://msedgedriver.azureedge.net/LATEST_STABLE"
_base_version = "https://msedgedriver.azureedge.net/LATEST_RELEASE"
_base_download = "https://msedgedriver.azureedge.net/{}/edgedriver_{}{}.zip"


def get_url(
    version: str = "latest", _os: str | None = None, _os_bit: str | None = None
) -> tuple[str, str, str]:

    if _os == "win":
        _os_name = "WINDOWS"
    elif _os == "linux":
        _os_name = "LINUX"
    elif _os == "mac":
        _os_name = "MACOS"
    else:
        raise OSError("There is no valid EdgeDriver release for {}".format(_os))

    if version in ("latest", "stable"):
        resolved_version = downloader.raw(_stable, "utf-16")
        resolved_version = resolved_version.strip() if resolved_version else ""

        if version == "latest":
            match = re.match(r"^(\d*)[.]?(\d*)[.]?(\d*)[.]?(\d*)$", resolved_version)
            if match:
                major, minor, patch, build = match.groups()
                _url = "{}_{}_{}".format(_base_version, major, _os_name)
                resolved_version = downloader.raw(_url, "utf-16")
                resolved_version = resolved_version.strip() if resolved_version else ""
    else:
        resolved_version = version

    url = _base_download.format(resolved_version, _os, _os_bit)

    if not resolved_version:
        raise Exception("Unable to locate EdgeDriver version: {}!".format(version))
    return "msedgedriver", url, resolved_version


if __name__ == "__main__":
    print(get_url("latest", "win", "64"))
    print(get_url("latest", "linux", "64"))
