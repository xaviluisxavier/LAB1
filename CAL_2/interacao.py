# Importação com 'alias' (as) como pedido na alínea 2e
from Operacoes.somar import Somar as S
from Operacoes.subtrair import Subtrair as Sub
from Operacoes.dividir import Dividir as D
from Operacoes.multiplicar import Multiplicar as M
from Operacoes.raiz_quadrada import RaizQuadrada as R

class Interacao:
    def __init__(self):
        pass

    def obter_inputs(self):
        """
        Solicita dois números ao utilizador e força a tipagem para float.
        """
        

    def execute(self):
        print("\n--- CALCULADORA 2 ---")
        try:
            num1 = float(input("Introduza o primeiro número: "))
            num2 = float(input("Introduza o segundo número: "))
            s = S()
            #Soma
            res = s.calcular(num1,num2)
            print("Valor da soma:" , res)

            #Subtrair
            sub = Sub()
            res = sub.calcular(num1,num2)
            print("Valor da Substração:" , res)

             #Multiplicação
            mul = M()
            res = mul.calcular(num1,num2)
            print("Valor da Multiplicação:" , res)

             #Dividir
            div = D()
            res = div.calcular(num1,num2)
            print("Valor da Divisão:" , res)

             #Raiz
            raiz = R()
            res = raiz.calcular(num1)
            print("Valor da Raiz (Num 1):" , res)



        except ValueError:
            print("Erro: Por favor, digite apenas números válidos.")
            return (None, None)