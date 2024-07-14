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

# Operacao de saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if (numero_saques + 1) > limite_saques:
        print("Operação não permitida. Número máximo de saques por dia atingido.")
        return saldo, extrato, numero_saques

    elif valor > limite:
        print("Operação não permitida. Saque maior que limite diário (R$ 500.00).")
        return saldo, extrato, numero_saques

    elif (saldo - valor) < 0:
        print("Operação não permitida. Saldo insuficiente para saque.")
        return saldo, extrato, numero_saques

    saldo -= valor
    numero_saques += 1

    print(f"O valor sacado da sua conta foi de R$ {valor:.2f}")
    extrato += f"\nSaque: R$ {valor:.2f}"

    return saldo, extrato, numero_saques

# Operacao de deposito
def depositar(saldo, valor, extrato):

    saldo += valor

    print(f"O valor depositado na sua conta foi de R$ {valor:.2f}")
    extrato += f"\nDeposito: R$ {valor:.2f}"

    return saldo, extrato

# Operacao de extrato
def visualiza_extrato(saldo, *, extrato):

    print(SEPARADOR + " Extrato " + SEPARADOR)

    if extrato == "":
        print("Não foram realizadas movimentações.")
        return

    saldo_total = f"\nSaldo Total: R$ {saldo:.2f}"
    print(extrato, saldo_total)

    return

# Navegando pelo menu das operacoes
while True:

    opcao = input(menu)
    
    # Operacao Deposito
    if opcao == "1":

        deposito = float(input("Digite a quantia para depósito em reais: "))
        saldo, extrato = depositar(saldo, deposito, extrato)

    # Operacao Saque
    elif opcao == "2":

        saque = float(input("Digite a quantia para saque em reais: "))
        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=saque, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    # Operacao Extrato
    elif opcao == "3":

        visualiza_extrato(saldo, extrato=extrato)

    # Saida do sistema
    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
