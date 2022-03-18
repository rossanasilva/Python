# tuplas são coleções ordenadas que não podem ser modificadas (imutáveis)
# utilizada para adicionar tipos diferentes de informações, porém, com a quantidade de elementos definidos

# criando uma ficha estudantil

#              0      1       2
student = ("Rossana", 22, "female")

# count é usada pra saber quantas vezes um elemento na tupla aparece
print(student.count("Rossana"))

# index é usado para saber o indice do elemento na tupla
print(student.index("female"))

print()

# mostrar todos os itens da tupla usando o loop for
for x in student:
	print(x, "", end="")

print()

# saber se um determinado elemento existe na tupla usando o if statement
if "Rossana" in student:
	print("Rossana is here!")