'''
Read an integer N. For all non-negative integers i < N, print i^2.
'''

if __name__ == '__main__':
    n = int(input())
    x = 1
    if 1 <= n <= 20:
        #Using for loop
        #for x in range(0, n):
        #print(x**2)
        #Using while loop
        while x < n:
            print(x**2)
            x = x+1
