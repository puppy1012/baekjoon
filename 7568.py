length=int(input())
person=[]
for i in range (length):
    person_info=list(map(int,input().split()))
    person.append(person_info)

for i in range(length):
    number=1
    for j in range(0,length):
        if i !=j and person[i][0]<person[j][0] and person[i][1]<person[j][1]:
            number+=1
    print(number, end=" ")
