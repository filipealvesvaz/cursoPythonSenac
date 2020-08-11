def soma_imposto(taxa_imposto, custo):
    valor_final = custo + (taxa_imposto * custo)
    return valor_final

taxa = float(input("informe o valor da taxa: "))
custo_inicial = float(input("informe o valor do custo inicial: "))

print("O valor final do produto é ", soma_imposto(taxa, custo_inicial))