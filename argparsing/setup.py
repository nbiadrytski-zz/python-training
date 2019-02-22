from setuptools import setup, find_packages
"""
the runnable will be called argparsing,
and when executed it will run the main function in the __main__
which is part of the argparsing package.
"""


setup(
    name='argparsing',
    version='1.0.0',
    packages=find_packages(),
    entry_points={'console_scripts': ['argparsing = argparsing.__main__:main']}
)