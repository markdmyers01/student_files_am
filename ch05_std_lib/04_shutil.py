"""
    04_shutil.py

    Before running:
                        ch05_std_lib
                              |
                              |__temp (empty)

    After running:
                        ch05_std_lib
                              |
                              |__temp (with 9 files)
                              |
                              |_ temp2 (with 9 files)
"""
import os
import shutil

temp = './temp'
temp2 = './temp2'
temp_temp2 = './temp/temp2'

if not os.path.exists(temp):
    os.mkdir(temp)
else:
    shutil.rmtree(temp)
    os.mkdir(temp)

for f in os.listdir('.'):
    if f.endswith('.py'):
        shutil.copy(f, temp)

if os.path.exists(temp2):
    shutil.rmtree(temp2)

shutil.copytree(temp, temp_temp2)
shutil.move(temp_temp2, '.')
