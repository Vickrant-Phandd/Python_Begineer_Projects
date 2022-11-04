#Find Missing Number using Python

def findmissingnumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output

n = [2,3,4,6,8,9,11]
print(findmissingnumbers(n))
