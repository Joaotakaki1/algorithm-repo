t = int(input())
for i in range(t):
  len = int(input())
  array = input()
  aux = 0
  m = 0
  if len == 1:
    if array == '0':
      m = 1
  else:
    array = array.split()
    for j in array:
      if j == '0':
        aux += 1
      else:
        if aux > m:
          m = aux
        aux = 0
    if aux > m:
      m = aux
  print(m)