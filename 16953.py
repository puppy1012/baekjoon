import queue
def bfs(A, B):
    visited = set()
    que = queue.Queue() #큐 설정
    que.put((A, 1))  # 초기 상태와 연산 횟수를 큐에 넣습니다.
    while not que.empty(): #큐가 빌때까지 진행합니다
        cur, cnt = que.get()  # 현재 상태와 연산 횟수를 가져옵니다.
        if cur == B:  # 목표 상태에 도달한 경우 연산 횟수를 반환합니다.
            return cnt
        # 가능한 연산을 적용하여 새로운 상태를 큐에 넣습니다.
        visited.add(cur)
        # 현재상태에서 가능한 두가지 연산을 적용하여 새로운 상태인 next_cur를 생성합니다
        for next_cur in [cur * 2, int(str(cur) + '1')]:
            #새로운 상태가 목표 상태 B보다 작거나 같고, 아직 방문하지 않은 상태라면 큐에 넣습니다.
            if next_cur <= B and next_cur not in visited:
                que.put((next_cur, cnt + 1))
                visited.add(next_cur)
    return -1  # 목표 상태에 도달할 수 없는 경우 -1을 반환합니다.
# 입력을 받습니다.
A, B = map(int, input().split())
# 문제를 해결하고 결과를 출력합니다.
print(bfs(A, B))