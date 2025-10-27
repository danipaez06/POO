class CuentaBancaria: 
    def __init__(self,  titular, saldo_inicial = 0):
        self._titular=titular #atributo protegido
        self.__saldo=saldo_inicial #atributo privado
        
    def depositar (self, monto):
        if monto > 0:
            self.__saldo += monto
            print (f"Depósito exitoso. Su saldo es: ${self.__saldo}")
        else:
            print ("El monto debe ser positivo, es decir, mayor a 0.")
    
    def retirar (self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print (f"El retiro ha sido exitoso. Su saldo es: ${self.__saldo}")
        else:
            print ("Fondos insuficientes o monto inválido.")
    
    def get_saldo (self):
        return self.__saldo
    def get_titular (self):
        return self._titular
    
Cuenta1 = CuentaBancaria ("Daniela", 12504320)
Cuenta1.depositar (1000)
Cuenta1.retirar (12504320)

print(f"Nombre del titular: {Cuenta1.get_titular()}")
print(f"El saldo de la cuenta es: ${Cuenta1.get_saldo()}")

