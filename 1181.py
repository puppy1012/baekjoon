"""
lista=[]

n=int(input())
for i in range(n):
    lista.append(input())
set_list=list(set(lista))
set_list.sort
set_list.sort(key=lambda x:len(x))
for i in set_list:
    print(i)
print(list)
"""
"""
for문으로 입력 받고
list값을 sort해서 분류하고
list문의 문자열의 길이가 같으면 ord값을 통해 비교연산해서 위치 배정하기


import sys

n = int(sys.stdin.readline())
# set 자료형을 통해 중복을 제거하고 정렬을 위해 list 자료형으로 감싸준다.
word = list(set(str(sys.stdin.readline().strip()) for _ in range(n)))
word.sort() # 오름차순 정렬
word.sort(key=lambda x: len(x)) # 단어의 길이를 기준으로 오름차순 정렬

# 반복문을 통해 단어를 출력
for i in word: print(i)
    
"""
n=int(input())
word_list=[]
for i in range(n):
    word_list.append(input())
#중복값set으로 제거,list형식으로 입력
set_world=list(set(word_list))
print("set_world",set_world)
sorted_word_list=[]
for i in set_world:
    sorted_word_list.append((len(i),i))
print("sorted_world_list",sorted_word_list)
result=sorted(sorted_word_list)
print("resut",result)


for len_word,word_list in result:
    print(len_word,word_list)
    print(word_list)