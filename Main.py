class Main:
    pass

print("testando projeto")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("Joao", "123456789")
print(c1.nome, " e ",c1.telefone)
conta = Conta(c1.nome,6565,0)
print(conta.titular, " numero ",conta.numero, " saldo ",conta.saldoo)
