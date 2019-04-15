# Loops inside loops

'''
Can the body of a loop have another loop
within it? Yes! This is called a nested loop.
It’s like Russian dolls, where each doll fits
inside a larger doll. In a nested loop, an
inner loop runs inside an outer loop.
'''

for hooray_counter in range(1, 4):
    for hip_counter in range(1, 3):
        print('Hip')
    print('Hooray!')

'''
How it works
The whole of the inner for loop
is inside the body of the outer
for loop. Each time we do one
repeat of the outer loop, we
have to do two repeats of the
inner loop. This means the body
of the outer loop is run three
times in total, but the body of
the inner loop is run six times.
'''