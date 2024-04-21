# 작업의 개수 N과 작업 순서 정보의 개수 M 입력 받기
N, M = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

# 작업 순서 정보 입력 받기
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

# 오늘 반드시 끝내야 하는 작업 X 입력 받기
X = int(input())

# DFS 함수 정의
def dfs(start, visited):
    count = 0
    for neighbor in graph[start]:
        if neighbor not in visited:
            visited.add(neighbor)
            count += 1 + dfs(neighbor, visited)
    return count

# 방문한 노드 저장을 위한 집합 초기화
visited = set()

# 결과 출력
print(dfs(X, visited))