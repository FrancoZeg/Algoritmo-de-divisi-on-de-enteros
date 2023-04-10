A = 0
Q = 7
M = 3
Count = int.bit_length(M)
CountA = int.bit_length(A)
CountQ = int.bit_length(Q)

def decimal_a_binario(numero_decimal):
    numero_binario = 0
    multiplicador = 1

    while numero_decimal != 0:
        numero_binario = numero_binario + numero_decimal % 2 * multiplicador
        numero_decimal //= 2
        multiplicador *= 10

    return numero_binario

def countdef (x):
  count = 0
  while x > 0:
    count += 4
    x =- 4
  return count

A = decimal_a_binario(A)
Q = decimal_a_binario(Q)
M = decimal_a_binario(M)
Count = countdef(Count)
CountSec = countdef(CountQ)

def det (x):
  tmp = 0
  if (x == 0):
    tmp = 1
  else:
    tmp = 1
    while (x >= 10):
      tmp += 1
      x = x//10
  return tmp

while Count != 0:
  A = A - M
  if A < 0:
    Q = (Q*10) + 0
    A = A + M
    A = (A*10) + 1
  else:
    Q = (Q*10) + 1
  if (det(Q) != CountSec):
    Q -= (Q//10**(det(Q) - 1)) * (10**(det(Q)-1))
  Count -= 1

print ("EL RESIDUO ES:", A, "EL COCIENTE ES:", Q)
