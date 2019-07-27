from setuptools import setup
import re

__version__, = re.findall('__version__ = "(.*)"', open('regex_intersections/__init__.py').read())

setup(
    name='regex_intersections',
    version=__version__,
    packages=['regex_intersection', 'regex_intersections.utils'],
    install_requires=['dataclasses; python_version<"3.7"'],
    author='MegaIng',
    author_email='MegaIng <trampchamp@hotmail.de>',
    description="a regex intersection checker",
    license="MIT",
    url='https://github.com/MegaIng/regex_intersections',
    download_url='https://github.com/MegaIng/regex_intersections/tarball/master',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
