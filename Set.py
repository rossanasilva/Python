""" set uma coleção de itens desordenada, parcialmente imutável 
	e que não podem conter elementos duplicados. 
	Por ser parcialmente imutável, os sets possuem permissão de adição e remoção de elementos.
	"""

# set de utensílios

utensils = {"fork", "spoon", "knife"} # se você adicionar itens duplicados não vai printar o duplicado
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes) # adiciona a utensils, os elementos de dishes
# dinner_table = utensils.union(dishes) # união dos sets

# como é um set, vai printar desordenado
"""for x in dinner_table:
	print(x, "", end="")"""

# método de comparar as semelhanças e as diferenças dentro dos elementos encontrados em dois sets

print(utensils.difference(dishes)) # vai mostrar os itens que utensils tem que dishes não tem
print(utensils.intersection(dishes)) # vai mostrar os itens em comum entre utensils e dishes