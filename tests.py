from conta import Conta
from datas import Data

def test_extrato():
   conta = Conta(numero=1, titular="Robson", saldo=35) 
   assert conta.extrato == 35

def test_depositar():
    conta = Conta(numero=1, titular="Robson") 
    conta.depositar(100)
    assert conta.extrato == 100

def test_sacar():
    conta = Conta(numero=1, titular="Robson", saldo=100, limite=0) 
    conta.sacar(100)
    assert conta.extrato == 0

def test_formatada():
    data = Data(21, 11, 2010)
    assert data.formatada == "21/11/2010"

if __name__ == "__main__":
    test_extrato()
    test_depositar()
    test_sacar()
    test_formatada()
    conta = Conta(numero=1, titular="Robson", saldo=100, limite=0) 
    print(conta.__saldo )