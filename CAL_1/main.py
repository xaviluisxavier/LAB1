
from multiplicar import multiplicar
from somar import somar
from subtrair import subtrair
from raiz_quadrada import raiz_quadrada
from dividir import dividir

def iniciar_calculadora():
    print("Opções: +, -, *, /, v (para raiz quadrada)")
    
    operador = input("Escolha a operação: ")

    if operador == 'v':
        num1 = float(input("Digite o número para a raiz: "))
        resultado = raiz_quadrada(num1) 
        
    elif operador in ['+', '-', '*', '/']:
        num1 = float(input("Número 1: "))
        num2 = float(input("Número 2: "))
        
        if operador == '+':
            resultado = somar(num1, num2)
        elif operador == '-':
            resultado = subtrair(num1, num2)
        elif operador == '*':
            resultado = multiplicar(num1, num2)
        elif operador == '/':
            resultado = dividir(num1, num2)
            
    else:
        print("Operação desconhecida.")
        return

    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    iniciar_calculadora()