import heapq

# 연산의 개수 N 입력 받기
N = int(input())

# 최소 힙 초기화
min_heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        # 배열에서 가장 작은 값을 출력하고 제거
        if min_heap:
            print(heapq.heappop(min_heap))#
        else:
            print(0)
    else:
        # 배열에 x 추가
        heapq.heappush(min_heap, x)