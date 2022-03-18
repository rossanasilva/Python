# listas 2D são listas que contém outras listas

# 0        # 0        1       2
drinks = ["coffee", "soda", "tea"]
# 1
dinner = ["pizza", "hamburger", "hotdog"]
# 2
dessert = ["cake", "ice cream"]

# adicionar todas essas listas em uma lista chamada food

food = [drinks, dinner, dessert]

# o primeiro index acessar a lista o segundo index acessar o item da lista selecionada
print(food[0][0])