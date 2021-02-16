def sum(n):
    counter = 0
    for element in range(1, n + 1):
        counter += element
    return counter
print(sum(20))