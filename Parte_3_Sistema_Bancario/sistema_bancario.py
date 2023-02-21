from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self._contas.append(conta)
        
class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self.historico = Historico()
    
    @classmethod    
    def nova_conta(self):
        pass
    
    @property
    def saldo (self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero 
    
    @property
    def cliente(self):
        return self._clinte
    
    def sacar(self, valor):
        saldo = self._saldo
        if saldo < valor:
            print("\n@!@!@!@ Você não possui saldo suficiente @!@!@!@\n")
        elif valor > 0:
            self._saldo -= valor
            print("\n=-=-=-=-=-= Saque efetuado com sucesso! =-=-=-=-=-=\n")
            return True
        else:
            print("\n@!@!@ Valor inválido para saque @!@!@\n")
        return False
            
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=-=-=-=-=-= Depósito efetuado com sucesso! =-=-=-=-=-=")
            return True
        else:
            print("\n@!@!@ Valor inválido para saque @!@!@\n")
        return False
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
        
class Historico():
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo" : transacao.__class__.__name__,
                "valor" : transacao.valor,
                "data" : datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )
        
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass
        
        
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.depositar(self._valor):
            conta.historico.adicionar_transacao(self)
    