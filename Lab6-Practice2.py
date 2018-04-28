alist = [[1,3,5],[2,4,6],[0,1,0]]
'''
1 3 5
2 4 6
0 1 0
'''

def printlist(alist):
    for i in range(0, len(alist)):
        for j in range(0,len(alist[0])):
            print(alist[i][j])

def printcolumn(alist, column):
    print('The column is: ')
    for i in range(0,len(alist)):
        print(alist[i][column])

def printrow(alist, row):
    print('The row is: ')
    for j in range(0,len(alist[row])):
        print(alist[row])
