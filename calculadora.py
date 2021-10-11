class Calculadora:
	'''Classe Calculadora para manipular as operações da calculadora'''
	
    def soma(self, a, b):
		'''Retorna a soma de a e b'''
        return a + b

    def subtrai(self, a, b):
		'''Retorna a subtração de a por b'''
        return a - b

    def multiplica(self, a, b):
		'''Retorna a multiplicação de a por b'''
        return a * b

    def divide(self, a, b):
		'''Retorna a divisão de a por b'''
        return a / b

    def potencia(self, b, e):
    '''Retorna b elevado a potencia e'''
    return pow(b, e)