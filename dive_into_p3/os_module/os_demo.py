import os

# /Users/mikalai_biadrytski/Documents/autotests/udemy_python/python-training/dive_into_p3
print(os.getcwd())

os.chdir('/Users/mikalai_biadrytski/Documents/autotests/udemy_python/python-training/dictionary_app')
# /Users/mikalai_biadrytski/Documents/autotests/udemy_python/python-training/dictionary_app
print(os.getcwd())

# /Users/mikalai_biadrytski/Documents/autotests/udemy_python/python-training/dictionary_app/test
print(os.path.join('/Users/mikalai_biadrytski/Documents/autotests/udemy_python/python-training/dictionary_app', 'test'))

# /Users/mikalai_biadrytski
print(os.path.expanduser('~'))

# /Users/mikalai_biadrytski/Documents/autotests/udemy_python/python-training/dictionary_app/test.py
print(os.path.join(os.path.expanduser('~'), 'Documents', 'autotests', 'udemy_python', 'python-training', 'dictionary_app', 'test.py'))