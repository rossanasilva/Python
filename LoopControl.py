# instruções de controle de um loop
# usados para alterar a execução de um loop a partir de sua sequência

""" instruções de controle de loop alteram a execução de sua sequência normal. 
	quando a execução deixa um escopo, todos os objetos automáticos
	que foram criados nesse escopo são destruídos. """

# break -> encerra todo o loop
# continue -> pula para a próxima iteração do loop
# pass -> atua como um espaço vazio de loops vazio, não faz nada

# exemplo de break
# enquanto você não digitar seu nome, ele vai continuar o loop

""" while True:
		name = input("Enter your name: ")
		if name != "":
			break """

# exemplo de continue
# mostrar o número do celular sem os traços

""" phone_number = "123-456-7890"
	for i in phone_number:
		if i == "-":
			continue
		print(i, end="") """

# exemplo de pass
# printar a contagem de 1 a 20 usando um loop for, sem mostrar o número 13

for i in range(1, 21):
	if i == 13:
		pass
	else:
		print(i)
