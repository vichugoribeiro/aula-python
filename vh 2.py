#Variaveis
produtosValor = [100,200,300]
total = sum(produtosValor)
print(f'Total antes do desconto: {total}')
desconto = 0
#Desconto 10%
if total > 500: 
    desconto = total - (total * 0.1)
    resultado = total - desconto
    print(f'Desconto aplicado: {desconto}')
    print(f'Total com desconto: {resultado}')
else:
    diferenca = 500 - total
    print(f"Faltou {diferenca} para o desconto ser aplicado! Deseja incluir mais algum produto?")





