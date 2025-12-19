import random
import sys

#criador de cpf
for _ in range(50):#a quantidade de cpf's que será gerado
    nove_digitos = '' 
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))#gera nove digitos aleatorios e os coloca como a variavel

    contador_regressivo = 10#é como será feita a contagem regressiva

    resultado = 0
    for digito in nove_digitos:#faz a conta do digito 1
        resultado += int(digito) * contador_regressivo
        contador_regressivo -= 1
    digito_1 = (resultado * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    
    dez_digitos = nove_digitos + str(digito_1)
    # dez_digitos = cpf[:10]
    resultado_2 = 0
    contador_regressivo_2 = 11
    for digito in dez_digitos:#faz a conta do digito 2
        resultado_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    
    cpf_gerado = (f'{nove_digitos}{digito_1}{digito_2}')
    print(cpf_gerado)