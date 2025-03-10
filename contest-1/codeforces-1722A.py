t = int(input())
for i in range(t):
    len = int(input())
    name = input()
    if len != 5:
       print('NO')
    else:
      res = 'NO'
      dic = {'T': 0, 'i': 0, 'm': 0, 'u': 0, 'r': 0}
      for j in name:
        if j in dic.keys() and dic[j] == 0:
          dic[j] = 1
      if 0 in dic.values():
         print('NO')
      else:
         print('YES')
         
        