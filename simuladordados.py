import random

def rolar_dado():
    return random.randint(1, 6)  # Gera um número aleatório entre 1 e 6
#randint gerar números inteiros aleatórios dentro de um intervalo especificado

def simulador_dado():
    print("Bem-vindo ao simulador de dado!")
    
    while True:
        input("Pressione Enter para rolar o dado...")
        resultado = rolar_dado()
        print(f"O resultado da rolagem do dado é: {resultado}")
        
        continuar = input("Deseja rolar o dado novamente? (s/n): ").lower()
        if continuar != 's':
            print("Saindo do simulador. Até logo!")
            break

# Executa o simulador de dado
if __name__ == "__main__":
    simulador_dado()
