import os
import glob as gl

# printing xml files from cur dir using absolute path
print([os.path.abspath(f) for f in gl.glob('*.xml')])

# printing xml files with size > 0 bytes from cur dir using relative path
print([os.path.relpath(f) for f in gl.glob('*.xml') if os.stat(f).st_size > 0])

# printing xml files and their size in cur dir using relative path
print([(os.stat(f).st_size, os.path.relpath(f)) for f in gl.glob('*.xml')])

a_list = [1, 9, 8, 4]

# multiply each elem in a_list by 2
b_list = [elem * 2 for elem in a_list]
print(b_list)
