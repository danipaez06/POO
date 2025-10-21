class CuentaBancaria:
    tasa_interes = 0.05
    
    def __init__(self, titular, balance):
        self.titular = titular
        self.balance = balance
        
    def ActTasa (self, NuevaTasa):
        self.tasa_interes = NuevaTasa
        
    def MostrarInfo (self):
        return f"\nEl titular de la cuenta es {self.titular}. \nSu balance actual es de ${self.balance} con una tasa de interés de ${self.tasa_interes}"
     
Cuenta1 = CuentaBancaria ("Daniela", 1000)
Cuenta2 = CuentaBancaria ("David", 5000)

Cuenta1.ActTasa(0.1)
Cuenta2.ActTasa(0.15)

print (Cuenta1.MostrarInfo())
print (Cuenta2.MostrarInfo())