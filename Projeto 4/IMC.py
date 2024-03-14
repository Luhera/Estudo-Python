#Passo a Passo
#Passo 1: comandos
#Passo 2: Criano Função Principal
#Passo 3:Implemetando a Função
#Passo 4: 

def calcular_imc(peso, altura):
    """
    Calcula o IMC (Índice de Massa Corporal) com base no peso (em kg) e na altura (em metros).
    """
    return peso / (altura ** 2)

def interpretar_comando(comando, peso, altura):
    """
    Interpreta o comando inserido pelo usuário e executa a ação correspondente.
    """
    if comando == 'calcular':
        # Calcula o IMC
        imc = calcular_imc(peso, altura)
        print(f"Seu IMC é: {imc:.2f}")
        # Determina a categoria do IMC
        if imc < 18.5:
            print("Você está magro(a).")
        elif imc >= 18.5 and imc < 25:
            print("Seu peso está na média.")
        else:
            print("Você está acima do peso.")
    else:
        print("Comando inválido!")

def main():
    """
    Função principal do programa.
    """
    while True:
        # Solicita ao usuário um comando
        comando = input("Digite um comando (calcular ou sair): ").lower()
        if comando == 'sair':
            # Sai do programa se o comando for 'sair'
            print("Saindo do programa...")
            break
        elif comando == 'calcular':
            # Solicita ao usuário peso e altura para calcular o IMC
            peso = float(input("Digite o seu peso em kg: "))
            altura = float(input("Digite a sua altura em metros: "))
            # Interpreta o comando e exibe o resultado
            interpretar_comando(comando, peso, altura)
        else:
            print("Comando inválido!")

if __name__ == "__main__":
    main()
