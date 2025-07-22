from create import my_array

def remove_Element(arr,target):
    for i in range(len(arr) - 1):
        if arr[i] ==  target:
            for j in range(i, len(arr) - 1):
                arr[j] = arr[j+1]
            arr.pop()
            return f"Element {target} removed. Updated array: {arr}"
    return 'Not Found'
print(remove_Element(my_array,1))