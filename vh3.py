#Categoria
idade = int(input('qual é a sua idade?'))


#Definindo a Categoria 
def validarIdadePersona(idade):
    if idade < 0:
        return 'bebe'
    elif idade > 0 and idade < 13:
        return 'Criança'
    elif idade >= 13 and idade < 18:
        return 'Adolecente'
    elif idade >= 18 and idade < 65:
        return 'Adulto'
    elif idade > 65 and idade <= 105:
        return 'idosa'
    else:
        return "Acho que essa pessoa ja foi de arrasta"
categoria = validarIdadePersona (idade)
print(f'Essa pessoa esta classificada como:{categoria}')