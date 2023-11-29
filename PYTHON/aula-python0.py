#FUNÇÕES
#EX:1


#-------------------------------------------

#FUNÇÕES
#EX:2
fluxo_caixa = []
print("-------------")
print("@ Fluxo caixa")
print("-------------")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("/n# Digite outro numero para encerrar #/n")

def adicionar_transacao(opcao):
    nome = str(input("Nome:"))
    valor = float(input("Valor: "))
    fluxo_caixa.append({
            "nome": nome,
            "valor": valor
        })

while True:
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        adicionar_transacao
    elif opcao == 2:
        adicionar_transacao

    else:
        break

# nota fiscal
total = 0
for fc in fluxo_caixa:
    print("Nome: ", fc['nome'], ", Valor: R$", fc['valor'])
    total = total + fc['valor']
print("Saldo atual: R$", total)
breakpoint()
#-------------------------------------------
#FUNÇÕES
#EX:1
#codigo sem função
fluxo_caixa = []
print("-------------")
print("@ Fluxo caixa")
print("-------------")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("/n# Digite outro numero para encerrar #/n")
while True:
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        nome =str(input("Nome:"))
        valor = float(input("Valor: "))
        fluxo_caixa.append({
            "nome": nome,
            "valor": valor
        })
    elif opcao == 2:
        nome = input("Nome: ")
        valor = float(input("Valor: "))
        fluxo_caixa.append({
            "nome": nome,
            "valor": valor
        })

    else:
        break

# nota fiscal
total = 0
for fc in fluxo_caixa:
    print("Nome: ", fc['nome'], ", Valor: R$", fc['valor'])
    total = total + fc['valor']
print("Saldo atual: R$", total)
#-------------------------------------------
#FUNÇÕES
#EX:1
def minha_funcao(valor1, valor2):
    return valor1 + valor2
#resposta = minha_funcao(10, 10)
#print("Resposta:", resposta)


while True:
    valor1 = int(input("Valor1: "))
    valor2 = int(input("Valor2: "))

    resposta = minha_funcao(valor1, valor2)
    print(valor1, "+", valor2, "=", resposta)



#-------------------------------------------






#DICIONARIOS

#REPETIÇÕES WHILE
#EX:4

#-------------------------------------------
#REPETIÇÕES WHILE
#EX:3
import os
mensagens = []

nome = str(input("Nome: "))
while True:
    #Limpar terminal
    os.system('cls')
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("_____________________________________")

#-------------------------------------------
# Obtendo o texto
    texto = str(input("mensagem: "))
    if texto == "fim":
        break
# Adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })

#-------------------------------------------
#REPETIÇÕES WHILE
#EX:2
pessoa = {
    "nome": "Programador Python",
    "idade": 27,
    "peso": 70.2
}
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['peso'])

#-------------------------------------------


#REPETIÇÕES WHILE
#EX:1
#IINFORMAÇÕES DO JOGADOR
player = {
    "nome": "Guilherme",
    "level": 1,
    "hp": 100,
    "exp": 0,
    "dano": 5,
}
# LISTA DE INIMIGOS
npcs = [
    {"nome": "Monstrinho", "dano": 2, "hp": 50, "exp": 5},
    {"nome": "Monstro", "dano": 5, "hp": 100, "exp": 10},
    {"nome": "Monstrão", "dano": 10, "hp": 150, "exp": 15},
    {"nome": "Chefão", "dano": 25, "hp": 200, "exp": 20},

]

#-------------------------------------------




#REPETIÇÕES WHILE
#EX:4
notas = []
contador = 1
while contador <= 5:
    codigo_aluno = str(input("RM: "))
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    #Alternativa: contador += 1
    contador = contador + 1
print("Quantidade de notas", len(notas))
#-------------------------------------------

#REPETIÇÕES
#EX:3
notas = []
for x in range(5):
    codigo_aluno = str(input("RM: "))
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
print("Quantidade de notas", len(notas))
for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM", codigo_aluno, "tirou a nota:", nota)
#-------------------------------------------

#REPETIÇÕES WHILE
#EX:2
#-------------------------------------------

while True:
    print("Se eu rodar o script meu pc morre")


#REPETIÇÕES
#EX:1
#-------------------------------------------
for x in range (11):
    print(x)


# IF, ELSE
#EX:5
numeros = [10, 9, 8, 7, 6]


print("Total", len(numeros))
print("Menor valor", min(numeros))
print("Maior Valor", max(numeros))


#-------------------------------------------

#EX:4
lista_vazia = []
lista_vazia.append("Olá")
lista_vazia.append("Mundo")
print(lista_vazia)


#-------------------------------------------



#EX:3

numeros = [1, 2, 3]
string =["Jõao", "Maria", "Bruxa"]
decimais = [10.8, 15.2, 33.4]

list_numeros = [3, 7, 9]
list_numeros[0] = 10
print(list_numeros[0])
print(list_numeros[1])
print(list_numeros[2])

#-------------------------------------------

#EX:2
salario = float(input("Informe o salário: "))

if salario <= 3000:
    print("programador junior")
elif salario > 3000 and salario <= 6000:
    print("programdor pleno")
elif salario > 6000 and salario <= 15000:
    print("programdor senior")
else:
    print("gerente de projetos")



#-------------------------------------------

#EX:2
idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("PERMITIDO")

else:
    print("BLOQUEADO")

#-------------------------------------------



#EX:1
valor1 = 10
valor2 = 50


if valor1 > valor2:
    print(valor1, "é maior que", valor2)
else:
    print(valor2, "é maior que", valor1)

#-------------------------------------------




#-------------------------------------------

# Operadores Matematicos
soma = 1 +1
multiplicacao = 4 * 4
divisao = 30 / 3
potencia =  7 **2
print("soma", soma)
print("multiplicacao", multiplicacao)
print("divisao", divisao)
print("potencia", potencia)
#------------------------------






#MOSTRA NA TELA
nome1 = "Roberto"
idade1 = "36"
peso1 = float("85.3")
print("Olá Mundo, seu nome é:", nome1, "você tem á idade:", idade1, " seu peso é:", peso1, type(peso1))
print(1+3)

nome = str(input("Seu nome:"))
idade = int(input("Digite sua idade:"))

print("Seu nome é:", nome, "é sua idade é:", idade)

#------------------------



#
#str,int,float
#------------------------


#BOOLEAN
is_python = True
is_java = False


#Armazenando condiçoes
ingressos = 50
compradores = 250
tem_ingresso_suficiente = (ingressos >= compradores)
print(tem_ingresso_suficiente)
#------------------------





