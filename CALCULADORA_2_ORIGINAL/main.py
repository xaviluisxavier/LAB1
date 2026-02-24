import somar
import dividir
#import Operacoes.dividir as dividir
import interface
def main():
    print("Qual é o cálculo que quer efetuar? x + - /")
    res:str = input()
    print("Preciso que introduza dois valores:")
    x:float = float(input("x="))
    y:float = float(input("y="))
    if res =="+":
        s:object = somar.Somar(x,y)
        res = s.executar()
        print("O valor da operação somar é:", res)
    elif res =="/":
        s:object = dividir.Dividir(x,y)
        res = s.executar()
        if type(res)==str:
            print (res)
        else:
            print("O valor da operação divisão é:",res)

if __name__ == '__main__':
    main()

