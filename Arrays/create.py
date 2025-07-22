import array
my_array1 = array.array('i')
my_array = array.array('i', [1, 2, 3, 4, 5, 6, 99])

import numpy as np
np_array = np.array([], dtype=int)
np_array1 = np.array([1, 2, 3, 4])

if __name__ == "__main__":
    print(my_array1)
    print(my_array)
    print(np_array)
    print(np_array1)
    print("create.py is running directly")
