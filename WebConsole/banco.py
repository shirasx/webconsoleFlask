class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f'Olá {self.titular}. O seu saldo é de {self.saldo}'

    def deposito(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print(f"Ola {self.titular} O valor de {valor} foi depositado em sua conta!")
        else:
            print("Valor inválido.")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo = self.saldo - valor
            print(f"Ola {self.titular} Um saque de {valor} foi feito em sua conta!")
        else:
            print("Valor inválido ou saldo insuficiente.")


contas = []


raul = Conta("Raul", 0)
maria = Conta("Maria", 1000)
joao = Conta("João", 500)

contas.append(raul)
contas.append(maria)
contas.append(joao)


raul.deposito(10000)
maria.saque(1000)
joao.deposito(200)
raul.saque(3000)


for conta in contas:
    print(conta)
