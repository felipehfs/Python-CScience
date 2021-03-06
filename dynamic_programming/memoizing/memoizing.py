# Utilizando memoizing e alguns conceitos de dynamic programming

def fib(n, memo):
	''' Função que calcula o fibonacci utilizando memoizing como cache'''
	if n <= 0:
		return 0
	if n == 1:
		return 1
	elif not n in memo:
		memo[n] = fib(n-1, memo) + fib(n-2, memo)
	return memo[n]

def fat(n, cache):
	''' Função que retorna o fatorial desejado'''
	if n < 0:
		raise ValueError("Impossível calcular o fatorial de número negativo")
	if n == 1 or n == 0:
		return 1
	elif not n in cache:
		cache[n] = fat(n - 1, cache) * n
	return cache[n]

print("Fib(14) = {}".format(fib(14, {})))
print("12! = {}".format(fat(12, {})))
