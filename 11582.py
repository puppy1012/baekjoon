def custom_merge_sort(arr, k):
    if k == 1: #부분배열을 정렬합니다.
        return sorted(arr)

    if len(arr) == 1:#정렬하고자하는 배열의 길이가 1일시 정리가 필요X
        return arr

    #재귀적 정렬을 위한 처리과정
    mid = len(arr) // 2 #배열을 나누기위한 작업
    left = custom_merge_sort(arr[:mid], k // 2)
    right = custom_merge_sort(arr[mid:], k // 2)

    if k == 2: #정렬수행 회원이 2명일시 배열을 정렬후 반환
        return sorted(left + right)
    #재귀함수적 처리가 끝날시 결과값 반환
    return left + right


# 입력 받기
N = int(input("치킨집의 개수 N을 입력하세요: "))
arr = list(map(int, input("치킨집의 맛의 수치를 입력하세요: ").split()))
k = int(input("현재 정렬을 진행 중인 회원들의 수 k를 입력하세요: "))

result = custom_merge_sort(arr, N//k) #k명의 회원이 정렬을 수행하는지 확인하기위한 N//k
print(" ".join(map(str, result)))
