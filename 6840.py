n=[]
for i in range(3):
    n.append(int(input()))
n.sort()
print(n[len(n)//2])