import os
path = "E:/Image set/aa/"

for item in os.listdir(path) :
 # Read in the file
 with open(item, 'r') as file :
   filedata = file.read()

 # Replace the target string
 filedata = filedata.replace('Mask-Ok','Mask-Ok')
 #filedata2 = filedata.replace('Non Mask :(','No-Mask')
 # Write the file out again
 with open(item, 'w') as file:
   file.write(filedata)
  # file.write(filedata2)
