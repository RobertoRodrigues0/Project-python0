#PROJETO CRIANDO UMA CALCULADORA DE JUROS COMPOSTOS
#EX:3
# FORMULA DE JUROS COMPOSTOS: montante = inicial * (1 + taxa)** tempo


nome = str(input("Qual é o seu nome? "))
print(f"Olá {nome}, seja muito bem vindo aos juros compostoa! Aqui nós cuidamos da sua aposentadoria: ")

dinheiro_inicial = int(input("Digite a quantidade de dinheiro inicial do investimento: "))
tempo = int(input("Digite quantos anos você deixará o dinheiro investido: "))
taxa = float(input("Digite, em decimal, qual a taxa anual de retorno do seu investimento: "))

montante = dinheiro_inicial * (1 + taxa) ** tempo
montante = round(montante, 2)
print("---------------------------------------")

print(f"Parabéns {nome}! Ao final do periodo você terá R${montante} ")
breakpoint()
#---------------------------------------