#print number in one line instead of one each in new line

'''
print 12345
instead of,
1
2
3
4
5
'''

def counter(n):
    for i in range(1, n+1):
        print(i,end='')

if __name__ == '__main__':
    n = int(input())
    counter(n)