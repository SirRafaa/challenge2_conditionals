# Desafio 2: Condicionais

preco = [100, 150, 250]

# Cliente 1
print('Bem vindo ao Hotel!\n') 
print('Valor dos Quartos:\n \nSimples = R$100,00 \nDuplo = R$150,00 \nLuxo = R$ 250,00\n')
nome = input('Nome do Cliente: ')
quarto = int(input('Escolha o Quarto (1 - Simples , 2 - Duplo, 3 - Luxo ) '))
dias = int(input('Dias de Estadia: '))
print('')
if quarto == 1:
    valor_total = preco[0] * dias
elif quarto == 2:
    valor_total = preco[1] * dias
elif quarto == 3:
    valor_total = preco[2] * dias
else:
    print('Opção de quarto inválida. ')
    valor_total = 0

# Cliente 2 

nome2 =  input('Nome do Cliente 2: ')
quarto2 = int(input('Escolha o Quarto (1 - Simples , 2 - Duplo, 3 - Luxo ) '))
dias2 = int(input('Dias de Estadia: '))
print('')
if quarto2 == 1:
    valor_total2 = preco[0] * dias2
elif quarto2 == 2:
    valor_total2 = preco[1] * dias2
elif quarto2 == 3:
    valor_total2 = preco[2] * dias2
else:
    print('Opção de Quarto Inválida. ')
    valor_total2 = 0

# Cliente 3

nome3 = input('Nome do Cliente 3: ')
quarto3 = int(input('Escolha o Quarto (1 - Simples , 2 - Duplo, 3 - Luxo ) '))
dias3 = int(input('Dias de Estadia: '))
print('')
if quarto3 == 1:
    valor_total3 = preco[0] * dias3
elif quarto3 == 2:
    valor_total3 = preco[1] * dias3
elif quarto3 == 3:
    valor_total3 = preco[2] * dias3
else:
    print('Opção de Quarto inválida. ')
    valor_total3 = 0

print('Valor total por cliente: \n')

if valor_total > 0:
    print(f"O valor total a ser pago por {nome} é: R${valor_total:.2f}")

if valor_total2 > 0:
    print(f"O valor total a ser pago por {nome2} é: R$ {valor_total2:.2f}")

if valor_total3 > 0:
    print(f"O Valor total a ser Pago por {nome3} é: R$ {valor_total3:.2f}")