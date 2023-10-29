"""
당신에게 3x3 크기의 보드가 주어진다. 각각의 칸은 처음에 흰색 혹은 검은색이다.
만약 당신이 어떤 칸을 클릭한다면 당신이 클릭한 칸과 그 칸에 인접한 동서남북 네 칸이 (존재한다면) 검은색에서 흰색으로,
혹은 흰색에서 검은색으로 변할 것이다.
당신은 모든 칸이 흰색인 3x3 보드를 입력으로 주어지는 보드의 형태로 바꾸려고 한다. 보드를 회전시킬수는 없다.
"""

#3*3이라는 공간이 주어지며 하나의 칸을 누르면 십자가 형태로 색깔이 반전된다.
#흰색기준으로 성립된 공간을 주어진 보드형태로 바꾸어야하며 회전은 안된다.
#구현을 위해 반전 함수, 클릭시 십자가 형태로 인접 칸의 값을 반전하는 함수

# 셀의 색을 뒤집는 함수
# def flip(board, x, y):
#     # 전달된 좌표가 보드값 안에 있을시 작동
#     if x >= 0 and x < 3 and y >= 0 and y < 3:
#         # 색을 뒤집음: 1은 0으로, 0은 1로
#         board[x][y] = 1 - board[x][y]
#
#
# # (x, y) 위치에서 클릭을 적용하는 함수
# def click(board, x, y):
#     # 클릭한 셀과 그 주변 셀의 색을 뒤집음
#     flip(board, x, y)
#     flip(board, x + 1, y)
#     flip(board, x - 1, y)
#     flip(board, x, y + 1)
#     flip(board, x, y - 1)
#
#
# # 보드가 모두 흰색인지 확인하는 함수
# def is_all_white(board):
#     # 보드의 각 셀을 순회
#     for i in range(3):
#         for j in range(3):
#             # 어떤 셀이 검은색(1)이면 False 반환
#             if board[i][j] == 1:
#                 return False
#     # 모든 셀이 흰색(0)이면 True 반환
#     return True
#
#
# # 메인 함수
# def main():
#     T = int(input())  # 테스트 케이스의 수를 입력받음
#     for _ in range(T):  # 각 테스트 케이스에 대해 반복
#         # 초기 보드 설정을 입력받아 리스트로 표현
#         board = []
#         for _ in range(3):
#             row = list(map(lambda x: 1 if x == '*' else 0, input().strip()))
#             board.append(row)
#
#         ans = float('inf')  # 최소 클릭 횟수를 저장할 변수, 초기값은 무한대
#
#         # 가능한 모든 클릭 조합(총 2^9 = 512 가지)을 시도
#         for mask in range(1 << 9):
#             # 클릭을 적용할 임시 보드를 생성
#             temp_board = [row.copy() for row in board]
#             clicks = 0  # 이 조합에 대한 클릭 횟수를 저장할 변수
#
#             # 3x3 보드의 각 셀에 대해 클릭할지 말지 결정
#             for i in range(3):
#                 for j in range(3):
#                     # 비트마스크를 사용해 해당 셀을 클릭할지 말지 결정
#                     if mask & (1 << (i * 3 + j)):
#                         click(temp_board, i, j)  # 클릭 적용
#                         clicks += 1  # 클릭 횟수 증가
#
#             # 모든 클릭을 적용한 후 보드가 모두 흰색인지 확인
#             if is_all_white(temp_board):
#                 ans = min(ans, clicks)  # 필요하다면 최소 클릭 횟수 업데이트
#
#         print(ans)  # 이 테스트 케이스에 대한 최소 클릭 횟수 출력
#
#
# # 프로그램의 시작점
# if __name__ == "__main__":
#     main()
# 주어진 보드가 모두 흰색인지 확인하는 함수
# 주어진 보드가 모두 흰색인지 확인하는 함수
def is_all_white(board):
    for x in board:
        for y in row:
            if y == 1:
                return False
    return True


# (x, y) 위치와 그 주변의 칸을 클릭하여 색을 뒤집는 함수
def click(board, x, y):
    dx = [-1, 1, 0, 0, 0]
    dy = [0, 0, -1, 1, 0]
    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 3 and 0 <= ny < 3:
            board[nx][ny] = 1 - board[nx][ny]


# 재귀 함수로 문제를 해결하는 함수
def solve(board, x, y, clicks):
    # 모든 칸을 확인했으면 결과를 반환
    if x == 3:
        if is_all_white(board):
            return clicks
        else:
            return float('inf')

    # 다음 칸의 좌표 계산
    next_x, next_y = x, y + 1
    if next_y == 3:
        next_x, next_y = x + 1, 0

    # 현재 칸을 클릭하지 않는 경우
    ans1 = solve(board, next_x, next_y, clicks)

    # 현재 칸을 클릭하는 경우
    click(board, x, y)
    ans2 = solve(board, next_x, next_y, clicks + 1)

    # 원상태로 복구
    click(board, x, y)

    # 두 경우 중 최소 클릭 횟수를 반환
    return min(ans1, ans2)


# 테스트 케이스의 수를 입력받음
T = int(input())

for _ in range(T):
    # 초기 보드 설정
    board = []
    for _ in range(3):
        row=[]
        for x in input().strip():
            if x == '*':
                row.append(1)
            else:
                row.append(0)
        board.append(row)

    # 문제 해결
    ans = solve(board, 0, 0, 0)
    print(ans)