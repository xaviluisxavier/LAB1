import math

class RaizQuadrada:
    """
    Classe responsável pela operação de raiz quadrada.
    """
    def calcular(self, num1, num2=None):
        """
        Retorna a raiz quadrada do primeiro número.
        O segundo argumento (num2) é ignorado, mantido apenas para
        compatibilidade com a chamada padrão das outras operações.
        """
        if num1 < 0:
            return "Erro (Número negativo)"
        return math.sqrt(num1)


