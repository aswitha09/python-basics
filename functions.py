#functions:
def greet(name,branch):
    print("hello world",name,branch)
greet("aswitha","cse AI & ML") 

# positional arguments:
def greet(name,rollno):
    print("hello",name,"your rollno is",rollno)
greet("aswitha","Q0")
# keyword arguments:
def greet(rollno,name):
    print("hello",name,"your rollno is",rollno)
greet(name="aswitha",rollno="Q0") 
# default arguments:
def greet(name = "student"):
    print("hello",name)
greet()
greet(name = "aswitha")    
# variable-length arguments:
def sum1(*list1):
    sum2 = 0
    for i in range(len(list1)):
        sum2 = sum2 + list1[i]
    print(sum2)
    print(type(list1))
sum1(10,20,30,40,50)
# ***kwargs:(keyword variable-length arguments)
# collects multiple key=value pair into a dictionary.
def details(**info):
    for i,j in info.items():
        print(i,":",j)
details(name="aswitha",rollno="Q0",branch="csm")   
# scope of the variable:
x  = 10
def var1():
    y = 5
    print("inside var1 function",x)
var1()
def var2():
    print("inside var2 function",x)
var2()
print("outside function",x)  

# lamda function:
#normal function:
def sqe(a):
    print(a*a)
sqe(5) 
#files
file = open("student.txt","w")
file.close()

