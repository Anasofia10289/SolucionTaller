helados = []  
helado={}
contadore_id = 1  

while True:
    print("\nGestión de Helados")
    print("1. Agregar un helado")
    print("2. Ver lista de helados")
    print("3. Modificar un helado")
    print("4. Eliminar un helado")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":  
        nombre = input("Ingrese el nombre del helado: ")
        descripcion = input("Ingrese la descripción del helado: ")
        cantidad = int(input("Ingresa la cantidad:"))
        precio = input("Ingrese el precio del helado: ")
        
        if precio.isdigit():
            precio = float(precio) 
            helado = {"id": contadore_id, "nombre": nombre, "descripcion": descripcion, "cantidad":cantidad ,"precio":precio}
            helados.append(helado)  
            contadore_id += 1
            print("Helado agregado correctamente.")
        else:
            print("Error: El precio debe ser un número.")
    
    elif opcion == "2":  
        if len(helado) == 0:  
            print("No hay helados registrados.")
        else:
            print("Lista de Helados:\n")
            for helado in helados:
                print(f"ID: {helado['id']}, Nombre: {helado['nombre']}, Descripción: {helado['descripcion']}, Cantidad:{helado['cantidad']} ,Precio: ${helado['precio']}")
               
    
    elif opcion == "3":  
        id_modificar = input("Ingrese el ID del helado a modificar: ")
        
        if id_modificar.isdigit():
            id_modificar = int(id_modificar)
            encontrado = False
            
            for helado in helados:
                if helado["id"] == id_modificar:
                    nuevo_nombre = input("Nuevo nombre: ") 
                    nueva_descripcion = input("Nueva descripción: ")
                    nueva_cantidad=input("Nueva cantidad: ")
                    nuevo_precio = input("Nuevo precio: ")
                    
                    if nuevo_nombre:
                        helado["nombre"] = nuevo_nombre
                    if nueva_descripcion:
                        helado["descripcion"] = nueva_descripcion
                    if nueva_cantidad:
                        helado["cantidad"]=int(nueva_cantidad)
                    if nuevo_precio.isdigit():
                        helado["precio"] = float(nuevo_precio)
                    
                    print("Helado modificado correctamente.")
                    encontrado = True
                    break
            
            if not encontrado:
                print("Error: No se encontró un helado con ese ID.")
        else:
            print("Error: El ID debe ser un número.")
    
    # Eliminar un helado
    elif opcion == "4":  
        id_eliminar = input("Ingrese el ID del helado a eliminar: ")
        
        if id_eliminar.isdigit():
            id_eliminar = int(id_eliminar)
            encontrado = False
            
            for helado in helados:
                if helado["id"] == id_eliminar:
                    # Error: variable incorrecta
                    helados.remove(helado)  
                    print("Helado eliminado correctamente.")
                    encontrado = True
                    break
            
            if not encontrado:
                print("Error: No se encontró un helado con ese ID.")
        else:
            print("Error: El ID debe ser un número.")
    
    elif opcion == "5":  # Salir
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente nuevamente.")
