def gerador_de_cpf(str):
    import random
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))
# nesse primeiro bloco de função foi gerado o CPF

#Agora iremos fazer o calculo para descobrir o primeiro digito e o segundo digito /
#Conforme o calculo informado pelo Governo Brasileiro
    contagem_regressiva_1 = 10
    resultado_digito_1 = 0
# Será necessário iterar o cpf, e multiplicar pela contagem regressiva até o número 2
    for digito_1 in nove_digitos:
        resultado_digito_1 += int(digito_1)*contagem_regressiva_1
        contagem_regressiva_1 -= 1

# O próximo passo é multiplicar o resultado_digito_1 por 10, e fazer o % por 11
    primeiro_digito = (resultado_digito_1 *10) % 11
# O próximo passo é uma condição
# Se o primeiro digito for menor ou igual a 9, ele recebe o resultado 
# Se o primeiro digito for maior do que 9, ele automaticamente recebe 0
    primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

# ----------------- Segundo Digito ---------------------

# Será necessário também uma contagem_regressiva mas começando de 11.
# E adicionando o primeiro digito ao cpf de novo_digitos

    contagem_regressiva_2 = 11
    resultado_digito_2 = 0
    dez_digitos = nove_digitos + str(primeiro_digito)

    for digito_2 in dez_digitos:
        resultado_digito_2 += int(digito_2) * contagem_regressiva_2
        contagem_regressiva_2 -= 1

# A partir de agora é feito o mesmo calculo do primeiro digito

    segundo_digito = (resultado_digito_2 * 10) % 11
    segundo_digito = segundo_digito if segundo_digito <= 9 else 0

# Agora podemos concatenar os resultados

    cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
    
    print(f'CPF GERADO: {cpf_gerado}')


print(gerador_de_cpf(str))