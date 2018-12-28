import os
import sqlite3
import glob2

# os is a module (single file)
# sqlite3 is a library (collection of files)
# glob2 is a 3rd-party package installed via pip

files = os.listdir()
print(files[0])

r = sqlite3.Cache(1)
print(type(r))

y = glob2.__version__
x = glob2.glob("*")
print(y)
print(type(y))
print(x)
print(type(x))