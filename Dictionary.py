# Os dicionários são coleções de itens e seus elementos são armazenados de forma não ordenada.

# dicionário de capitais
#            key       value
capitals = {'USA': 'Washington DC',
			'India': 'New Dehli',
			'China': 'Beijing',
			'Brazil': 'Brasília'}

# adicionar um novo item no dicionário
capitals.update({'Germany': 'Berlin'})

# pode usar o mesmo .update para atualizar um valor, chave do dicionário
capitals.update({'USA': 'Las Vegas'})

# remover item do dicionário
capitals.pop('China')

# limpar o dicionário
# capitals.clear()

# mostrar o valor de tal chave
print(capitals['Brazil']) # chave: Brazil, valor: Brasília

# modo certo
print(capitals.get('Italy')) # vai pegar essa chave e vai retonar None (nenhum), pois não está no dicionário

# mostrar somente as chaves do dicionário
print(capitals.keys())

# mostrar somente os valores do dicionário
print(capitals.values())

# mostrar todo o dicionário
print(capitals.items())

# pode usar o loop for para mostrar cada chave com seu respectivo valor
for key,value in capitals.items():
	print(key, value)