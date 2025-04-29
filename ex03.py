#cadastra notas
#calcula media
#notas acima da media
notas=[""]*5
soma = 0
z = 0
for x in range(len(notas)):
    notas[x] = float(input("Digite as notas dele: "))
print(f"As notas são: {notas}")
for y in range(len(notas)):
    soma = soma + notas[y]
media = soma / 5
for j in range(len(notas)):
    if notas[j] >= media:
        z += 1
print(f"A média, é: {media}")

print(f"Alunos acima da média da sala: {z} ")







