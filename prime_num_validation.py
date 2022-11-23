# My code 
def is_prime(num):
    if num < 2:
        return False
    elif num == 2 | num == 3:
        return True
    else:
        for j in range(2, num):  # num bcos d loop will stop at j b4 num and we want to divide num with each j
            # starting j 4rm 2 and not 1 bcos anything divided by 1 is still dsame
            if num % j == 0:
                return False
            else:
                return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()  # NOT CORRECT. REWRITE THIS FUNCTION

# soln
def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()