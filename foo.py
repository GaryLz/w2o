import os
import shutil
print(os.getcwd())
fpath = os.path.join(os.path.abspath(os.curdir), 'w2o.py')
print(fpath)
print(os.path.split(fpath))
print(os.getcwd())