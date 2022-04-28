## for文で取得した数を加算
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total = 0
for all_day in month_day:
  total = total + all_day
print(total)

## sum関数を使って
day_sum = sum(month_day)
print(day_sum)
