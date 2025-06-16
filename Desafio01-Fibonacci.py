
def Fibonacci_recursivo(n):
    if n < 0:
        raise ValueError("O valor de N deve ser maior ou igual a 0.")
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return Fibonacci_recursivo(n - 1) + Fibonacci_recursivo(n - 2)

def Fibonacci_linear(n):
    if n < 0:
        raise ValueError("O valor de N deve ser maior ou igual a 0.")
    if n == 0:
        return 0
    
    v0 = 0
    v1 = 1
    for _ in range(n - 1):
        v0, v1 = v1, v0 + v1
    if n > 0:
        return v1
    else:
        return v0

def main():
    
    while True:
        try:
            n = int(input("Digite um número inteiro (N >= 0): "))

            print("\nResultado: ")
            print(f"Fibonacci Recursivo de {n}: {Fibonacci_recursivo(n)}")
            print(f"Fibonacci Linear de {n}: {Fibonacci_linear(n)}")

            # coloquei esta opção de resposta para facilitar novas verificações, 
            # assim o usuário não terá que compilar o programa novamente
            # caso queira verificar um novo número.
            while True:
                resp = input("\nDeseja verificar mais um número (S/N)?").strip().upper()
                if resp in ("S", "N"):
                    break
                print("Resposta inválida. Digite apenas 'S' ou 'N'.")

            if resp == "N":
                print("Encerrando programa...")
                break

        except ValueError as e:
            print("Erro: ", e)

if __name__ == "__main__":
    main()
