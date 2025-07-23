# 1. Create an array and Traverse
from array import *
print("Step 1")
my_arr = array('i', [1, 2, 3, 4, 5])

for i in my_arr:
    print(i)

# 2. Access individual elements through indexes
print("Step 2")
print(my_arr[3])

# 3. Append any value to the array using append() method
print("Step 3")
my_arr.append(6)
print(my_arr)

# 4. Insert value in an array using insert method()
print("Step 4")
my_arr.insert(2, 7)
print(my_arr)

# 5. Extend python array using extend() method
print("Step 5")
my_arr1 = array('i', [11, 12, 13, 14, 15])
my_arr.extend(my_arr1)
print(my_arr)

# 6. Add items from list into array using fromlist() method
print("Step 6")
tmp_List = [20, 30, 40, 50]
my_arr.fromlist(tmp_List)
print(my_arr)

# 7. Remove any array element using remove() method
print("Step 7")
my_arr.remove(11)
print(my_arr)

# 8. Remove last array element using pop() method
print("Step 8")
my_arr.pop()
print(my_arr)

# 9. Fetch any element's  index using index() method
print("Step 9")
print(my_arr.index(12))

#10 Reverse a python array using reverse() method
print("Step 10")
my_arr.reverse()
print(my_arr)

# 11. Get array buffer information using buffer_info() method
print("Step 11")
print(my_arr.buffer_info())

# 12. Check for number of occurrences of an element using count() method
print("Step 12")
print(my_arr.count(1))

# 13. Convert array to string using tostring() method and Append a string to char array using fromstring() method
print("Step 13")
strTemp = my_arr.tobytes()
ints = array('i')
ints.frombytes(strTemp)
print(ints)

# 14. Convert array to python list using tolist() method
print("Step 14")
print(ints.tolist())

# 15. Slice Elements from an array
print("Step 15")
print(my_arr)
print(my_arr[::-1])
