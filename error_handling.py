#i = 5
#if i%2 == 0:
 #   print("odd")
#else:
#    print("even")
# zero division error:
#try:
 #   a = int(input("enter the numerator: "))
 #   b = int(input("enter the dinominator: "))
#    c = a%b
#    print(c)
#except : 
#    print("error: division by zero is not possible")  
#
#try:
#    i = 3
#    n = int(input("enter the n value: "))
#    if i%n==0:
 #       print("yes,number is multiple of",n)
 #   else:
#        print("no, number not is multiple of",n)

#except ZeroDivisionError:
 #   print("error:dividion by zero is not possible")

# value error :
#ry:
#    rollno = int(input("enter your rollno:"))
#except ValueError:
#    print("error: given value is not in the integer datatype.")

# indexerror:
try:
    list = [10,20,30] 
    print(list[5])   
except:
    print("error: the given index is not from the list")

# keyerrror:
try:
    dict = {"name":"aswitha","rollno":"q0"}
    print(dict["age"])
except KeyError:
    print("error: the given key is not from the list")

# type error:
try:
    list = [10,20,30] 
    sum = list + 5
    print(sum) 
except TypeError:
     print("invalid type operation.") 

# name error:
try:
    print(mult)
except NameError:
    print("variable not declared")    

# file not found error:
try:
    file = open("detail.txt","w")
    print(file.read())
except:
    print("file is not found in the system.")
finally:
    print("program is excuted")                 