idade = 25
categoria = 'indefinida'
if idade < 13:
    categoria = 'Criança'
elif idade >= 13 and idade < 18:
    categoria = 'Adolecente'
    
print('A pessoa é classificada como:', categoria)