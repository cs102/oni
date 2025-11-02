def factorial(number):
    if number ==1:
        return 1 # base case

    #recursive case
    return number * factorial(number -1)

print(factorial(5))

def recursion(i):
    if i == 1:
        return i
    else:
        return recursion(i-1)

print(recursion(100))
