'''
Helper routines handeling sys calls for conversion/cleanup.
'''

import sh
import os

def Delete(filePath):
	sh.rm(filePath)

def Convert(filePath,format):
	newPath = '.'.join(os.path.splitext(filePath)[:-1]).strip()+format
	if os.path.exists(newPath):
		Delete(newPath)
	sh.avconvert('-i',filePath,newPath)
	return newPath