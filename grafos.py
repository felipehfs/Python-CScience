grafos = {'a': ['b', 'c'], 'b': ['a', 'c'], 'c':['a', 'b']}

def dfs_caminhos(grafo, inicio, fim):
	pilha = [(inicio, [inicio])]
	while pilha:
		vertice, caminho = pilha.pop()
		for proximo in set(grafo[vertice]) - set(caminho):
			if proximo == fim:
				yield caminho + [proximo]
			else:
				pilha.append((proximo, caminho + [proximo]))

caminhos = list(dfs_caminhos(grafos, 'a', 'c'))
print(caminhos)
