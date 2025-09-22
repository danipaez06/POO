class Tienda2:
    def __init__(self, nombre_tienda, nombre_producto, precio_base, descuento):
        self.nom_t=nombre_tienda
        self.nom_p=nombre_producto
        self.pre_b=precio_base
        self.desc=descuento
        self.precio_final = 0
        
    #Convertir a porcentaje segun descuento
        descuento_decimal = self.desc/100 
    #Operacion del precio con el descuento
        self.precio_final = self.pre_b * (1- descuento_decimal)
    
    #Condicionales
        if self.pre_b > 200:
            print("Esta adquiriendo un producto de alto valor. Se aplicara un descuento del 15% ")
            self.precio_final=self.precio_final*0.85
        elif self.pre_b > 100 and self.pre_b < 199:
                print("Esta adquiriendo un mediano de alto valor. Se aplicara un descuento del 10% ")
                self.precio_final=self.precio_final*0.90
        elif self.pre_b < 99:
                    print("Esta adquiriendo un bajo de alto valor. Se aplicara un descuento del 5% ")
                    self.precio_final=self.precio_final*0.95
    
    def Show(self):
        print("\n---- DETALLES DEL PRODUCTO ---")
        print(f" Tienda: {self.nom_t}")
        print(f" Producto: {self.nom_p}")
        print(f" Precio Base: {self.pre_b}")
        print(f" Descuento aplicado: {self.desc}%")
        print(f" Total: {self.precio_final}")
        print("------------------------------\n")
    
producto1 = Tienda2 ("Supermark", "Queso", 300, 15)
producto2 = Tienda2 ("Supermark", "Leche", 150, 10)
producto3 = Tienda2 ("Supermark", "Pan", 50, 5)

producto1.Show()
producto2.Show()
producto3.Show()