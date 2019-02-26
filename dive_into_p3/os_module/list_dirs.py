import os
import glob

os.chdir('/Users/mikalai_biadrytski/Documents/autotests/udemy_python/python-training')

# print all .py files from argparsing folder
print(glob.glob('argparsing/*.py'))  # ['argparsing/__init__.py', 'argparsing/setup.py', 'argparsing/__main__.py']

# chdir with relative path
os.chdir('argparsing/')
print(os.getcwd())
print(glob.glob('*et*.py'))  # ['setup.py']

