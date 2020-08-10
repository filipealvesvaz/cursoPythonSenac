vet=[]
for n in range(1,11):
    num = int(input(f"informe os numeros {n}"))
    vet.append(num)
    vet.sort()
    vet.reverse()
print(vet)