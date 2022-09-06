sw = 1
j = 0
n = 5
count = 0
dat = [5, 2, 7, 1, 4]

while sw == 1:
  sw = 0
  m = n - 1

  while j < m:
    if dat[m] <= dat[m-1]:
      m = m - 1

    elif dat[m] > dat[m-1]:
      w = dat[m]
      dat[m] = dat[m-1]
      dat[m-1] = w
      m = m - 1
      count += 1

      sw = 1


    j = j + 1

print(dat)
print(count)
