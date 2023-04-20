class Conta:
    def __init__(self,nome, agencia, numero):
        self.nome = nome
        self.agencia = agencia
        self.numero = numero
        self.limite = 1000
        self.historico = []
        self.saldo = 0
    
    def verificar_saldo(self):
        return f"{self.nome} tem {self.saldo} real/reais de saldo disponível"
    
    def verificar_extrato(self):
        pass
    
    def sacar(self, valor):
        if self.saldo <= 0:
            print("Não há saldo suficiente para saque.")
        else:
            self.saldo -= valor
    def depositar(self, valor):
        if self.saldo > self.limite and valor >=0:
            print("Não pode, o valor maximo é R$1000,00")
        elif valor <=0:
            print("Não pode depositar valor negativo.")
        else:
            self.saldo += valor
    
    def fazer_transferencia(self):
        pass
    
    def encerrar(self):
        self.historico = []
        self.saldo = 0

Thais = Conta("Thais", 1234, 000000000)
Thais.depositar(300)
print(Thais.verificar_saldo())

Thais.sacar(400)
print(Thais.verificar_saldo())

Thais.depositar(100)
print(Thais.verificar_saldo())

Gabriel = Conta("Gabriel", 4321, 222222222)
Gabriel.depositar(1000)
print(Gabriel.verificar_saldo())

Thais.depositar(2000)
print(Thais.verificar_saldo())
