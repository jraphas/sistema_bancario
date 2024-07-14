# Representacao do menu
menu = """
Escolha uma das opções do sistema abaixo:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

# Variaveis e constantes auxiliares
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Navegando pelo menu das operacoes
while True:

    opcao = input(menu)
    
    # Operacao Deposito
    if opcao == "1":
        
        deposito = float(input("Digite a quantia para depósito em reais: "))
        saldo += deposito

        print(f"O valor depositado na sua conta foi de R$ {deposito:.2f}")

    # Operacao Saque
    elif opcao == "2":
        print("teste")

    # Operacao Extrato
    elif opcao == "3":
        print("teste")

    # Saida do sistema
    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
