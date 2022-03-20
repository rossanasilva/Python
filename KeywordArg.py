# argumentos de palavras-chave -> são argumentos que são procedidos por um idetificador quando
# os passamos para a function 
# a ordem dos argumentos não importa, diferente de argumentos posicionais
# o python sabe o nome dos argumentos que a function recebe

def hello(first, middle, last):
	print("Hello " + first + " " + middle + " " + last)

# usar um identificador para cada argumento, não importando a ordem
# por fim irá mostrar na ordem passada nos parâmetros da function
hello(last="da Silva", middle="Laurentino", first="Rossana")