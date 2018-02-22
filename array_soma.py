import sys

def simpleArraySum(n, ar):
    # Complete this function
    total = 0
    for index in range(n):
        total = ar[index] + total
    return total


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)