list=list(map(int,input().split()))
result=0
for i in range(len(list)):
    result+=list[i]
if result >=9:
    print("F")
else:
    print("S")