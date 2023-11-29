
#FOR LOOP


#EX2

bancos = ['Itau', 'Bradesco', 'Banco do Brasil']
cotacoes = [10, 20, 30]
for i in range(0, len(bancos)):# começa do indice 0

    print(i)
    print(bancos[i], cotacoes[i])
    print(f"O preço da ação {bancos[i]} é {cotacoes[i]}")
breakpoint()
#---------------------------------
# A CADA ELEMENTO X , FAÇA Y
#EX1
bancos = ['Itau', 'Bradesco', 'Banco do Brasil']
for banco in bancos:
    print(banco)
#---------------------------------
#LOOP WHILE
#EX4
i = 0
while i < 10:
   print(i)
   i= i + 1

#---------------------------------

#EX3

meta_vendas = 10
vendas = 0
while vendas < meta_vendas:
    print(f"Total de vendas: {vendas}! Trabalhem mais")
    vendas = vendas +1
print("Meta batida")

#---------------------------------
#CONDICIONAIS


#EX2
metodo_pagamento = input("Qual seu método de pagamento? ")
if metodo_pagamento == "pix" or metodo_pagamento == "cartão":
    print("Podemos receber seu pagamento!")
elif metodo_pagamento == "dinheiro":
    print("Infelismente não podemos aceitar pois não vivemos mais como os Incás :(")
else:
    print("Não conhecemos esse tipo de dinheiro! ")

#---------------------------------








#EX1

dinheiro = int(input("Quanto dinheiro você tem para investir hoje: "))

if dinheiro <= 20:
    print("Invista em você mesmo")
elif dinheiro > 20 and dinheiro <= 1000:
    print("Comece a montar uma carteira de investimentos")
else:
    print("Invista pesado e se aposente cedo")


#---------------------------------
