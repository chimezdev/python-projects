# RECURSION
# A term in computer programming where a function invokes itself
# rewriting the fib() to make use of recursion:
def fib(n):
    if n < 1:
        return None #base case (termination condition)
    elif 1 <= n < 3:
        return 1 ##base case (termination condition)
    else:
        return fib(n-1) + fib(n-2)
        
print(fib(6))
# be careful bcos such a code can enter infinite loop, so watchout for condition that must stop it