# Lembrete: ler sobre SOLID

class Conta:
    def __init__(self, numero:int, titular:str, saldo:int=0, limite:int=1000):
        self.__numero= numero
        self.__titular= titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, valor):
        self.__numero = valor
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, nome):
       self.__titular = nome 
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, value):
        assert self.__limite < self.extrato
        self.__limite = value

    @property
    def extrato(self):
        return self.__saldo
    
    def depositar(self, valor:int):
        assert valor >= 0, "Não é possivel depositar valores negativos"
        self.__saldo += valor

    def sacar(self, valor):
        assert valor >= 0, "Não é possivel sacar valores negativos"
        assert self.__saldo >= valor, "Saldo insuficiente" 
        assert self.__limite <= valor, "Saque acime do limite"
        self.__saldo -= valor

    def transferir(self, receptor, valor):
        self.sacar(valor)
        receptor.depositar(valor)
        