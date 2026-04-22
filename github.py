logistica = {
    "norte": ["pan", "arroz", "fideos", "jamon"],
    "centro": ["manzana", "pera", "uva", "naranja"],
    "sur": ["jugo", "agua", "bebida", "vino"]
}

pw_admin = "jefedejefes"
pw_centro = "centropro"
pw_repartidor = "delivery"


for intento in range(3):
    acceso = input("Ingrese la contraseña de administrador: ")
    if acceso == pw_admin:
        print("Ingreso concedido\n")
        break
    else:
        print(f"Ingreso denegado. Intentos restantes: {2 - intento}")
else:
    print("Demasiados intentos fallidos.")
    exit()

print("Bienvenido a la distribuidora")
for sector, productos in logistica.items():
    print(f"Sector {sector}: {', '.join(productos)}")

seleccion = input("¿A qué sector desea ingresar?: ").lower()

match seleccion:
    case "norte":
        print("Bienvenido al sector norte.")
    case "centro":
        p_centro = input("Ingresa contraseña para esta sección: ")
        if p_centro == pw_centro:
            print("Acceso concedido al sector centro.")
        else:
            print("Contraseña incorrecta.")
            exit()
    case "sur":
        print("Bienvenido al sector sur.")
    case _:
        print("Ubicación no encontrada.")
        exit()

if seleccion in logistica:
    d = input("Ingrese contraseña de repartidor para modificar inventario: ")
    
    if d == pw_repartidor:
        print("Contraseña correcta")
        
        while True:
            nuevo_prod = input(f"Ingrese producto para {seleccion} (o 'fin' para terminar): ")
            if nuevo_prod.lower() == "fin":
                break
            logistica[seleccion].append(nuevo_prod)
            print(f"'{nuevo_prod}' agregado.")
    else:
        print("Contraseña de repartidor incorrecta.")

print("INVENTARIO ACTUALIZADO")
for sector, productos in logistica.items():
    print(f"{sector.capitalize()}: {', '.join(productos)}")

print("mision cumplida camión vacío")
