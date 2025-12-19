cpf_enviado_usuario = input('Digite seu cpf: ')
nove_digitos = cpf_enviado_usuario[:9]#pega os nove primeiros digitos do cpf
contador_regressivo = 10

resultado = 0
for digito_1 in nove_digitos: # resulta no digito 1
    resultado += int(digito_1) * contador_regressivo
    contador_regressivo -= 1
digito_1 = (resultado * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

dez_digitos = nove_digitos + str(digito_1)
# dez_digitos = cpf[:10]
resultado_2 = 0
contador_regressivo_2 = 11
for digito_2 in dez_digitos:#resulta no digito 2
    resultado_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)

cpf_gerado_pelo_calculo = (f'{nove_digitos}{digito_1}{digito_2}')

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:#verifica se o cpf é valido ou não
    print(f'O CPF {cpf_enviado_usuario} é valido.')
else:
    print(f'O CPF {cpf_enviado_usuario} é invalido')