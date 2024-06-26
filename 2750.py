N = int(input()) #N을 입력받습니다.

# N개의 수를 입력받아 리스트에 저장합니다.
numbers = [int(input()) for _ in range(N)]

# 버블 정렬 알고리즘을 사용하여 리스트를 오름차순으로 정렬합니다.
for i in range(N):
    for j in range(0, N-i-1): #정렬 이후 마지막 i개의 원소가 이미 정렬되어있기에 마지막 원소를 무시합니다.
        # 인접한 두 원소를 비교하여 필요하면 교환합니다.
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# 정렬된 리스트를 출력합니다.
for num in numbers:
    print(num)