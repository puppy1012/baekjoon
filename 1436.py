n=int(input())
number=0
i=1
while(True):
    if '666' in str(i): number+=1
    if number == n:
        print(i)
        exit()
    i+=1

# n = int(input())
# number = 0
# for i in range(1, 10000000):  # 충분히 큰 범위를 설정하여 모든 조건을 만족하는 수를 찾습니다.
#     if '666' in str(i):
#         number += 1
#     if number == n:
#         print(i)
#         break
