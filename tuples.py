# tuples:
#coordinates = ("x","y")
#my_tuple = (10,20,30)
#print(my_tuple)
#print(type(my_tuple))

# creating a tuple:
# empty tuple
#Et = ()
# tuple with numbers:
#N = (1,2,3,4,5,6)
#tuple with strings:
#S = ("A","B","C","a","b","c")
# tuple with mixed datatypes
#M = (24,3.15,"A","C",True,"false")

# tuple with single element:
#a = 10
#print(type(a))
#b = [14]
#print(type(b))
#c = (9,)
#print(type(c))

# accessing elements:
# tuple uses index values to access an element.
#A = (10,20,30,40,)
#print(A[0])
#print(A[1])
#print(A[2])
#print(A[3])
#print(A[-1])
#print(A[-2])
#print(A[-3])
#print(A[-4])

#sclicing the tuple:
#a = (1,2,3,4,5,6)
#print(a[1:5])
#print(a[2:4])
#print(a[-1:])

# changing the values:
#A = (1,2,3,4,5,6,7,8)
#A[1] = 50
#print(A)

# append():
#A.append(50)
#print(A)

#length:
#A = (1,2,3,4,5,6,7)
#print(len(A))

# max:
#print(max(A))
#print(min(A))
#print(sum(A))

#concatnation :
#a = (2,3)
#b = (3,5)
#c = a + b
#print(c)

#repetition:
#a = (2,3,4)
#n = int(input("enter the n values :"))
#b = a * n
#print(b)

# searching and checking:
#z = (1,3,4,5,6,7,8)
#if 3 in z :
#    print("yes,num in the list")
#    print(3 not in z) 

#index():
#a = (1,2,3,4,5,6)
#print(a.index(1))

#count():
#b = (2,4,6,8,10,12,14)
#cnt = 0
#print(b.count(8))
#for i in range(10):
#    if i == 8:
#        cnt = cnt+1
#    print(cnt) 

# sort:
#st = (25,12,5,31,18,7)
#st.sort()
#st.reverse()

#copy:
#a1 = ("b","c","d","e",)
#a2 = a1.copy()

#Iterating tuple using for loop:
subjects = ("PEE","EC","HVPE","LAODE")
for subject in subjects:
    print("subjects=",subject)