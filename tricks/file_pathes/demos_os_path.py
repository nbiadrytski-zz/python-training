from pathlib import Path

# https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/
# https://treyhunner.com/2019/01/no-really-pathlib-is-great/



CURRENT_DIR = Path(__file__).resolve().parent
print(CURRENT_DIR)
# /Users/mikalai_biadrytski/Documents/autotests/udemy_python/python-training/tricks/file_pathes

CURRENT_PARENT_DIR = Path(__file__).resolve().parent.parent
print(CURRENT_PARENT_DIR)
# /Users/mikalai_biadrytski/Documents/autotests/udemy_python/python-training/tricks

TEMPLATES_DIR = CURRENT_PARENT_DIR.joinpath('templates')
print(TEMPLATES_DIR)
# /Users/mikalai_biadrytski/Documents/autotests/udemy_python/python-training/tricks/templates

# create src/__pypackages__ directory inside current directory
Path('src/__pypackages__').mkdir(parents=True, exist_ok=True)
# Path('.editorconfig').rename('src/.editorconfig')
