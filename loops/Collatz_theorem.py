# In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis 
# (it still remains unproven) which can be described in the following way:

# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, skip to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.

# Of course, it's an extremely complex task to use a computer in order to prove the 
# hypothesis for any natural number (it may even require artificial intelligence), 
# but you can use Python to check some individual numbers. Maybe you'll even find 
# the one which would disprove the hypothesis.

# Write a program which reads one natural number and executes the above steps as 
# long as c0 remains different from 1. We also want you to count the steps 
# needed to achieve the goal. Your code should output all the intermediate values of c0, too.

# Hint: the most important part of the problem is how to transform Collatz's 
# idea into a while loop - this is the key to success.

#SOLUTIONS
#my soln
c0 = int(input("Enter a number: "))
counter = 0
if c0 < 1:
    print("Sorry your number has to be a positive non-zero integer to evaluate Collatz hypothesis")
else:
    while c0 >= 1:
        if c0%2 == 0:
            c0 /= 2
        else:
            c0 = (3 * c0) + 1
        counter += 1
        if c0 != 1:
            print("Value of c0: ", c0)
            continue
        else:
            break
        
    print("Final value of c0: ", c0)    
print("Number of iterations: ", counter)

#soln from stackoverflow
n = int(input("Enter a strictly positive integer: "))
steps = 0
while n != 1:
    if n % 2 == 0:
        n = n / 2
    elif n % 2 == 1: 
        n = (3*n) + 1
    steps += 1
    print(int(n))

print (steps)