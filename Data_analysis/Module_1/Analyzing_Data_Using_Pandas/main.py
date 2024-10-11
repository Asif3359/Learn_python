import numpy as np
import pandas as pd


def print_hi(name):
    ser = pd.Series()
    print(ser)
    # simple array
    data = np.array(['g', 'e', 'e', 'k', 's'])
    ser = pd.Series(data)
    print(ser)

    # Calling DataFrame constructor
    df = pd.DataFrame()
    print(df)

    # list of strings
    lst = ['Geeks', 'For', 'Geeks', 'is',
           'portal', 'for', 'Geeks']
    lst2 = ['Geeks', 'For', 'Geeks', 'is',
           'portal', 'for', 'Geeks']

    # Calling DataFrame constructor on list
    df = pd.DataFrame(lst)
    print(df)

    # # Reading the CSV file
    # df = pd.read_csv("Iris.csv")
    # # Printing top 5 rows
    # df.head()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
