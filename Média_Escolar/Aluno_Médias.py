# projeto 9

cod_alunoD = {}# dicionário vazio é criado 
banco_notas = {}# outro dicionário vazio é criado
lista_notas = []# uma lista vazia é criada
banco_medias = {}# mais um dicioário vazio é criado
#entrada
while True:# um laço de repetição é criado através da função while utilizando o True irá se repetir tudo que estiver dentro da função enquanto for verdadeiro. 

    print("0 - CADASTRAR ALUNO \n1 - MOSTRAR CADASTROS \n2 - MOSTRAR NOTA")# print mostra as opções ao usuário sendo assim um menu.
    conf = int(input("Digite sua opção: "))# variável criada para receber o dado em numero inteiro para cadastrar o aluno.
    if (conf == 0): # Cadastrar aluno, condição if, se receber o dado igual a 0 irá solicitar uma serie de informações ao usuário
        cod_aluno = input("Digite um código numérico para o aluno: ")# variável criada para solicitar um número que será o seu código de cadastro.
        nome_aluno = input("Digite o nome do aluno:")# variável que solicita o usuário a digitar o nome do aluno.
        nota1 = float(input("Digite a primeira nota do aluno:"))# variável que solicita a primeira nota do aluno usando o input. 
        nota2 = float(input("Digite a segunda nota do aluno:"))# variável que solicita a segunda nota do aluno usando o input.
        nota3 = float(input("Digite a terceira nota do aluno:"))#variável que solicita a terceira nota do aluno usando o input. 
        media = (nota1 + nota2 + nota3) / 3# variável criada para somar as três notas do aluno e dividir por 3 para da a media total.

        lista_notas.append(nota1)# adiciona a nota1 a lista_notas usando o método .append.
        lista_notas.append(nota2)# adiciona a nota2 a lista_notas usando o método .append.
        lista_notas.append(nota3)# adiciona a nota3 a lista_notas usando o método .append.
        cod_alunoD[cod_aluno] = nome_aluno# atribui cod_aluno como chave e nome_aluno como valor ao dicionário cod_alunoD
        banco_notas[cod_aluno] = lista_notas# atribui cod_aluno como chave e lista_notas como valor ao dicionário banco_notas
        banco_medias[cod_aluno] = media# atribui cod_aluno como chave e media como valor ao dicionário banco_medias
        lista_notas = []# não entendi o uso dessa lista.
        print(f'O aluno cadastrado foi {nome_aluno} e a suas notas estão no sistema.')# depois que todos os requesitos foram preenchidos o print mostra que o aluno foi cadastrado.
#processamento
    elif (conf == 1): # Mostrar cadastros, se o usuário digitar 1 
      print("Lista de alunos cadastrados:")# print mostrar string como titulo da lista de alunos cadastrados
      print("-----------------------------")# print com sinais de menos para dar espaços entre os textos
      print(cod_alunoD)# print mostra o codigo do aluno 
    elif (conf == 2): # Mostrar notas de um aluno, se o usuário digitar 2
      Cod_Aluno = input("Digite o cod de cadastro do aluno: ")# variável que pede o codigo do aluno para consultar.
      nome_aluno = cod_alunoD.get(Cod_Aluno)# variavel 
      notas = banco_notas.get(Cod_Aluno)#  variável notas é criada e recebe dic banco_notas com o métedo .get para retornar o valor da chave Cod_aluno.
      media = banco_medias.get(Cod_Aluno)# variável media é criada e recebe dic banco_medias com o métedo .get para retornar o valor da chave Cod_aluno.
      print("As notas do aluno {} são: {}".format(nome_aluno,notas))# print mostra o nome do aluno e notas usando o método .format para substituir as chaves na string.
      print("E sua média é: {}".format(media))# print mostra a media tambem usando o método .format para substituir a chave dentro da string.
#saída
    print("")# não entendi o uso dessas aspas.
    print("===========")# print com vários sinais de igualdade para separar os textos.
    print("0 para CONTINUAR | 1 para SAIR")# print que pergunta se o usuario quer fazer mais alguma ação ou sair. 
    if int(input()) == 1:# se o usuário digitar 1 o ciclo da função while para através da função break.
      break# para o ciclo de repetição.