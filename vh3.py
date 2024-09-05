#Categoria
idade = 5
categoria = 'indefinida'

#Definindo a Categoria 
if idade < 13:
    categoria = 'Criança'
elif idade >= 13 and idade < 18:
    categoria = 'Adolecente'
elif idade >= 18 and idade < 65:
    categoria = 'Adulto'
else:
    categoria = "idosa"   
print(f'Essa pessoa esta classificada como:{categoria}')