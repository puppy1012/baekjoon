N = int(input())  # 단어의 개수 N을 입력받습니다.
count = 0  # 그룹 단어의 개수를 저장할 변수를 초기화합니다.

for _ in range(N):  # N개의 단어에 대해 반복합니다.
    word = input()  # 단어를 입력받습니다.
    if list(word) == sorted(word, key=word.find):  # 단어의 문자들이 처음 나타나는 순서대로 정렬된 경우, 그룹 단어입니다.
        count += 1  # 그룹 단어의 개수를 1 증가시킵니다.

print(count)  # 그룹 단어의 개수를 출력합니다.