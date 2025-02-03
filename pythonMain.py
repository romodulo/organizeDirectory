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
def fileWrite():
    #check if file exists
    #
    # ...
    if os.path.exists("temporaryText.txt"):
        print("return_value:", os.path.exists("temporaryText.txt"))
        print("file exists")
    else:
        print("return_value:", os.path.exists("temporaryText.txt"))
        print('file doesn t exist') 
        print('...creating file')
        fileObj = open("temporaryText.txt". "w")
        fileObj.close()
        print('File-created.')
    if True:
        fileObj = open("temporaryText.txt", "a")
        fileObj.close()
    #write something
#temporarily_run:
fileWrite()

#attempt to use/utilize sys
print(len(sys.argv))
if len(sys.argv) < 0:
    sys.exit()

os.system("ls")
# print(os.getcwd())
# pprint(os.listdir('/home/romel-linux'))
def file_open():
    fileObj = open("listOfDirs.txt", "w")
    fileObj.write('yo')
    fileObj.close