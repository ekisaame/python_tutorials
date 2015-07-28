#importing all data files I will use for this programme.
file_location="C:/Users/emmanuelk.DI/Documents/python_tutorials/Keith_scores.txt"
file_location1="C:/Users/emmanuelk.DI/Documents/python_tutorials/Sophie_scores.txt"
file_location2="C:/Users/emmanuelk.DI/Documents/python_tutorials/Richard_scores.txt"
files=[file_location,file_location1,file_location2]

#opening the files
def open_file(files):
	file=open(files, "r")
	data=file.readlines()
	print (data)
# return data
# i=0
# # for i in range (0,3):
#  		current_file=files[i]
# 		i=i+1
#  		d=open_file(current_file)
# print (d)

