import numpy as np


def simple_broadcast():
    macros = np.array([
        [0.8, 2.9, 3.9],
        [52.4, 23.6, 26.5],
        [55.2, 31.7, 23.9],
        [14.4, 11, 4.9]
    ])
    result = np.zeros_like(macros)
    # print(result)
    cal_per_macro = np.array([3, 3, 8])
    for i in range(macros.shape[0]):
        result[i, :] = macros[i, :] * cal_per_macro

    # result =  macros * cal_per_macro
    print(result)


def broadcast():
    v = np.array([12, 24, 36])
    w = np.array([45, 55])

    # print(v.shape)
    # print(w.shape)
    # print(np.reshape(v,(3,1)))
    print(np.reshape(v,(3,1))*w)

    x = np.array([[12, 22, 33], [45, 55, 66]])
    print(x + v)
    print((x.T + w).T)
    print(x + np.reshape(w, (2, 1)))
    print(x * 2)


def print_hi():
    # simple_broadcast()
    broadcast()



if __name__ == '__main__':
    print_hi()
