#collection data types
#list1 = [10,20,30,40,50]
#print(list1)
#list4 = [10,20.5,"hello",True,"flase"]
#print(list4)
#list1 = [2,3,4,5,6]
#print(list1[1:4])
#print(list1[-4:3])
#print(list1[2:4])
#slcl = ["prabhas","balayya","pspk","vdk","bhai"]
#print(slcl[:3])
#print(slcl[1:4])
#print(slcl[-3:1])
#print(slcl[2:3])
#print(slcl[0:5])
#print(slcl[-3:])

#kalkicast = ["prabhas","kamal h","amitha bachan","deepika p","ssr"]
#print(kalkicast)
#kalkicast.append("deesha patani")
#print(kalkicast)
#kalkicast.insert(2,"vijay D")
#print(kalkicast)
#kalkicast.extend(["anudeep","mrunal T","bujji"])
#print(kalkicast)
#kalkicast.remove("kamal h")
#print(kalkicast)
#kalkicast.pop(2)
#print(kalkicast)
#kalkicast.clear()
#print(kalkicast)
#kalkicast[1] = "sandeep R V"
#print(kalkicast)
#a = [1,2]
#b = [3,4]
#c = a+b
#print(c)
#a = [1,2]
#n = int(input("enter the n value:"))
#b = a*n
#print(b)

# searching and checking:
#a = [2,4,6,8,10,12,14]
#if 2 in a :
 #   print("yes, item is present in the list")
#    print(3 not in a)
#print(a.index(8))
#cnt = 0
#print(a.count(8))
#for i in range(10):
#    if i == 8:
#        cnt = cnt + 1
#print(cnt)

#st = [25,12,5,31,13,18,7,45,8,55,68]        
# AO = 5,7,8,12,13,18,25,31,45,55,68
#st.reverse()
#st.sort()
#print(st)      
#DO = 68,55,45,31,25,18,13,12,8,7,5
#st.reverse()
#print(st) 

# copying the list:

#frd1 = ["A","C","D","A","D","B","B","C","C","A","A"]
#frd2 = frd1.copy()
#frd2[2] = "B"
#print(frd2)
#st = [25,12,5,31,13,18,7,45,8,55,68]
#print(len(st))
#print(max(st))
#print(min(st))
#print(sum(st))
#a = "hello world to the python programing"
#b = a.split()
#print(b)

# multiple values using input data to the list

#a = list(map(int,input("enter the multiple values:").split()))
#print(a)
#print(max(a))
#b = input("enter the multiple values:").split()
#print(b)

#traversing a list:

# accessing the elements using a loop
#cars = ["thar","jaguer","audi","nano"]
#for car in cars:
#    print("cars=",car)

# using index with for loop:

#print(len(cars))
#for i in range(0,4):
 #   print("cars",i,cars[i])

# adding elements using for loop:

#10
# list1 = []
#n = int(input("enter the number of list  values: "))
#for i in range(0,n):
#   a = input("enter the list values: ")
#   list1.append(a)
#print(list1)
# give the input values to the llists from 0 to 10
#list1 = []
#n = int(input("enter the number of  list values: "))
#for i in range(n):
   #a = input("enter the list values: ")
   #list1.append(i)
  # print(list1)

# sum of list items = 10 20 30 40 50 without using sum().
#list1 = [10,20,30,40,50]
#sum = 1
#for i in list:
    #sum =  sum * i 
    #print(sum)   

# convert ["p","y","t","h,"o","n"] to python
#list1 = ["y","t","h","o","n"]
#word = "p"
#for i in list1:
#    word = word + i
#print(word)

# find the maximum and minimum number from list without using max() and min():
#list = [2,3,7,6,4,5,9]
#list.sort()
#print(list)
#print("maximum of list :",list[6])
#print("minimum of list :",list[0]) 

# find the maximum and minimum number from list without using max() , min() , sort().
#list1 = [2,6,7,3,1,8,9]
#max1 = list1[0]
#min1 = list1[0]
#for num in list1:
#    if num > max1:
#        max1 = num
#    if num < min1:
#        min1 = num
#print(max1)
#print(min1)

# searching for an element in a list
  
#names = ["mallareddy","revanth reddy","modi","rahul gandhi"]
#searching_name = input("enter the name to be found: ")
#found = False
#for i in names:
#    if searching_name == i:
#       found = True

#if found:
#    print("yes")
#else:
#    print("no") 

 # count even and odd numbers

#numbers = [1,2,3,4,5,6,7,8,9]

#evn_cnt = 0
#odd_cnt = 0
#for i in range(len(numbers)):
 #   if numbers[i]%2 ==0:
 #       evn_cnt += 1
 #   else:
 #       odd_cnt += 1
#print("number of even numbers are: ",evn_cnt)
#print("number of odd numbers are: ",odd_cnt)

#reversing a list without reverse
#list1 = [7,10,12,17,18,23,31,45,227,229]
#l = len(list1)
#r_list = []
#for i in range(l-1,-1,-1):
#    r_list.append(list1[i])
#print(r_list)    

# removing all negative using loop   
#numbers = [2,-4,5,-8,32,-9]
#positive_list = []

#for i in range(len(numbers)):
#    if numbers[i] > 0:
#        positive_list.append(numbers[i])
#print(positive_list)        

#multiply each element in the list
#numbers = [56,92,8,30,30,45,23,19,72,55,18,7,0]
#n = int(input("enter the number to be multiplied: "))
#after_multiplication = []
#for i in numbers:
 #   after_multiplication.append(i*n)
#print(after_multiplication)

## take a list of names and print the longest name:
#list = ["aswitha","rupika","varshitha"]
#word = ""
#for i in list:
#    word = word + i
#print(word)

# print all -ve , +ve , 0's in the list :
list = [2,3,-5,0,-9,-23,8,0,4] 
positive_list = []
negitive_list = []
zero_list = []
for i in range(len(list)):
   if list [i] > 0:
      positive_list.append(list[i]) 
   if list [i] < 0:
        negitive_list.append(list[i])
   if list [i] == 0:
        zero_list.append(list[i])  
print(positive_list)
print(negitive_list)
print(zero_list)              