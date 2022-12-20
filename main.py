import re
import sys

cpf = '399.338.030-42'
cpf_formated = re.sub(r'[^0-9]', '', cpf)
cpf_to_validate = cpf_formated[0:9]

if cpf_formated[0] * len(cpf_formated) == cpf_formated:
  print("\nThe informated CPF is invalid.")
  sys.exit()
  
print(cpf_formated, "\n")

i = 10

repeat = 0
while repeat != 2:
  repeat += 1
  
  soma = 0
  for digito in cpf_to_validate:

    operation = int(digito) * i
    
    soma += operation

    print(digito, "*", i, "\t= ", operation)
    
    i -= 1 

  print("\nSum of results = ", soma)
  
  product = (soma * 10) % 11

  print("(", soma, " * 10) % 11 = ", product, sep='')
  
  digit = 0 if product > 9 else product

  if repeat == 1:
    print("First digit = ", digit, "\n")
  else:
    print("Second digit = ", digit)
  
  cpf_to_validate += str(digit)

  i = 11
  
if cpf_to_validate == cpf_formated:
  print("\nThe informated CPF is valid.")

else:
  print("\nThe informated CPF is invalid.")
  
