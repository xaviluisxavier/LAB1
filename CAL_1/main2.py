from multiplicar import multiplicar
from somar import somar
from subtrair import subtrair
from raiz_quadrada import raiz_quadrada
from dividir import dividir

def iniciar_calculadora_total(): 
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        print("\n--- Resultados ---")

        res_soma = somar(num1, num2)
        print(f"Soma ({num1} + {num2}) = {res_soma}")

        res_sub = subtrair(num1, num2)
        print(f"Diferença ({num1} - {num2}) = {res_sub}")

        res_mult = multiplicar(num1, num2)
        print(f"Multiplicação ({num1} * {num2}) = {res_mult}")

        try:
            res_div = dividir(num1, num2)
            print(f"Divisão ({num1} / {num2}) = {res_div}")
        except ZeroDivisionError:
            print("Divisão: Erro - Não é possível dividir por zero.")

        try:
            res_raiz = raiz_quadrada(num1)
            print(f"Raiz Quadrada de {num1} = {res_raiz}")
        except ValueError:
            print(f"Raiz Quadrada: Erro - Não existe raiz real de número negativo.")

    except ValueError:
        print("Erro: Por favor, introduza apenas números válidos.")

if __name__ == "__main__":
    iniciar_calculadora_total()


