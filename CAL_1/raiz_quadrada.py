import math

def raiz_quadrada(a: float) -> float:
    if a < 0:
        print("Erro: Não existe raiz de número negativo.")
        return 0.0
    return math.sqrt(a)


