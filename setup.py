"""
    setup.py
    --------
    Install book as a package
"""
from setuptools import setup


setup(
    name="cookbook",
    version="0.0.1",
    description="A collection of python references as a package",
    author_email="dillan@teaglebuilt.com",
    packages=["cookbook"],
    install_requires=['pytest']
)
