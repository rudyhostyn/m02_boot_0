def sumatodos(limitTo):
    resultado = 0
    for i in range (1,limitTo+1):
        resultado += i
    return resultado
    
def sumatodosloscuadrados(limitTo):
    resultado = 0
    for i in range (1, limitTo+1):
        resultado += i*i
    return resultado

print(sumatodos(100))
print(sumatodosloscuadrados(4))