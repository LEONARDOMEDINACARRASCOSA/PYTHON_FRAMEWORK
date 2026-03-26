# Peça o valor de um produto e:
produto =  float(input('Digite o valor do produto: '))


# Calcule um desconto de 10%.


desconto = produto * 0.10


# Mostre o valor final.


valor_prod = produto - desconto
print('Valor do produto R$', valor_prod)


# Verifique se o valor final é maior que 100.


print('Verifique se o valor final é maior que 100 - ', valor_prod > 100)


# Verifique se o produto ficou barato (menor que 50).


print('Verifique se o produto ficou barato (menor que 50) - ', valor_prod < 50)






a = ("500" + "500")
 
print(a)

("\n")

b = 500 + 500
print(b)



lista = []


lista.append(100)
lista.append(150)
lista.append(100)
lista.append(80)
lista.append(100)
lista.append(1400)
lista.append(1048520)
lista.append(1789500)



indice = lista.index(1789500)
lista.pop(indice)

print(lista)



saldo = [1500.0]


extrato = []


extrato.append(sum(saldo))


saque =  float(input('Digite o saque: '))


transacao =  sum(saldo) - saque


extrato.append(saque)


saldo = [transacao]


print('Saldo R$', saldo)


deposito =  float(input('Digite o Deposito R$: '))


extrato.append(deposito)


transacao =  sum(saldo) + deposito


saldo = [transacao]


print('Saldo R$', saldo)


print(extrato)

