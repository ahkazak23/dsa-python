import numpy as np
my_arr = np.array([[1,2,3,4,5],
                  [6,7,8,9,10],
                  [11,12,13,14,15],
                  [16,17,18,19,20]])
print(my_arr)
print('*'*10)
# Inserting
print("Inserting")
new_arr = np.insert(my_arr,0,[[1,2,3,4],[6,7,8,9]],axis=1)
print(new_arr)
print('*'*10)
new_arr = np.insert(my_arr,0,[[1,2,3,4,5],[6,7,8,9,10]],axis=0)
print(new_arr)
print('*'*10)
new_arr = np.append(my_arr,[[1,2,3,4,5],[6,7,8,9,10]],axis=0)
print(new_arr)
print('*'*10)

# Accessing
print('Accessing')
def accessElement(arr,row,col):
    if row<0 or row>=len(arr) or col<0 or col>=len(arr[0]):
        return 'Index out of range'
    return arr[row][col]

print(accessElement(my_arr,3,4))

# Traversing
print('Traversing')
def traverse(arr):
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            print(arr[row][col], end=' ')
    print()

traverse(new_arr)

# Searching
print('Searching')
def search(arr,target):
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col]==target:
                return f'Value {target} is located at index: [{row}][{col}] '
    return 'Value Not Found'

print(search(new_arr,440))

# Deleting
print('Deleting')
print(my_arr)
new_arr = np.delete(my_arr,3,axis=0)
print(new_arr)
