def isGoodArray(array, tam):
  if (sum(array)/tam) == 1:
    return True
  else:
    return False

t = int(input())
for i in range(t):
  len = int(input())
  array = input().split()
  arrayInt = [int(val) for val in array]
  soma = sum(arrayInt)
  m = 0
  if isGoodArray(arrayInt, len):
    m = 0
  else:
    if soma > len:
      m = soma - len
    else:
      m = 1
  print(m)