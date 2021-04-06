# checkpath.py

import os
imgfile = os.listdir() 
mainpath = os.getcwd()
print(mainpath)
print(imgfile)
print('==========')

pathlist = []

for img in imgfile:
	if img[-4:] == 'jpeg' or img[-3:] == 'png':
		path = os.path.join(mainpath,img)
		print(path)
		pathlist.append(path)





