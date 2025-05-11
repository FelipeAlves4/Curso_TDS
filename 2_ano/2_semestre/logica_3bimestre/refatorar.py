def solicitar_numeros():
    while True:
        try:
            a = int(input("Número A: "))
            b = int(input("Número B: "))
            return a, b
        except ValueError:
            print("Entrada inválida. Por favor, insira números inteiros.")

def mostrar_menu():
    print("Menu: ")
    print("1. Soma")
    print("2. Subtração")
    print("3. Divisão")
    print("4. Multiplicação")
    print("5. Sair")

def realizar_operacao(escolha, a, b):
    if escolha == 1:
        print(f"Resultado: {a + b}")
    elif escolha == 2:
        print(f"Resultado: {a - b}")
    elif escolha == 3:
        try:
            print(f"Resultado: {a / b}")
        except ZeroDivisionError:
            print("Não é possível fazer divisão por zero. Escolha outro número.")
    elif escolha == 4:
        print(f"Resultado: {a * b}")

def main():
    while True:
        a, b = solicitar_numeros()
        while True:
            mostrar_menu()
            try:
                escolha = int(input("Qual o número da operação: "))
                if 1 <= escolha <= 4:
                    realizar_operacao(escolha, a, b)
                elif escolha == 5:
                    print("Saindo...")
                    return  # Sai da função main, encerrando o programa
                else:
                    print("Opção Inválida, tente novamente.")
            except ValueError:
                print("Opção inválida. Por favor, insira um número válido.")

main()
