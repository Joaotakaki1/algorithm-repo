t = int(input())
for i in range(t):
  nums = input().split()
  a = int(nums[0])
  b = int(nums[1])
  count = 0
  somador = 1
  lista = []
  if a > b:
    maxi = a
    mini = b
  else:
    maxi = b
    mini = a
  while mini < maxi:
    mini += somador
    lista.append(somador)
    somador += 1
    count += 1
  if (mini - maxi) % 2 == 0:
    print(count)
  else:
    while (mini - maxi) % 2 != 0:
      mini += somador
      somador += 1
      count += 1
    print(count)