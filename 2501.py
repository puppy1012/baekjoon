# 입력을 받습니다. N은 자연수, K는 N의 약수 중에서 K번째로 작은 수를 찾을 것입니다.
N, K = map(int, input().split())

# 약수를 저장할 리스트를 초기화합니다.
divisors = []

# N의 약수를 찾습니다. i가 1부터 N까지 반복하면서 N을 i로 나눴을 때 나머지가 0이면 i는 N의 약수입니다.
for i in range(1, N + 1):
    if N % i == 0:
        divisors.append(i)

# K번째 약수를 출력합니다. 만약 K번째 약수가 없다면 0을 출력합니다.
if len(divisors) < K:
    print(0)
else:
    print(divisors[K - 1])