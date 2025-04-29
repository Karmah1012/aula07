A=[5,6,7,8,9]
multi = [""] *5
num = int(input("Digite um número: "))
for x in range(len(A)):
    multi[x]= num*A[x]
print(multi)

