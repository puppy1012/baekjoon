student=[i for i in range(1,31)]
for _ in range(28):
    i= int(input())
    student.remove(i)
print(student)
print(min(student))
print(max(student))

