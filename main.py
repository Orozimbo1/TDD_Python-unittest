from calculadora import soma

print(soma(10, 20))
print(soma(-10, 20))

try:
    print(soma('10', 20))
except AssertionError as e:
    print(f'Conta invalida: {e}')

print('oi', soma(25, 25))