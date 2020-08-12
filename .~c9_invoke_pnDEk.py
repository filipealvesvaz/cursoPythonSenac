# Valida formato do CPF
def validar_formato_cpf(cpf):
    # XXX.XXX.XXX-XX
    if cpf[3] != '.':
        return False
    elif cpf[7] != '.':
        return False
    elif cpf[11] != '-':
        return False
    return True
def validar_cpf(cpf):
     if validar_formato_cpf(cpf):
         cpf_limpo = cpf.replace('.','').replace('-','')
         contador = 10
         soma = 0
         for caractere in cpf_limpo:
             if contador > 1:
                soma += + int(caractere) * contador
                contador -= 1
        
         digito1 =  (soma * 10) % 11
         
         
        
         if digito1 != int(cpf_limpo[9]):
            return False
            
         contador = 11
         soma = 0
         for caractere in cpf_limpo:
            if contador > 1:
                soma += + int(caractere) * contador
                contador -= 1
                
         digito2 = (soma * 10) % 11
        
         if digito2 != int(cpf_limpo[10]):
            return False
     else:
        return False
        
     return True
    
# Realizando os testes
cpf = input('Digite um cpf válido: ')

if validar_cpf(cpf):
    print(f'{cpf}: válido')
else:
    print(f'{cpf}: inválido')
    