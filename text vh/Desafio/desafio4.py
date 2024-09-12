frutas = [" maçã", "banana", "laranja"]
print("Lista de Frutas:", frutas)
adicionarFruta = input("adicione uma fruta:")

frutas.append(adicionarFruta)
print ("Lista de Frutas Atualizada:",frutas)
removerFruta = input("remover uma fruta:")


if removerFruta in frutas:
    frutas.remove(removerFruta)
    print("Lista de Frutas Atualizada:",frutas)
else:
    print("Não foi encontrado na lista de frutas") 