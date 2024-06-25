#crear una app que permita registrar productos de una tienda de abarrotes
#los requisitos son:

#crear archivo con formato csv
#ingresar productos, codigo de barra, nombre, marca, precio, stock
#listar productos
#eliminar producto
#modificar stock actual

#usar funciones, listas y librerias vistas en clases
#crear repositorio en github y guardar los cambios

# Crear una app, que permita registrar productos de una tienda de abarrotes
# Los requisitos son:
# crear menu con las siguientes opciones:
# 
# Crear archivo con formato csv
# Ingresar productos (codigo de barra, nombre, marca, precio, stock)
# Listar productos
# Eliminar producto
# Modificar stock actual
# 
# Usar funciones, listas y librerias vistas en clases.
# Crear repositorio en github y guardar los cambios


import csv
import os

def crearArchivo():
    with open('RegistroDeProducto.csv', 'w', newline='') as doc:
        csv.writer(doc)
        print("==========> Archivo creado")

def Producto():
    print("*******************************************")
    print("|==========  Registrar Ingreso  ==========|")
    print("*******************************************")
    print("Ingrese los siguientes datos:")
    codigo_barra = input('Codigo de Barra: ')
    if not codigo_barra.isdigit():
        print('ingrese un código valido')
        return
        
    nombre = input('Nombre del producto: ')
    if len(nombre.strip()) == 0:
        print('---ERROR: El nombre no fue especificado ')
        return
    
    marca = input('Marca del producto: ')
    if len(marca.strip()) == 0:
        print('---ERROR: La marca no fue especificada ')
        return
    precio = input('Precio del producto: ')
    if not precio.isdigit():
        print('---ERROR: El precio no es un valor numerico ')
        return
    stock = input('Stock del producto: ')
    if not stock.isdigit():
        print('---ERROR: El stock no es un valor numerico ')
        return
    with open ('RegistroDeProducto.csv', 'a', newline= '') as doc:
        writer = csv.writer(doc)
        writer.writerow([codigo_barra, nombre, marca, precio, stock])
        print('Producto añadido con exito')
    
def listarProductos():
    with open ('RegistroDeProducto.csv', 'r', newline= '') as doc:
        reader = csv.reader(doc)
        print("==========================================")
        print("========== Listado de Productos ==========")
        print("==========================================")
        for row in reader:
            print(row)

def eliminar_producto():
    print("=======================================")
    print("|==========  Eliminar Producto  ==========|")
    print("=======================================")
    codigo_barra = input('Ingrese el código de barra del producto a eliminar: ')
    producto = []
    with open ('RegistroDeProducto.csv', 'r', newline= '') as doc:
        reader = csv.reader(doc)
        for row in reader:
            if row[0] == codigo_barra:
                print("Producto encontrado")
                print("¿Desea eliminar el producto? (si/no): ")
                respuesta = input()
                if respuesta.lower() == 'si':
                    print("Producto eliminado")
                    return
                if not respuesta.lower() == 'no':
                    print("No se elimino el producto")

def modificar_stock():
    print("=======================================")
    print("|==========  Actualizar Stock  ==========|")
    print("=======================================")
    codigo_barra = input('Ingrese el código de barra del producto a actualizar: ')
    producto = []
    with open ('RegistroDeProducto.csv', 'r', newline= '') as doc:
        reader = csv.reader(doc)
        for row in reader:
            if row[0] == codigo_barra:
                print("Producto encontrado")
                stock_act = int(input('Ingrese el nuevo stock: '))
                row[4] = stock_act
                print("Stock actualizado")
                
opcion = ""
while opcion != "6":
    os.system("cls")
    print("******* Menú *******")
    print("1.- Crear archivo")
    print("2.- Ingresar producto")
    print("3.- Listar producto")
    print("4.- Eliminar producto")
    print("5.- Modificar Stock")
    print("6.- Salir")
    opcion = input("Ingrese opción: ")

    if opcion not in ("1","2","3","4","5","6"):
        print("La opción ingresada no es válida")    

    if opcion == "6":
        break

    if opcion == "1":
        crearArchivo()
    if opcion == "2":
        Producto()
    if opcion == "3":
        listarProductos()
    if opcion == "4":
        eliminar_producto()
    if opcion == "5":
        modificar_stock()

    input("Presionen enter para continuar....")