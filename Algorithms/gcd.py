def gcd(a,b):
    while (b != 0):
        t = a       # We are putting a in t because we need it to calculate b and a value is going to change in next line
        a = b       # because remainder is not zero to need to calculate further
        b = t % b   # calculating new b value using a which is in t
                    # loop will stop when b == 0
    return a        # function is returning value i.e. a's value

print(gcd(12,8))

'''
Explanation:

a and b
a > b
divide a by b
r == 0 then stop GCD is b

otherwise set a to b & b to r
repeat step 1 until r is 0

a 	b 	r
20 	8 	4
8 	4 	0
'''