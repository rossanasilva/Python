# chamadas de functions aninhadas -> são functions chamadas dentro de outras functions
# isso é possível porque certas functions retornarão o value, podendo usá-lo como argumento
# para a próxima function

# programa para pedir ao usuário para digitar um número inteiro positivo
# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num) # valor absoluto
# num = round(num) # arredondar para o número mais próximo
# print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))