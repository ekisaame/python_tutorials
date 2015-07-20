#global variable: This variable is defined outside the function definitions and is 
#visible/usable by all the functions under it or above it. Once indented however,
#it will cease to be global and only apply to the function under which it has been defined.
name = "Alex"

def nameFun():
    f_name = "allan"
    print("my name : "+f_name)
    print("global Name: "+name)

def newName():
    f_name = "lukwago"
    print("my name : "+name)

def modifyGlobal():
    global name
    #print name
    name=name.capitalize()
    print("in modify globale: "+name)
