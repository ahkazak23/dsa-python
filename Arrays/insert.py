import array

my_array = array.array('i',[1,2,3]) # O(n)
print(my_array)

# insert at the beginning   T= O(N)  and S= O(1)
my_array.insert(0,7)
print(my_array)

# insert to any place  T= O(N)  and S= O(1)
my_array.insert(2,7)
print(my_array)

# insert at the ending  T= O(N)  and S= O(1) 
my_array.insert(len(my_array),7)
print(my_array)

