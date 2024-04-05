# Calculadora de despesas domésticas

print('Controle de despesas domésticas')

ana = float(input('Quanto Ana gastou? '))
bia = float(input('Quanto Bia gastou? '))
print()
total = ana + bia
print('Valor total dos gastos: R$ %s' % total)
media = total / 2
print('Média do valor gasto por pessoa: R$ %s' % media)
if ana < media:
    diferenca = media - ana
    print('Ana deve receber: R$ %s' % diferenca)
elif bia < media:
    diferenca = media - bia
    print('Bia deve receber: R$ %s' % diferenca)
else:
    print('Ana e Bia gastaram a mesma quantia!')