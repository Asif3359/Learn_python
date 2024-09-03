import  numpy as np

def indexing():
    # a = np.arange(0,10,1)
    a = np.arange(10,1,-2)
    print(" A sequential array with a negative step:\n",a)
    # new_arr = a[np.array([0,1,2,3])]
    new_arr = a[np.array([3,1,2])]
    print(" Elements at these indices are:\n",new_arr)

def slicing():
    a = np.arange(20)
    print("\n Array is : \n",a)
    # a[artar:stop:step]
    print("\n a[-8:17:1] = ",a[8:17:1])
    # A 3 dimensional array.
    b = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [10, 11, 12]]])
    c = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [10, 11, 12]]])
    d = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [10, 11, 12]]])
    print("\n")
    print(b[...,0])
    print("\n")
    print(c[...,1])
    print("\n")
    print(d[...,2])



def print_hi():
    indexing()
    slicing()


if __name__ == '__main__':
    print_hi()

