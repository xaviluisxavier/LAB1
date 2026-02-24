class Dividir:
    """
    Classe responsável pela operação de divisão.
    """
    def calcular(self, num1, num2):
        """
        Retorna a divisão de num1 por num2.
        Retorna uma mensagem de erro se num2 for zero.
        """
        if num2 == 0:
            return "Erro: Divisão por zero"
        return num1 / num2


