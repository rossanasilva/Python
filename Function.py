# a função é um bloco de código que só é executando quando é chamado
# muito usado para quando se quer repetir códigos, como vários prints iguais

# todo código identado dentro da function, pertence a function
# e só irá executar quando essa function, for chamada


# criar uma função chamada Hello

# def hello(name): # se você não souber o que sua function vai fazer, só escreva pass dentro dela
def hello(first_name, last_name, age):
	print("Hello! " + first_name + " " + last_name)
	print("Have a nice day!")
	print("You are " + str(age) + " years old") # para mostrar esse valor integer, você tem que convertê-lo para string

	# podemos enviar a nossa function algumas informações e ela poderá fazer alguma coisa com
	# essas informações, então só listar os dados que deseja enviar, dentro dos parênteses da function
# para chamar sua function, só escrever o nome dela e colocar parentêses 
# hello("roh") # adcione o argumento que quiser como parâmetro
# my_name = "roh" # pode se criar a variável e chama-la na function
# hello(my_name) # a variável não precisa ter o mesmo nome do parâmetro

# você pode lançar dois ou mais argumentos, contanto que a function, esteja projetada para
# aceitar mais de dois ou mais argumentos

hello("Rossana", "Silva", 22)