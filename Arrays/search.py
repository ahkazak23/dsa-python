from create import my_array

def linear_search(arr,target): # T= O(N)  and S= O(1)
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return 'Not Found'

print(linear_search(my_array,97))