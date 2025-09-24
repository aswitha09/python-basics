# arrays in python:
# creating an array:
import array as arr
numbers = arr.array('i',[1,2,3,4,5])
print(type(numbers))
print(numbers)

# accessing array elements:
print(numbers[0])
print(numbers[3])
print(numbers[-1])

# adding an element in array:
#append
numbers.append(7)
print(numbers)
#insert
numbers.insert(2,6)
print(numbers)
#extending:
numbers.extend([0,9])
print(numbers)

#deleting an element:
#remove
numbers.remove(0)
print(numbers)
#pop
numbers.pop(4)
print(numbers)

#updating an element:
numbers[0] = 10
print(numbers)