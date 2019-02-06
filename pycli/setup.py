from setuptools import setup
"""
the runnable will be called pycli,
and when executed it will run the main function in the __main__ module
which is part of the pycli package.
"""


setup(
    name='pycli',
    version='1.0.0',
    packages=['pycli'],
    entry_points={'console_scripts': ['pycli = pycli.__main__:main']}
)
