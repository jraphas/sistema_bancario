from abc import ABC, abstractmethod
import datetime

AGENCIA = "0001"

class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):

    def __init__(self, valor: float) -> None:
        self._valor = valor

    def registrar(self, conta):
        if(conta.depositar(self._valor)):
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):

    def __init__(self, valor: float) -> None:
        self._valor = valor
    
    def registrar(self, conta):
        if(conta.sacar(self._valor)):
            conta.historico.adicionar_transacao(self)

class Historico:

    def __init__(self):
        self._lista_transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self._lista_transacoes.append(transacao)

class Cliente:

    def __init__(self, endereco: str, contas: list) -> None:
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class Conta:

    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, historico: Historico) -> None:
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico
    
    def saldo(self) -> float:
        return self._saldo
    
    def nova_conta(self, cliente: Cliente, numero: int):
        conta = Conta(0, numero, AGENCIA, cliente, Historico())
        return conta
    
    def sacar(self, valor: float) -> bool:
        if (self.saldo() - valor) < 0:
            print("Operação não permitida. Saldo insuficiente para saque.")
            return False

        self._saldo -= valor

        print(f"O valor sacado da sua conta foi de R$ {valor:.2f}")

        return True
    
    def depositar(self, valor: float) -> bool:
        if (valor < 0):
            return False
        
        self._saldo += valor

        print(f"O valor depositado na sua conta foi de R$ {valor:.2f}")

        return True


class ContaCorrente(Conta):

    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, historico: Historico, limite: float, limite_saques: int) -> None:
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor: float) -> bool:
        numero_saques = 0

        for transacao in self._historico._lista_transacoes:
            if( type(Saque()).__name__ == type(transacao).__name__ ):
                numero_saques += 1

        if (numero_saques + 1) > self._limite_saques:
            print("Operação não permitida. Número máximo de saques por dia atingido.")
            return False

        elif valor > self._limite:
            print("Operação não permitida. Saque maior que limite diário (R$ 500.00).")
            return False

        elif (self.saldo() - valor) < 0:
            print("Operação não permitida. Saldo insuficiente para saque.")
            return False

        self._saldo -= valor

        print(f"O valor sacado da sua conta foi de R$ {valor:.2f}")

        return True

class PessoaFisica(Cliente):

    def __init__(self, endereco: str, contas: list, cpf: str, nome: str, data_nascimento: datetime) -> None:
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento