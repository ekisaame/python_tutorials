a="Emma"
b="Kisaame Keith Susan"
identity=(a,b)
print identity[0]

#length of string
length=len(b)
print("length of: {0}".format(length))
c=b.split(" ")
print(c)
first_str=c[1]
print("split string {0}".format(first_str))

#method for changing the case
i=0
for s in c:
	i=i+1
	upper=s.lower()
	print("lower cased string: "+str(i)+" "+upper)
