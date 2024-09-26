# Função para mostrar o menu e obter a escolha do usuário
def menu():
    saldo = 0  # Inicializa o saldo
    while True:
        print("\n--- Caixa Eletrônico ---")
        print("1. Ver Saldo")
        print("2. Depositar Dinheiro")
        print("3. Sacar Dinheiro")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print(f"Seu saldo atual é: R$ {saldo:.2f}")
        
        elif opcao == "2":
            deposito = float(input("Digite o valor que deseja depositar: R$ "))
            if deposito > 0:
                saldo += deposito
                print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
            else:
                print("O valor do depósito deve ser maior que zero.")
        
        elif opcao == "3":
            saque = float(input("Digite o valor que deseja sacar: R$ "))
            if 0 < saque <= saldo:
                saldo -= saque
                print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
            elif saque > saldo:
                print("Saldo insuficiente para realizar o saque.")
            else:
                print("O valor do saque deve ser maior que zero.")
        
        elif opcao == "4":
            print("Saindo do caixa eletrônico. Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu principal
if __name__ == "__main__":
    menu()
