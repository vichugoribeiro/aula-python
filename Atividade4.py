def adicionarContato(listaContato, pessoa):
    listaContato.append(pessoa)
    
def main():
    contatos = []
    
    print(f'Minha lista de contatos atualmente tem {len (contatos)} ')
    
    pessoaAlice = {"nome":"Alice", "Telefone":"123-456-789"}
    pessoaBob = {"nome":"Bob", "Telefone":"098-765-432"}
    
    contatos.append(pessoaAlice)
    print(f'Minha lista de contatos {len(contatos)}')
    print(f'Lista de contatos atualizados:{contatos}')
    
    contatos.append(pessoaBob)
    print(f'Minha lista de contatos {len(contatos)}')
    print(f'Lista de contatos atualizados:{contatos}')
    
main()