def factorial(n):
    result=1
    if(n>0):
        result=n*factorial(n-1)
    return result
n=int(input())
print(factorial(n))
"""
result1=1
for i in range(1,n+1):
    result1*=i
print(result1)
"""