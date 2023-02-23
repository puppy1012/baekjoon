#print("".join(reversed(input())))
#문자열을 선언 후 input값을 reversed한 뒤 문자열에 .join시킨다
"""

"""
'''

n=list(input())
print(n[::-1])
#slicing은 원본 리스트의 순서를 변경하지않는다 새로운 리스트 리턴형식
n.reverse()
print(n)
#reverse함수는 리스트 형태에서만 사용 가능
#
'''
string = 'Hello, World!'
reversed_str = ''
for i in string:
    reversed_str = i + reversed_str
    print('reversed_str',reversed_str)
    print('i',i)

print(f'Original String: {string}')
print(f'Reversed String: {reversed_str}')