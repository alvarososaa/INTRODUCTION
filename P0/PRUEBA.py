def sum(n):
    counter = 0
    for element in range(1, n + 1):
        counter += element
    return counter
print(sum(20))
def fibbonaci(n):
    lista = [1,1]
    for element in range(2, n + 1):
        x = lista[-1] + lista[-2]
        lista.append(x)
    return lista
k = fibbonaci(21)
print(k)



