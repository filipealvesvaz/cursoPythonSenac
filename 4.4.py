letras = ["a", "b","c","d","e","f","g","h","i","j"]

consoantes = []

for letra in letras:
    #if "aeiou".find(letra) == -1:
    if letra not in "aeiou":
        consoantes.append(letra)
        
print(consoantes)