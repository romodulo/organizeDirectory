#! /usr/bin/python3
# i intend to organize my dirs

import os
from pprint import pprint
import sys

#write a function that takes
# a system argument and 
# write that system argument
# into a text file
# line-by-line
def placeholder01():
    pass
    #write something

#write a function that
# opens; closes; a file 
# within those two actions
# write some content
# into the file
def fileWrite(filename="temporaryText.txt"):
    #check if file exists
    #
    # ...
    if os.path.exists(filename):
        print("file exists")
    else:
        # print("return_value:", os.path.exists(filename))
        # print('file doesn t exist') 
        # print('...creating file')
        fileObj = open(filename, "w")
        fileObj.close()
        print('File-created')
    # deprecated: 
    # fileObj = open(filename, "a")
    # fileObj.write('content---appended\n')
    # fileObj.close()
    #write something
# function required:
# function that outputs all directories; filenames; 
# to a txt file. 
#write to a file
def file_open(filename="temporaryText.txt", payload=None): #not applicable somewhere
    fileObj = open(filename, "a")
    fileObj.write(f'{payload}\n')
    fileObj.close
#switch?
def file_open_2(filename="temporaryText.txt", payload=None): #not applicable somewhere
    baseDir = os.getcwd()
    print('baseDir:', baseDir)
    # combineDTest = os.path.join(baseDir, "organize_home_Dir")
    # print('combineDTest:', combineDTest, "type:", type(combineDTest))
    target_Path = os.path.join(baseDir, "organize_home_Dir", filename)
    fileObj = open(target_Path, "a")
    fileObj.write(f'{payload}\n')
    fileObj.close

# I can utilize a switch case for 
# - default configuration
# - test_default configuration

#attempt to use/utilize sys
if len(sys.argv) == 3:
    if sys.argv[1] == 'default':
        sys_argv_pos1 = "temporaryText.txt"
    elif sys.argv[1] == 'test_default':
        sys_argv_pos1 = "test_defaultTemporary.txt"
    else:
        sys_argv_pos1 = sys.argv[1]

    sys_argv_pos2 = sys.argv[2]
    # print(type(sys_argv_pos2))
    #check if file exists:
    fileWrite(sys_argv_pos1)
    file_open_2(sys_argv_pos1, sys_argv_pos2)
    print(f'"{sys_argv_pos2}" written in \'{sys_argv_pos1}\'')
    print("system exits.")
    sys.exit()
else:
    print("expect only two arguments for this command.")
    sys.exit()

os.system("ls")
# print(os.getcwd())
# pprint(os.listdir('/home/romel-linux'))