t = int(input())
for i in range(t):
  cols = int(input())
  alturas = list(map(int, input().split()))
  maiorAlt = max(alturas)
  res = True
  for i in range(cols):
    if (alturas[i] - maiorAlt)%2 != 0:
      res = False
  if res:
    print('YES')
  else:
    print('NO')