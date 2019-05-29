# Python Program to Find the Factorial of a Number

num = int(input('Enter the number: '))

# check if the number is negative

if num < 0:
    print('Sorry, factorial does not exist for negative number')

elif num == 0:
    print('Factorial of 0 is 1')

elif num > 0:
    factorial = 1
    for i in range(1, num+1):       # 1 x 2 x 3 .... , range will stop at one number before num, hence num+1
        factorial = factorial*i
    print(factorial)