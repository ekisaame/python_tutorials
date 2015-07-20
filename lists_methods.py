list = ['larry', 'curly', 'molly','molly']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print list  ## ['xxx', 'larry', 'curly', 'molly', 'shemp', 'yyy', 'zzz']
print list.index('curly')    ## 2

list.remove('curly')         ## search and remove that element
n=list.pop(1)  
print n                ## extracts and returns 'larry'
print list  ## ['xxx', 'molly', 'shemp', 'yyy', 'zzz']
x=list.count('wobly')
print x 
#string methods
s=list[1]
res=s[1:4]
print res 
# s.replace ("rry" ,"m")
# print s