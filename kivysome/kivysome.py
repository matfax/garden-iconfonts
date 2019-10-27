import re
from enum import Enum

import urllib3
from lastversion import lastversion
from mutapath import Path
from remotezip import RemoteZip
from urllib3.exceptions import MaxRetryError

from kivysome.iconfonts import register, create_fontdict_file

_VERSION_MATCHER = re.compile(r'.*"version":"([a-zA-Z0-9.]+)"')


class FontGroup(Enum):
    SOLID = "solid"
    REGULAR = "regular"
    BRANDS = "brands"


def enable(url: str, group: FontGroup = FontGroup.REGULAR, force: bool = False, font_folder=Path.getcwd() / "fonts"):
    """
    All-in-one function to deploy free Font Awesome fonts.
    It fetches the font file with the version from the given Font Awesome kit script file,
    converts the css and registers it as primary font.
    :param url: the script for your font kit from https://fontawesome.com/kits
    :param group: a valid ::class:`~kivysome.FontGroup`
    :param force: to ignore the existing files and refetch them by force
    :param font_folder: to folder to put the font files, "fonts" is used as default
    """
    font_folder = Path(font_folder)

    pool_manager = urllib3.PoolManager()
    try:
        result = pool_manager.request("GET", url)
    except MaxRetryError as e:
        raise ValueError("the given link could not be accessed") from e
    if not result.status == 200:
        raise ValueError("the given link did not return a correct status code")
    content = result.data.decode('utf-8')
    if '"license":"free"' not in content:
        raise ValueError("the given link is not referencing a free version of a Font Awesome kit")
    version_match = _VERSION_MATCHER.match(content)
    if version_match is None:
        raise ValueError("no version could be parsed from the given link")

    version = version_match.group(1)
    if version == "latest":
        repo = "FortAwesome/Font-Awesome"
        version = lastversion.latest(repo, 'version')

    download_link = f"https://use.fontawesome.com/releases/v{version}/fontawesome-free-{version}-web.zip"

    ttf_local = font_folder / f"fa-{group.value}-{version}.ttf"
    css_local = ttf_local.with_suffix(".css")
    fontd_local = ttf_local.with_suffix(".fontd")

    if force or not ttf_local.isfile() or not css_local.isfile():

        with RemoteZip(download_link) as remote_zip:
            ttf_file: str = ""
            css_file: str = ""
            for file_name in remote_zip.namelist():
                if group.value in file_name and file_name.endswith(".ttf"):
                    ttf_file = file_name
                elif file_name.endswith("all.css"):
                    css_file = file_name

            if not ttf_file or not css_file:
                raise ValueError(f"the required font files could not be found in the remote zip file {download_link}")

            if ttf_local.exists():
                if not remote_zip.getinfo(ttf_file).file_size == ttf_local.size:
                    ttf_local.remove()
            if css_local.exists():
                if not remote_zip.getinfo(css_file).file_size == css_local.size:
                    css_local.remove()

            if not ttf_local.exists():
                target_path = remote_zip.extract(ttf_file, font_folder)
                Path(target_path).move(ttf_local)
            if not css_local.exists():
                target_path = remote_zip.extract(css_file, font_folder)
                Path(target_path).move(css_local)

            for tmp_folder in font_folder.dirs(f"*{version}*"):
                if len(list(tmp_folder.walkfiles())) == 0:
                    tmp_folder.rmtree()

    if force or not fontd_local.isfile():
        create_fontdict_file(css_local, fontd_local)

    register(f"fontawesome-{group}", ttf_local, fontd_local)
