# #importing all data files I will use for this programme.

file_location="C:/Users/emmanuelk.DI/Documents/python_tutorials/Keith_scores.txt"
file_location1="C:/Users/emmanuelk.DI/Documents/python_tutorials/Sophie_scores.txt"
file_location2="C:/Users/emmanuelk.DI/Documents/python_tutorials/Richard_scores.txt"
#separating the student marks
# keith_scores=file_location
# Sophie_scores=file_location1
# richard_scores=file_location2

files=[file_location,file_location1,file_location2]


#opening the files
def open_file(files):
    file=open(files, "r")
    data=file.readlines()
    # print (data)
    return data
#list that will contain each students data
data = []

for current_file in files:
    d=open_file(current_file)
    #add the returned data to the data list
    data.append(d);
    # print data
 
for d in data:
	# grade(d)
	print d
# print ("Keiths marks "+ str(data[0]))
# print ("sophies marks "+ str(data[1]))
# print ("richards marks "+ str(data[2]))
