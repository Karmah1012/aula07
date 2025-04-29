nomes = ["Joao", "Carlos", "Maria", "Luiza", "Isabel"]
nomealuno = input("Qual o nome? ")
msg="nome não encontrado"
for x in range(len(nomes)):
    if nomealuno == nomes[x]:
        msg = f"Achei o {nomealuno}, na posição {x}"

print(msg)







