class CuentaBancaria: 
    def __init__(self,  titular, saldo_inicial = 0):
        self._titular=titular #atributo protegido
        self._saldo=saldo_inicial #atributo protegido
        self._activa=True
    
    @property
    
    def saldo (self):
        """Getter automatico se usa como un atributo"""
        return self._saldo
    
    @property
    
    def titular (self):
        return self._titular
    
    @titular.setter
    
    def titular (self, valor):
        if len(valor) > 0:
            self._titular = valor
        else:
            raise ValueError ("Titular no puede estar vacío.")
        
    @property
    
    def esta_activa (self):
        return self._activa
    
Cuenta1 = CuentaBancaria ("Daniela", 12504320)
Cuenta2 = CuentaBancaria ("David")

print("\n---------- CUENTA 1 ----------")
print(Cuenta1.titular)
print(Cuenta1.saldo)
print(Cuenta1.esta_activa)

print("\n---------- CUENTA 2 ----------")
print(Cuenta2.titular)
print(Cuenta2.saldo)
print(Cuenta2.esta_activa)