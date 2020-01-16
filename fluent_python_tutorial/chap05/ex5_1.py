def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print("factorial(5) = %s" % factorial(5))
print(factorial.__doc__, type(factorial), sep='\n')

help(factorial)


fact = factorial
print(fact)
print(fact(5))
print(map(factorial, range(11)))

map_list = list(map(factorial, range(11)))
print(map_list)