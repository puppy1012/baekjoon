# #값을 받아오는부분
# word= list(input())
# answer=[]
# tmp=[]
# #변환가능한 값 변환
# for i in range(1,len(word)-1):
#     for j in range(i+1,len(word)):
#         a=word[:i]
#         b=word[i:j]
#         c=word[j:]
#         a.reverse()
#         b.reverse()
#         c.reverse()
#         tmp.append(a+b+c)
# #sorted를 사용하기위해 리스트가 아닌 문자열로 변환하는 작업
# for a in tmp :
#     answer.append(''.join(a))
#
# #원하는 최종결과물 제일 첫번째 문자열출력
# print(sorted(answer)[0])
#
#
#
word=list(input())
answer=[]
tmp=[]

for i in range(1,len(word)-1):
    for j in range(i+1,len(word)):
        a=word[:i]
        b=word[i:j]
        c=word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        tmp.append(a+b+c)
for a in tmp:
    answer.append(''.join(a))
print(sorted(answer)[0])