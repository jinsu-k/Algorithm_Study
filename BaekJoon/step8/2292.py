N = int(input())

count = 1
tmp_number = 1

while N >= tmp_number:
  if (N == tmp_number):
    break
  tmp_number = tmp_number + (count*6)
  count = count + 1

print(count)