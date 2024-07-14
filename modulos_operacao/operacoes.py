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
SEPARADOR = 30 * "*"

# Navegando pelo menu das operacoes
while True:

    opcao = input(menu)
    
    # Operacao Deposito
    if opcao == "1":
        
        deposito = float(input("Digite a quantia para depósito em reais: "))
        saldo += deposito

        print(f"O valor depositado na sua conta foi de R$ {deposito:.2f}")
        extrato += f"\nDeposito: R$ {deposito:.2f}"

    # Operacao Saque
    elif opcao == "2":

        if (numero_saques + 1) > LIMITE_SAQUES:
            print("Operação não permitida. Número máximo de saques por dia atingido.")
            continue

        saque = float(input("Digite a quantia para saque em reais: "))

        if saque > limite:
            print("Operação não permitida. Saque maior que limite diário (R$ 500.00).")
            continue

        elif (saldo - saque) < 0:
            print("Operação não permitida. Saldo insuficiente para saque.")
            continue

        saldo -= saque
        numero_saques += 1

        print(f"O valor sacado da sua conta foi de R$ {saque:.2f}")
        extrato += f"\nSaque: R$ {saque:.2f}"

    # Operacao Extrato
    elif opcao == "3":

        print(SEPARADOR + " Extrato " + SEPARADOR)

        if extrato == "":
            print("Não foram realizadas movimentações.")
            continue

        saldo_total = f"\nSaldo Total: R$ {saldo:.2f}"
        print(extrato, saldo_total)

    # Saida do sistema
    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
