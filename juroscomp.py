#Juros Composto

#Vf = Vi . (1+i)m

#Vf -Valor final na poupança, ao término do tempo
#Vi -Valor inicial que o cliente vai colocar na poupança
# i -Rentabilidade mensal (em porcentagem)
# m -Tanto de meses que o dinheiro do cliente vai ficar rendendo

#Valor inicial aplicado
vi = float(input("Valor inicial:"))

#Rentabilidade mensagem, em %
i = float(input("Rentabilidade mensal:"))

#Transformando a porcentagem em valor númerico
i = i / 100

#Tempo de investimento
m = int(input("Meses que vai deixar rendendo:"))

vf = vi * (1+i) ** m

print('Valor após',m,'meses:R$',vf)