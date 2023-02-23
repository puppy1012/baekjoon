n=int(input())
m=list(map(int,input().split()))
target=int(input())
result=0
for i in range (n):
    if m[i]==target:
        result+=1
print(result)