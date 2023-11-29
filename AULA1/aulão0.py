






#FUNÇÕES LISTA
bancos = ['Itau', 'Bradesco', 'Banco do Brasil']
preco_acoes = [20, 15, 10]
bancos.append("Santander")# colocar um elemento no fim da lista .append
preco_acoes.append(30)
#ADICIONAR UM NOVO DADO EM UMA POSIÇÃO ESPECIFICA
bancos.insert(0, "Nubank")
#REMOVER ITEM DA LISTA
bancos.remove('Bradesco')
print(bancos)


#ORDENAR UMA LISTA
preco_acoes.sort()# ordenar lista
print(preco_acoes)
breakpoint()

#---------------------------------------
#Lista
lista_nomes = ["breno", "leandro", "lucas"]
print(lista_nomes[0:2])
print(lista_nomes[1])

#---------------------------------------

#Como comentar em codigo
'''
comentar varias linha sem problema nenhum
'''

#COMO COLETAR DADOS DE USUARIOS


#EX:3
nome = str(input("Qual é seu nome? "))
idade = int(input("Qual é sua idade?"))

ano_nascimento = 2023 - idade
print(f"Olá {nome}, seja muito bem vindo. Soube que você tem {idade} anos e nasceu no ano {ano_nascimento}")

#---------------------------------------

# FUNÇÕES MATEMÁTICAS ÚTEIS NATIVAS DO PYTHON

# #EX:1
numero_maximo = max(4, 10)
print(numero_maximo)
numero_minumo = min(4, 10)
print(numero_minumo)

rentabilidade_ibovespa = round(0.424515485665, 2)# 2  é duas casa decimais
print(rentabilidade_ibovespa)

#---------------------------------------

#COMO LIDAR COM NÚMEROS E OPERAÇOES ARITMETICAS

#EX:2
soma = 2 + 2
subtracao = 10 - 8
multiplicacao = 100 * 8
exponeciar = 2 ** 5
dividir_inteiro = 5 // 2
resto_divisao =  5 % 2
equacao = (10 + 5) * 2 ** 2 - 6 / 3

print(soma)
print(subtracao)
print(multiplicacao)
print(exponeciar)
print(dividir_inteiro)
print(resto_divisao)

print(equacao)



#---------------------------------------
#EX:1
inteiro = 30
numero_decimal = 1.54

convertendo_texto_para_inteiro = int("50")
print(type(convertendo_texto_para_inteiro))
print(convertendo_texto_para_inteiro)

convertendo_texto_para_float = float("50.12")
print(type(convertendo_texto_para_float))
print(convertendo_texto_para_float)
#---------------------------------------







#Como colocar variaves dentro de textos
#Ex:1

empresa = "Itau"
anos = "50"
anos_em_numero = 50
print("Vou investir na empresa " + empresa + " que possui " + anos +" anos de existencia.")
print(f"Vou investir na empresa {empresa} que possui {anos_em_numero} anos de existencia.")

ano_fundacao = 2023 - anos_em_numero

print(f"Vou investir na empresa {empresa} que possui {anos_em_numero} anos e foi fundada em {ano_fundacao}.")



#---------------------------------------
#Ex:2
nome = "Paulo"
idade = "50"
print("Estamos aprendendo Python")
print(f"Meu aluno se chama {nome} e a idade dele é {idade}")
print(f"O {nome} irá aprender a programar hoje")

#---------------------------------------

#COMO SELECIONAR LETRAS DENTRO DA FRASE
frase = "eu amo finanças"
print(frase[1])
print(frase[-1])# -1 pegaria a ultima posição
print(frase[0:2])
print(frase[0:])
print(len(frase))
frase_timão = frase.replace("finanças", "Corinthians")
print(frase_timão)


#---------------------------------------


#COMO COLOCAR PALAVRAS EM MAIUSCULO
frase = "eu amo finanças"
#SELECIONAR LETRA DENTRO DE PALAVRAS
#SABER TAMANHO DE UMA FRASE
print(frase)
print(frase.upper())
print(frase.lower())
print(frase.title())
# Atribuir variavel a outra variavel
frase_maius = frase.upper()
print(frase_maius)

print(frase_maius.islower())
print(frase_maius.isupper())
print(frase_maius.istitle())
#---------------------------------------




#STRING
nome = "Paulo"
print("Estamos aprendendo Python")
print("Meu aluno se chama " + nome)
print("O " + nome + " irá aprender a programar hoje")
#INTEIRO
#FLOAT
#BOOLEANO
#---------------------------------------