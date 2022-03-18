# operador index [] ele te dá acesso a uma sequência de elementos (str, list, tuples, ...)
#       0123456789...
name = "rossana Silva!"

# ver se a primeira letra do nome é minúscula
# e mudar para maiúscula

#if(name[0].islower()):
#	name = name.capitalize()

#print(name)

# criar uma substring da primeira parte do nome, usando os indices de 0 a 7 (0:7) ou pode usar só :7
first_name = name[:7].upper()

# criar uma substring da segunda parte do nome
last_name = name[8:].lower()

# pode acessar o ultimo elemento em uma sequência usando a chamada index negativa
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)