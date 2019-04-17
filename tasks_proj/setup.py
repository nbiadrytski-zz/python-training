"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages

setup(
    name='tasks',
    version='0.1.0',
    license='proprietary',
    description='Minimal Project Task Management',

    author='Test Testovich',
    author_email='test@test.com',
    url='https://test.com',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['click', 'tinydb', 'six'],
    extras_require={'mongo': 'pymongo'},

    entry_points={
        'console_scripts': [
            'tasks = tasks.cli:tasks_cli',
        ]
    },
)
