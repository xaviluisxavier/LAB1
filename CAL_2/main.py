from CAL_2.Operacoes.somar import Somar
from CAL_2.Operacoes.subtrair import Subtrair
from CAL_2.Operacoes.dividir import Dividir

class InterfaceCalculadora:
    def __init__(self):
        self.op_map = {
            '+': Somar(),
            '-': Subtrair(),
            '/': Dividir()
        }

    def exibir_menu(self):
        print("\nCALCULADORA")
        print("Opções: +, -, /")

    def obter_inputs(self, operador):
        try:
                num1 = float(input("Número 1: "))
                num2 = float(input("Número 2: "))
                return (num1, num2)
        except ValueError:
            print("Erro: Por favor, digite apenas números válidos.")
            return (None, None)

    def iniciar(self):
        self.exibir_menu()
        operador = input("Escolha a operação: ")
        if operador in self.op_map:
            operacao_obj = self.op_map[operador]
            
            num1, num2 = self.obter_inputs(operador)

            if num1 is not None:
                resultado = operacao_obj.calcular(num1, num2)
            print(f"Resultado: {resultado}")
        else:
            print("Operação desconhecida.")

if __name__ == "__main__":
    app = InterfaceCalculadora()
    app.iniciar()