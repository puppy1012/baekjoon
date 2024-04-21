while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        print(count)
        break  # 입력이 0 0이면 종료

    cds_n = sorted([int(input()) for _ in range(N)])  # 상근이가 가진 CD, 정렬 추가
    cds_m = sorted([int(input()) for _ in range(M)])  # 선영이가 가진 CD, 정렬 추가

    count = 0  # 공통으로 가진 CD의 개수
    index_n, index_m = 0, 0  # 각 리스트를 탐색할 인덱스

    while index_n < N and index_m < M:
        if cds_n[index_n] == cds_m[index_m]:
            count += 1  # 공통으로 가진 CD 발견
            index_n += 1
            index_m += 1
        elif cds_n[index_n] < cds_m[index_m]:
            index_n += 1  # 상근이의 다음 CD로 이동
        else:
            index_m += 1  # 선영이의 다음 CD로 이동


