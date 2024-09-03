import numpy as np

def numpyEmpty():
    print("Numpy Empty:\n")
    b = np.empty(2, dtype=int)
    print("Matrix b : \n", b)
    a = np.empty([2, 2], dtype=int)
    print("Matrix a : \n", a)
    c = np.empty([3, 3])
    print("Matrix : \n", c)


def numpyZeros():
    print("Numpy Zeros:\n")
    za = np.zeros(2,dtype=int)
    print("Matrix za :\n",za)
    zb = np.zeros([2,2],dtype=int)
    print("Matrix zb :\n",zb)
    zc = np.zeros([3,3])
    print("Matrix zc :\n",zc)

def addition():
    a = np.array([5, 72, 13, 100])
    b = np.array([2, 5, 10, 30])
    # Performing addition using arithmetic operator
    add_ans = a + b
    print(add_ans)
    # Performing addition using numpy function
    add_ans = np.add(a, b)
    print(add_ans)
    # The same functions and operations can be used for
    # multiple matrices
    c = np.array([1, 2, 3, 4])
    add_ans_with_c = a + b + c
    print(add_ans_with_c)
    add_ans_with_c = np.add(a, b, c)
    print(add_ans_with_c)

def subtraction():
    a = np.array([5, 72, 13, 100])
    b = np.array([2, 5, 10, 30])
    # Performing subtraction using arithmetic operator
    sub_ans = a - b
    print(sub_ans)
    # Performing subtraction using numpy function
    sub_ans = np.subtract(a, b)
    print(sub_ans)
    # The same functions and operations can be used for
    # multiple matrices
    c = np.array([1, 2, 3, 4])
    sub_ans_with_c = a - b - c
    print(sub_ans_with_c)
    sub_ans_with_c = np.subtract(a, b, c)
    print(sub_ans_with_c)

def multiplication():
    a = np.array([5,72,13,100])
    b = np.array([2,5,10,30])
    # Performing multiplication using arithmetic
    # operator
    mul_ans = a*b
    print(mul_ans)
    # Performing multiplication using numpy function
    mul_ans = np.multiply(a,b)
    print(mul_ans)

def division():
    a = np.array([5,72,13,100])
    b = np.array([2,3,10,30])
    # Performing division using arithmetic operators
    div_ans = a/b
    print(div_ans)
    # Performing division using numpy functions
    div_ans = np.divide(a,b)
    print(div_ans)


def operationNumpyArray():
    addition()
    subtraction()
    multiplication()
    division()


def print_hi():
    numpyEmpty()
    numpyZeros()
    operationNumpyArray()



if __name__ == '__main__':
    print_hi()

