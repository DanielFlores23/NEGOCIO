menu = ["pollo frito", "sopa de frijoles", "sopa marinera"]

def imprimir_menu():
	print("1 Lista Menu")
	print("2 Agregar Pedido")
	print("3 Imprimir Pedido")
	print("4 Salir")
	valor = input("Ingrese el numero de la accion que desea realizar")
	

def Lista_menu():
	print()
	PRINT("Listado de Menu")
	for producto in range(len(menus)):
		print("{0} {1}".format producto.menus[producto])

def agregar_pedido():
	print()
	print("Creando un pedido")
	mesa = input("Numero de mesa")
	producto = input("Nombre de platillo")
	pedidos.append("Meza No. {0} Platollo {1}"_fornat(mesa, producto)

def imprimir_pedidos()
	if pedidos:
		for pedido in pedidos:
			print(pedido)

	else:
		print("No hay pedidos ingresados")

salir = True

while continuar:
	#_retornado = valor Retornado
	v_retornado = imprimir_menu()
	if int(v_retornado) == 1:
		for producto in producto:
			print(producto)
	elif int(v_retornado) == 2:
		producto = []
	elif int(v_retornado) == 3:
		valor = input("Ingrese el pedido a agregar")
		producto.append(valor)
	elif int(v_retornado) == 4:
		continuar = False
	else:
		print("Opcion no controlada")

