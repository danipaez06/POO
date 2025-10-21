class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo
    
    @property
    def saldo (self):
        print ("Accediendo al saldo...")
        return self.__saldo
    
    @saldo.setter
    def saldo (self, monto):
        if monto >= 0:
            print ("Modificando saldo...")
        else:
            print ("Error: El saldo no puede ser negativo.")

C1 = CuentaBancaria (1000)
print (C1.saldo)

C1.saldo = 1500
C1.saldo = -400