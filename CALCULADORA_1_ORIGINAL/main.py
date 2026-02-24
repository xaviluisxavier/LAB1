def subtrair(x: float, y: float) -> float:
    """
    Subtrai dois números
    :param x: valor subtraido
    :param y: valor a subtrair
    :return: retorna o resultado da subtraçao
    """
    return x - y


def somar(x: float, y: float) -> float:
    return x + y


def dividir(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y


def multiplicar(x: float, y: float) -> float:
    return x * y

def raizquadrada( x: float) -> float:
    pass

def main():
    print("Qual é o cálculo que quer efetuar? x + - /")
    res: str = input()
    print("Preciso que introduza dois valores:")
    x: float = float(input("x="))
    y: float = float(input("y="))

    # Teste
    # print(res)
    if res == "x":
        z: float = multiplicar(x, y)
        print("O resultado da multiplicação é:", z)
    elif res == "/":
        try:
            z = dividir(10, 0)
            print("O resultado da soma é:", z)
        except ZeroDivisionError as e:
            print("Error:", e)
    elif res == "+":
        m: float = somar(x, y)
        print("O resultado da soma é:", m)
    else:
        n: float = subtrair(x, y)
        print("O resultado da subtração é:", n)


if __name__ == '__main__':
    main()
