#Print Function

'''
Read an integer N.

Without using any string methods, try to print the following:
123...N

Note that "" represents the values in between.
'''

def counter(n):
    for i in range(1, n+1):
        print(i, end = '')

if __name__ == '__main__':
    n = int(input())
    counter(n)

