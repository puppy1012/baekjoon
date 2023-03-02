x=int(input())
result=0
for i in range(int(input())):
    a,b=map(int,input().split())
    result+=a*b
if result == x :
    print("Yes")
else:
    print("No")