n=list(input())
list=[]
alphabat=['a','b','c','d','e','f','g','h','i','j',
          'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(26):list.append(-1)
for i in range(len(n)):
    for j in range(len(alphabat)):
        if alphabat[j]==n[i]:
            if list[j] != -1:
                continue
            else: list[j]=i
for i in range(len(list)):
    print(list[i],end=' ')
'''
word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위
for x in alphabet :
    print(word.find(chr(x)))

S = input()
abc ='abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in S:
        print(S.index(i), end= ' ')
    else:
        print( -1, end =' ')
'''