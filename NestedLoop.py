# nested loop é um loop dentro de outro loop
# O loop interno ou externo pode ser de qualquer tipo, como loop while ou loop for.
# Por exemplo, o loop externo for pode conter um while loop e vice-versa.

# retângulo de @

rows = int(input("How many rows?: ")) # linhas
columns = int(input("How many columns?: ")) # colunas
symbol = input("Enter a symbol to use: ")

""" criando os loops aninhados, o loop externo será para as linhas
o loop interno será para as colunas """

for i in range(rows):
	for j in range(columns):
		print(symbol, end="") # o end="" irá impedir que o print quebre uma linha, ou pule a linha
	print()