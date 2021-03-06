'''
This file contains all the functions which return the list for
different time stamps or different slices

Author: Yan Gao
email: gaoy4477@gmail.com
'''

import os
import glob

def get_folder(path, keyword):
	# assigin the path, and return all the target folder (SHP...) as a sorted list
	all_files = os.listdir(path)
	all_files.sort()
	all_folder = [i for i in all_files if keyword in i]
	return all_folder

def get_allslice(path):
	# this function need to assign the path and will return all the ".tif" files as a sorted list
	all_files = glob.glob(os.path.join(path,'*.tif'))
	all_files.sort()
	return all_files

def get_allsegment(path):
	# this function need to assign the path and will return all the ".tif" files as a sorted list
	all_files = glob.glob(os.path.join(path,'*.png'))
	all_files.sort()
	return all_files
