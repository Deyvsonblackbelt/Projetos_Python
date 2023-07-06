# sistema de ifood
# cárdapio, burguers clássicos[cheese burguer, cheese salada,cheese bacon], burgers premium[palermo, london, kington]

cheese_burguer = [" pão brioche 170g, burguer na brasa, quiejo mussarela e maionese artesanal"]
cheese_salada = ["pão brioche, 170g burguer na brasa, quiejo mussarela, alface americana, tomates e maionese da casa"]
cheese_bacon = ["pão brioche, 170g burguer na brasa, quejo cheddar, maionese da casa e bacons"]

palermo = ["pão brioche, 170g burguer na brasa, quiejo mussarela, queijo gorgonzola,geleia de tomate artesanal,bacons e maionese artesanal"]
london = ["pão australiano, 170g burguer na brasa, fatias de queijo cheddar, cebolas caramelizadas, fatias de bacon, e maionese da casa "]
kingston = ["pão brioche, 170g burguer na brasa, fatias de lombo canadense, cebolas caramelizadas, cebolas empanadas e maionese da casa"]


cardapiop = {"cheese burguer":'16$',"cheese salada":'18$', "cheese bacon":'19$'}
cardapio = {"cheese burguer":16,"cheese salada":18, "cheese bacon":19}
cardapio_premiun_p = {"palermo":'27$', "london":'23$', "kingston":'24$'}
cardapio_premiun = {"palermo":27, "london":23, "kingston":24}

while True:
    
  print("0 - cárdapio simples | 1 - cárdapio premiun | 2 - comprar")
  opcoes = int(input("faça a sua escolha!"  ))

  def caradapio_simples():
    if opcoes == 0:
      print(cardapiop)
      print("ai está as opções dos hamburguers e seus preços! ")
      detalhes = str(input("para saber detalhes dos humburguers digite sim!  "))
      if detalhes == "sim":
        print("")
        print("\n CHEESE BURGUER",cheese_burguer , "\n CHEESE SALADA", cheese_salada ,"\n CHEESE BACON", cheese_bacon )
      else :
        print("finalize seu pedido em \'comprar'\ ") 
  caradapio_simples()      

  def cardapio_premiun(): 
    if opcoes == 1:
      print(cardapio_premiun)
      print("ai está as opções dos hamburgers premiuns e seus preços ")
      detalhes2 = str(input("para saber detalhes dos hambuguers premiuns digite sim!"))
      if detalhes2 == "sim":
        print("\n PALERMO",palermo, "\n LONDON", london , "\n KINGSTON", kingston)
      else :
        print("finalize o seu pedido em comprar!")  
  cardapio_premiun()  
  
  def comprar():
    if opcoes == 2:
      pedido = input("digite aqui o seu pedido! ")
      pedido
      
      
      print("seu pedido foi {} obrigado pela preferencia!" .format(pedido))
      print("volte sempre!")
  comprar()


  print("")
  print("===========")
  print("0 para CONTINUAR | 1 para SAIR") 
  if int(input()) == 1:
   break