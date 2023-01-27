#기준값 리스트
Standard=[1,1,2,2,2,8]
#값 입력받기
N=list(map(int,input().split()))
#입력받은 리스트의길이만큼 반복하면서 기준값-입력값을 출력,공란하나 출력
for i in range(len(N)):
    print(Standard[i]-N[i],end=' ')
"""
n=3
m=3
d=[0 for _ in range(n)]
print(d)

"""
