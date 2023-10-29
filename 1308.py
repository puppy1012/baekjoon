def is_leap(year):
    return year %4==0 and (year %100 !=0 or year%400 ==0)
def days_from_start(year,month,day):
    month_days = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                  [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
    days = 365 * (year - 1) + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    days += sum(month_days[is_leap(year)][0:month]) + day
    return days

y1,m1,d1=map(int,input().split())
y2,m2,d2=map(int,input().split())

# 두 날짜를 일수로 변환하고, 두 일수의 차를 구합니다.
days = days_from_start(y2, m2, d2) - days_from_start(y1, m1, d1)

# 남은 일수가 365 * 1000일 이상이라면, "gg"를 출력합니다.
if days >= 365 * 1000:
    print("gg")
# 그렇지 않다면, "D-"를 출력하고 그 뒤에 남은 일수를 출력합니다.
else:
    print("D-" + str(days))