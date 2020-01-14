import keyword

[print(var, end=', ') if i % 5 != 0 else print(var, end='\n') for i, var in
 zip(range(1, len(keyword.kwlist) + 1), keyword.kwlist)]
