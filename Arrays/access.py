from create import my_array

def access_Element(arr,i): # T= O(1) and S= O(1)
    if i >= len(arr): # T= O(1)  and S= O(1)
        return print('Index out of Range') # T= O(1)
    else:
        return print(arr[i]) # T= O(1)

access_Element(my_array,5)