

class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def saque(self, valor):
        if(self.__pode_sacar):
            self.__saldo -= valor
        else:
            print("O valor {} ultrapassou o limite.".format(valor))

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel


    def deposito(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite

    @property
    def numero(self):
        return self.__numero

    @limite.setter
    def limite(self, limite): #pode ser def set_limite
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'
        
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
        
class Data:
    
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def formatada(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))

