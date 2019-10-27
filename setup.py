import json
from pathlib import Path
from typing import Optional, List

from setuptools import setup, find_packages


def get_dependencies(pipfile_lock: Optional[str] = None, develop: bool = False):
    if pipfile_lock is None:
        pipfile_lock = "Pipfile.lock"
    lock_data = json.load(Path(pipfile_lock).open())
    result: List[str] = [package_name for package_name in lock_data.get('default', {}).keys()]
    if develop:
        result += [package_name for package_name in lock_data.get('develop', {}).keys()]
    return result


setup(
    name="kivysome",
    packages=find_packages(),
    version_config={
        "template": "{tag}",
        "dev_template": "{tag}.dev{ccount}+git.{sha}",
        "dirty_template": "{tag}",
    },
    license="MIT",
    description="Font Awesome 5 Icons for Kivy",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="matfax",
    author_email="matthias.fax@gmail.com",
    url="https://github.com/matfax/kivysome",
    keywords=["kivy", "fa", "font", "awesome", "icons"],
    setup_requires=["setuptools-git-ver"],
    install_requires=get_dependencies(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.7"
)
