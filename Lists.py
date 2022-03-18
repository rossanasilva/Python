# listas são usadas para armazenar vários itens em uma só variável

#          0          1           2          3           4
food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi"

# print(food[0])

# food.append("ice cream") # adiciona ice cream na lista (final)
# food.remove("hotdog") # remove hotdog da lista
# food.pop() # remove o ultimo elemento da lista
# food.insert(0, "cake") # adiciona no indice 0 -> cake
# food.sort() # vai deixar a lista em ordem alfabética
# food.clear() # remove todos os itens da lista

for x in food:
	print(x,"",end="")