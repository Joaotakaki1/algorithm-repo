eixos = input().split()
linhas = int(eixos[0])
colunas = int(eixos[1])
face = {'f': 0, 'a': 0, 'c': 0, 'e': 0}
matriz = []
count = 0
for i in range(linhas):
  linha = list(input())
  matriz.append(linha)
for i in range(linhas):
  for j in range(colunas):
    if i <= linhas - 2 and j <= colunas - 2:
      face = {'f': 0, 'a': 0, 'c': 0, 'e': 0}
      if matriz[i][j] in face.keys() and face[matriz[i][j]] == 0:
        face[matriz[i][j]] = 1
      if matriz[i+1][j] in face.keys() and face[matriz[i+1][j]] == 0:
        face[matriz[i+1][j]] = 1
      if matriz[i][j+1] in face.keys() and face[matriz[i][j+1]] == 0:
        face[matriz[i][j+1]] = 1
      if matriz[i+1][j+1] in face.keys() and face[matriz[i+1][j+1]] == 0:
        face[matriz[i+1][j+1]] = 1
      if 0 not in face.values():
        count += 1
print(count)