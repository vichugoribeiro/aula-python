numero = int (input ("Entrada de N"))

def verificaEntrada (numero):

    if numero > 0:
        return "tu numero eres positivo"
    elif numero<0:
        return "se o numero negativo"
    else:
        return "se numero zero"
verificaEntrada (numero)
print(verificaEntrada(numero))

