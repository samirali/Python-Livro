# coding: utf-8
print("calculos")
print("--------")
print("3 + 2 = ", 3+2)
print("complex(1,2) = ", complex(1,2))
print("3 + 4.2 = ", 3 + 4.2)
print("5 / 2 = ", 5/2)
print("5 // 2 = ", 5//2)
print("2 ** 8 = ", 2**8)

print("")
print("String")
print("--------")

print("""\
      
    Copa 2014
    Copa do Mundo 2014
    "Copa 2014"
    'Copa do Mundo 2014'
      
""")
print("Copa 2014")
print('Copa do Mundo')
print("Copa" "2014")
print("")

strExemplo = "Corinthians Campeão Mundial em 2000"

print(f"len({strExemplo}):", len(strExemplo))
print("pos[0]: ",strExemplo[0])
print("pos[2:7]: ",strExemplo[2:7])
print("pos[3:]: ",strExemplo[3:])
print("pos[:5]: ",strExemplo[:5])
print("")

print(f"'t' in {strExemplo}:", 't' in strExemplo)
print(f"'x' in {strExemplo}:", 'x' in strExemplo)
print(f"'{strExemplo}'+ ' uma vez!':", strExemplo + ' uma vez!' )
print("")

print("'s' * 5= ", 's' * 5)

print("'" + strExemplo + "'=> Substituindo anos abaixo:")
strExemplo = strExemplo.replace("em 2000", "em 2000 e 2012!")
print(strExemplo)
print()

print(f"Transforma em maiúsculo:" , strExemplo.capitalize())
print(f"Transforma em maiúsculo:" , strExemplo.capitalize())