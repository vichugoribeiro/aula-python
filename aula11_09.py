#Metodo de Busca Ler 
with open("text vh/exemplo.txt", 'r', encoding="utf-8") as arquivo :
    conteudo = arquivo.read()
    print(conteudo)
    
    # Metodo de Busca Escrever
with open("text vh/exemplo2.txt", 'w', encoding="utf-8") as arquivo :
    arquivo.write("Olá Mundo!")
    
    #Metodo de Acrescentar 
    with open("text vh/exemplo.txt", "a", encoding="utf-8") as arquivo :
        arquivo.write("\nTexto adicionalol")