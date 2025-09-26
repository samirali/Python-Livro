# coding: utf-8

salario = int(input('Salário?'))
# imposto = float(input('Imposto em % (ex: 27.5)?'))
imposto = input('Imposto em % (ex: 27.5)?')

if not imposto:
    imposto = 27.5
else:
    imposto = float(imposto)
        
print("Valor real: {}". format(salario-(salario*(imposto*0.01))))