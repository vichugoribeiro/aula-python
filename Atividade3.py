def manipularString(texto):
    
    textoMaiuscuo = texto.upper()
    textoMinusculo = texto.lower()
    totaisCaracteres = len(texto)
    
    return (textoMaiuscuo, textoMinusculo, totaisCaracteres)


def main():
    palavra = input("Digite uma string para ser manipulada:")
    
    resultadoDoMaiusculo, resultadoDoMinusculo, resultadoTotaisCaracteres = manipularString(palavra)
    
    print(f'Sua palavra em maiusculo: {resultadoDoMaiusculo}')
    print(f'Sua palavra em maiusculo: {resultadoDoMinusculo}')
    print(f'Sua palavra em maiusculo: {resultadoTotaisCaracteres}')
    
main()