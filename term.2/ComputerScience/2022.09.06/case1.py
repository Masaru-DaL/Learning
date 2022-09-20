j = 0
n = 5
dat = [5, 2, 7, 1, 4]
count = 0

while j < n-1:
  m = n - 1

  while j < m:
    if dat[m-1] <= dat[m]:
      m = m - 1

    elif dat[m-1] > dat[m]:
      w = dat[m]
      dat[m] = dat[m-1]
      dat[m-1] = w
      m = m - 1
      count += 1

  j = j + 1

print(dat)
print(count)
