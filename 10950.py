'''
n=int(input())
for i in range(n):
    print(sum(map(int,input().split())))

while True:
    try:
        print(sum(map(int,input().split())))
    except:
        break

while True:
    a,b,=map(int,input().split())
    if a == 0 and b==0:break
    print(a+b)
    '''
a,b=map(int,input().split())
print(a*b)