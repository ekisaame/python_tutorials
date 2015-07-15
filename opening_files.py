file_location="C:/Users/emmanuelk.DI/Documents/python_tutorials/text.txt"
file_location1="C:/Users/emmanuelk.DI/Documents/python_tutorials/marks.txt"
file_location2="C:/Users/emmanuelk.DI/Documents/python_tutorials/position.txt"
files=[file_location,file_location1,file_location2]

def open_file(file_name):
	file=open(file_name,"r")
	data=file.readlines()
	print data
 	return data

open_file(file_location)
i=0
for i in range(0,3):
	current_file=files[i]
	d=open_file(current_file)
	i=i+1
	print(d)

