class Tienda:
    def __init__(self, nombre_tienda, nombre_producto, precio_base, descuento, precio_final):
        self.nom_t=nombre_tienda
        self.nom_p=nombre_producto
        self.pre_n=precio_base
        self.desc=descuento
        self.pre_f=precio_final

    producto1 = Tienda ("Supermark", "Queso", 95)
    producto2 = Tienda ("Supermark", "Leche", 105)
    print(producto1.nom_t, producto1.nom_p, producto1.pre_n, producto1.desc)
    print(producto2.nom_t, producto2.nom_p, producto2.pre_n, producto2.desc)  