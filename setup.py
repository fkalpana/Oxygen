from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in oxygen/__init__.py
from oxygen import __version__ as version

setup(
	name="oxygen",
	version=version,
	description="Oxygen",
	author="Claudion",
	author_email="farook@htsqatar.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
