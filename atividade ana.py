#
dia = int (input("Qual o dia de hoje?"))
pedidoPizza = int(input("Quantas pizzas comprou?"))
pedidoBebida = int(input("Quantas bebidas comprou?"))
pedidoBolo = int(input("Quantos bolos comprou?"))
pedidoDoce = int(input("comprou quantos doces?"))

#Declarando Variaveis 
diaFesta = 26
pedidoMinimoPizza = 10
pedidoMinimoBebida = 12
pedidoMinimoBolo = 5
PedidoMinimoDoce = 600

if diaFesta == dia:
    print("Ana esta fazendo as compras no dia da festa!")
else:
    print("Ana fazendo compra adianta")
    
if(pedidoMinimoPizza >= pedidoPizza):
    if(pedidoMinimoPizza == pedidoPizza):
        print("Ana comprou o minimo permitido de pizzas")
    print("Ana não comprou pizzas suficiente")
    
if (pedidoMinimoBebida < pedidoBebida):
    print("Ana comprou o maximo permitido de bebidas ")
    
if(pedidoBolo > pedidoMinimoBolo):
    print("Ana comprou bolo a mais")