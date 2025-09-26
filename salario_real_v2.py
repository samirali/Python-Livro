# coding: utf-8

salario = int(input('Salário?'))
imposto = float(27.5)

while imposto > 0.:
    imposto = float(input('Imposto ou (0) para sair: '))
    print("Valor real: {}". format(salario-(salario*(imposto*0.01))))

if not imposto:
    imposto = 27.5
else:
    imposto = float(imposto)
        
print("Valor real: {}". format(salario-(salario*(imposto*0.01))))