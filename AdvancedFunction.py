

##   Postional argument 

def info(name,age): 
    print(" My Name is:",name,"\n","And My Age is:",age)

info(18,18)  #postion is requeired 


##   Keyword Argument

def info1(name , age):
    print(" My Name is:",name,"\n","And My Age is:",age)

info1( age = 18 , name = 'Moyed') ##


##   Defult Parmater

def info2(name = 'Mohammed', age = 18):
    print(" My Name is:",name,"\n","And My Age is:",age)

info2() ## there is a defult paramter will fill the values


##    Argument Packing
def avarge(*args):     ## can input unlimted parmeter if you use this symbol *  
    total = sum(args)
    leng = len(args)

    avg = total/leng
    print(avg)

avarge(12,23,43,45,65,32)
avarge(1,2,3)
avarge(2,4)


##    Argument Unpacking

def names(name1 , name2, name3):
    print(" My Name is:",name1,'\n','My Name is:',name2,'\n','My Name is:',name3)


name = ['Moyed' , 'Mohammed' , 'Hakem']
names(*name)    ## fill it auto no need to  fill the basic way like --> name[0], name[1], name[2]


##    Packing & Unpacking

def my_function(*items):
    print(items)

items = ['a' , 'b' , 'c']
my_function(items)  ##  as we can see the func output as a one argument (['a', 'b', 'c'],) not a three argument ('a', 'b', 'c')  
my_function(*items) ## now it will output three parmeters ('a', 'b', 'c') not one parmeter (['a', 'b', 'c'],) 

##    Argument Dictionary Packing


def dic(**kwargs):
    print(kwargs)
    print(type(kwargs))

dic(name='Moyed' ,age = 19, course ="Python102" )    


#####

