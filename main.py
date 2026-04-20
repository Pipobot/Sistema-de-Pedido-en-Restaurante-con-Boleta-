import os
os.system ("cls")

# Sistema de Pedido en Restaurante (con Boleta)
# Contexto:
# Un restaurante necesita un sistema en Python que permita registrar pedidos, validando los datos ingresados
# y generando una boleta con el detalle de la compra.
compro_algo = False
nombre = ""
rut = ""
while True:
    print("==BIENVENIDO AL PIPO BAJON==")
    print("1.- Agregar pedido\n2.- Ver resumen\n3.-Descargar boleta\n4.-Salir")
    try:
        opcion = int(input("Digite su opcion: "))
        if opcion == 1:
            opcion_pedido = 0
            cantidad = 0
            print("Agregar pedido")
            while len(nombre) <= 0 or len(nombre) >= 20:
                nombre = input("Ingrese su nombre: ")
            while len(rut) < 8:
                rut = input("Ingrese su rut: ")
            print("==MENU==\n1.- Hamburguesa $5000\n2.- Pizza $8000\n3.- Ensalada $4000")
            while opcion_pedido <= 0 or opcion_pedido > 3:
                opcion_pedido = int(input("Ingrese opcion del producto: "))
            while cantidad <= 0:
                cantidad = int(input("Ingrese la cantidad de productos: "))
            if opcion_pedido == 1:
                producto = "Hamburguesa"
                monto_producto = 5000
            elif opcion_pedido == 2:
                producto = "Pizza"
                monto_producto = 8000
            elif opcion_pedido == 3:
                producto = "Ensalada"
                monto_producto = 4000
            compro_algo = True
            total = monto_producto * cantidad
        elif opcion == 2:
            print("==RESUMEN==")
            print(f"Cliente: {nombre}")
            print(f"Rut: {rut}")
            print(f"Producto: {producto}")
            print(f"Cantidad: {cantidad}")
            print(f"Total: ${total}")
            
        elif opcion == 3:
            print("Descargar boleta")
            with open("Boleta.txt", "w") as archivo:
                archivo.write("***BOLETA***\n")
                archivo.write(f"Cliente: {nombre}\n")
                archivo.write(f"Rut: {rut}\n")
                archivo.write(f"Producto: {producto}\n")
                archivo.write(f"Cantidad: {cantidad}\n")
                print(f"Total: ${total}\n")
            
        elif opcion == 4:
            print("Salir")
            break
        else:
            print("Opcion no valida! Intente nuevamente.")
    except:
        print("Error! Valor no valido, intente nuevamente.")