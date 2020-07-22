# alimentos[0][1]


# Inicializando variables globales -alimentos y bebidas- fomadas en un diccionario .
alimentos ={"plato 1": {"name":"Pizza","price":11.99,"prest":'paquete'},
            "plato 2": {"name":"Hamburguesa","price":25.99,"prest":'preparacion'},
            "plato 3": {"name":"Cofuta","price":6.99,"prest":'paquete'},
            "plato 4": {"name":"Donas","price":2.99,"prest":'paquete'}

    }
    
    
    
bebidas = {"bebida 1": {"name":"Ron","price":6.99,"prest":'grande'},
           "bebida 2": {"name":"Coca Cola","price":2.99,"prest":'mediano'},
           "bebida 3": {"name":"Cerveza","price":3.99,"prest":'grande'},
           "bebida 4": {"name":"Limonada","price":2.75,"prest": 'grande'},
           "bebida 5": {"name":"sprite","price":2.35,"prest":''}

    }

    

combos = { "combo 1" : {"name" : "Hamburguesa & Refresco", "price": 15.99},
           "combo 2" : {"name":"Pizza & Refresco", "price": 21.55},
           "combo 3" : {"name": "nuggets & fries", 'price': 12.99},
           "combo 4" : {"name": "helado & brownie", 'price':15.99}

    }





# Funcion que permite mostrar solo las comidas de forma enumerada.
def show_food(alimentos):
    for i,e in enumerate(sorted(alimentos)):
        print(f"{i+1}. Nombre: {alimentos[e]['name']}\n\tprecio: {alimentos[e]['price']}\n\tPresentacion: {alimentos[e]['prest']}")
   


# similar a la funcion anterior, permite mostrar unicamente las bebidas de manera enumerada.
def show_drinks(bebidas):

    for i,e in enumerate(sorted(bebidas)):
        print(f"{i+1}. Nombre: {bebidas[e]['name']}\n\tprecio: {bebidas[e]['price']}\n\tPresentacion: {bebidas[e]['prest']}")


#Funcion que permite eliminar tanto alimentos como bebidas indicando el nombre tal cual se encuentra en El Database de "alimentos" y "bebidas".
#Es decir o bien plato 1 o bebida 1, etc.
def elim(alimentos,bebidas):
    opt3 = int(input("Ingrese El numero correspondiente a el tipo de producto que desea eliminar.\n1. Platos\n2. Bebidas "))
    #validando el input, si no es igual a 1 o 2 arroja error hasta que se introduzca una opcion correcta.
    while opt3 != 1 and opt3 != 2:
        opt3 = int(input("Ingrese Una Opcion valida: "))
        #Si pasa la validacion contiua el programa pidiendo los datos a corde a lo que se quiera eliminar.
    if opt3 == 1:
        show_food(alimentos)
        del_alimt = str(input("Ingrese El Plato del Elemento A Eliminar (EJ. Plato 1): "))
        del alimentos[del_alimt]
        print()
        print("--" *30)
        #retorna la funcion mostrar alimentos para que se verifique que si se elimino el plato
        show_food(alimentos)
    elif opt3 == 2:
        show_drinks(bebidas)
        del_drink = str(input("Ingrese LA Bebida a eliminar (EJ..Bebida 1): "))
        del bebidas[del_drink]
        print("--" *30)
        #retorna la funcion mostrar bebidas para que se verifique que si se elimino la bebida
        show_drinks(bebidas)
    




    
    
# se define la funciom para agregar tanto alimento como bebidas

def adt(alimentos,bebidas):
    print()
    print("Muy bien!\n1.Agregar Alimento. \n2.Agregar Bebida.")
    #se le pregunta el usuario para que este ingrese por teclado la opcion que desea realizar y se procede a validar
    opt2 = int(input("Ingrese La Opcion Que Desea Realizar:"))
    
    while opt2 != 1 and opt2 != 2:
        opt2 = int(input("Error Una opcion valida: "))
        #si pasa la validacion se procede a realizar la opcion que se selecciona.
    if opt2 == 1:
#se inician 3 variables que hacen referencia a cada unos de los keys de los diccionarios, donde el valor a ingresar corresponde al los values.
        prest= str(input("paquete o preparacion:"))
        name = str(input("Ingrese El Nombre Del Producto A Agregar:"))
        price = float(input("Ingrese El Precio Del Producto: "))
        print("Por Favor, Espere")
        alimentos[f"plato {len(alimentos)+1}"] = {"name":name,"price":price,"prest": prest}
        #imprime mensaje de que se agrego correctamente

        print("Alimento Agregado Exitosamente!")
        #print(alimentos)

    elif opt2 == 2:
        #se inician 3 variables que hacen referencia a cada unos de los keys de los diccionarios, donde el valor a ingresar corresponde al los values.

        present = str(input("Gande / Mediano / Pequeño"))
        name = str(input("Ingrese El Nombre Del Producto A Agregar:"))
        price = float(input("Ingrese El Precio Del Producto: "))
        print("Por Favor, Espere..") 
        bebidas[f"bebida {len(bebida)+1}"] = {"name":name,"price":price, "prest": prest}
        #imprime mensaje de que se agrego correctamente
        print("Alimento Agregado Exitosamente!")
    

def mod(alimentos,bebidas):
    print(("Indique la opcion que desea realizar: ").title())
    modd = int(input("1.Alimentos\n2.Bebidas\n//> "))
    while modd != 1 and modd != 2:
        modd = int(input("Error, Ingrese UN Caracter numerico valio: "))
    if modd == 1:
        print("--"*25)
        show_food(alimentos)
        print("--"*25)
        modda = str(input("Ingrese el plato que desea modificar (Ej.. plato 1): "))
        print("Que desea modiciar:\n1. Presentacion\n2.Nombre\n3.precio")
        modi = int(input(">>"))
        while modi != 1 and modi != 2 and modi != 3:
            modi = int(input("Ingrese un valor valido: "))
        if modi == 1:
            modi_prest = int(input("Ingrese El modo de presenacion (1.Paquete / 2.preparacion: "))
            while modi_prest != 1 and modi_prest != 2:
                modi_prest = int(input("Ingrese El modo de presenacion valido (1.Paquete / 2.preparacion: "))
            if modi_prest == 1:
                alimentos[modda]["prest"] = "paquete"
                show_food(alimentos)

            elif modi_prest == 2:
                alimentos[modda]["prest"] = "preparacion"
                print("Cambio realizado con exito")
                print()
                print('--'*25)
                show_food(alimentos)
        elif modi == 2:
            modi_name = str(input("Ingrese El nuevo nombre del plato: "))
            while modi_name == int:
                modi_name = str(input("Error Ingrese un valor no numerico: "))
            
            alimentos[modda]["name"] = modi_name 
            
            print("Cambio realizado con exito")
            print()
            print('--'*25)
            show_food(alimentos)
        elif modi == 3:
            modi_price = float(input("Ingrese El nuevo preecio del plato:"))
            while modi_price == str:
                modi_price = float(input("Error Ingrese un valor  numerico: "))

            alimentos[modda]["price"] = modi_price
            print("Cambio realizado con exito")
            print()
            print('--'*25)
            show_food(alimentos)
    elif modd == 2:

        print("--"*25)
        show_drinks(bebidas)
        print("--"*25)
        modda = str(input("Ingrese la bebida que desea modificar (Ej.. bebida 1): "))
        print("Que desea modiciar:\n1. Presentacion\n2.Nombre\n3.precio")
        modi = int(input(">>"))
        while modi != 1 and modi != 2 and modi != 3:
            modi = int(input("Ingrese un valor valido: "))
        if modi == 1:
            modi_prest = int(input("Ingrese El modo de presenacion (1.Pequeño / 2.Mediano / 3.Grande: "))
            while modi_prest != 1 and modi_prest != 2 and modi_prest != 3:
                modi_prest = int(input("Ingrese El modo de presenacion valido (1.Pequeño / 2.Mediano / 3.Grande: "))
            if modi_prest == 1:
                bebidas[modda]["prest"] = "Pequeño"
                show_drinks(bebidas)

            elif modi_prest == 2:
                bebidas[modda]["prest"] = "Mediano"
                print("Cambio realizado con exito")
                print()
                print('--'*25)
                show_drinks(bebidas)
            elif modi_prest == 3:
                bebidas[modda]["prest"] = "Grande"
                print("Cambio realizado con exito")
                print()
                print('--'*25)
                show_drinks(bebidas)

        elif modi == 2:
            modi_name = str(input("Ingrese El nuevo nombre de la bebida: "))
            while modi_name == int:
                modi_name = str(input("Error Ingrese un valor no numerico: "))
            
            bebidas[modda]["name"] = modi_name 
            
            print("Cambio realizado con exito")
            print()
            print('--'*25)
            show_drinks(bebidas)
        elif modi == 3:
            modi_price = float(input("Ingrese El nuevo precio de la bebida:"))
            while modi_price == str:
                modi_price = float(input("Error Ingrese un valor  numerico: "))

            bebidas[modda]["price"] = modi_price
            print("Cambio realizado con exito")
            print()
            print('--'*25)
            show_drinks(bebidas)
    
def show_combos(combos):
    for i,e in enumerate(sorted(combos)):
        print(f"{i+1}. Nombre: {combos[e]['name']}\n\tprecio: {combos[e]['price']}")

def del_combo(combos):
    show_combos(combos)
    del_comb = str(input("Ingrese El Combo del Elemento A Eliminar (EJ. Combo 1): "))
    
    
    
    del combos[del_comb]
    print()
    print("--" *30)
    #retorna la funcion mostrar combos para que se verifique que si se elimino el combo.
    show_combos(combos)

def agg_combos(combos):

    name_1= str(input("Ingrese El Nombre Del primer Producto:"))
    name_2 = str(input("Ingrese El Nombre Del Segundo Producto A Agregar:"))
    price = float(input("Ingrese El Precio Del combo: "))
    name_c = f"{name_1} & {name_2}"
    print("Por Favor, Espere")
    combos[f"combo {len(combos)+1}"] = {"name": name_c,"price": (price*0.16)+price }
        
    #imprime mensaje de que se agrego correctamente
    print("combo Agregado Exitosamente!")
    #devuelve el diccionario combos para comprobar que efectivamente se agrego el combo

        


    

def menu_combos(combos):
    
    print("""
    -----------------------------------
    Bienvenido A Nuestro Menu De Combos
    -----------------------------------
    """)
    dec = int(input("1. Agregar Combo\n2. Mostrar Combo\n3. Eliminar combo\n>> "))
    while dec != 1 and dec != 2 and dec != 3:
        dec = int(input("Error Ingrese un valor Numerico Valido: "))
    if dec == 1:
        agg_combos(combos)
        
    elif dec == 2:
        show_combos(combos)
    elif dec == 3:
        del_combo(combos)

    

def search(alimentos,bebidas,combos):
    print("---BUSCADOR DE SAMAN CARIBEAN---")
    se = int(input("1.Alimentos\n2.Bebidas\n3.Combos\n/>> "))
    while se != 1 and se != 2 and se != 3:
        se = int(input("Error. Intentelo De Nuevo, seleccione Una Opcion Valida: "))
    if se == 1:
        stt = str(input("Ingrese El nombre del plato que desea buscar (EJ.. Plato 1): "))
        
        if stt in alimentos:
            print('\n')
            print(f"Se ha encontrado Lo siguiente: {alimentos[stt]['name'] } con un precio de ${alimentos[stt]['price']}")
        else:
            print('--'*25)
            print("No se ha encontrado nada relacionado.")
    elif se == 2:
        st1 = str(input("Ingrese El nombre de la bebida que desea buscar (EJ.. bebida 1): "))

        if st1 in bebidas:
            print('\n')
            print(f"Se ha encontrado Lo siguiente: {bebidas[st1]['name'] } con un precio de ${bebidas[st1]['price']}")
        else:
            print('--'*25)
            print("No se ha encontrado nada relacionado.")
    elif se == 3:
        st2 = str(input("Ingrese El nombre del combo que desea buscar (EJ.. combo 1): "))

        if st2 in combos:
            print('\n')
            print(f"Se ha encontrado Lo siguiente: {combos[st2]['name'] } con un precio de ${combos[st2]['price']}")
        else:
            print('--'*25)
            print("No se ha encontrado nada relacionado.")


            

        
        
        
        
        


msg1 = """
--------------------------------------------------------
Bienvenido al sistema de restaurante de Saman Caribbean
--------------------------------------------------------
"""
#funcion que sirve para presentar el menu desplegable
#se imprime las posbiles opciones que tiene el usuario para seleccionar
#y se validan en dado caso de que el usuario la seleccione

def menu(alimentos,bebidas):
    print(msg1)
    check = True
    print(("1.Agregar Platos.\n2.Mostrar Platos.\n3.Modificar Productos.\n4.Eliminar Platos\n5.Combos.\n6. buscar\n7.Salir").title())
    opt = int(input(("Ingrese una de las opciones a realizar: ").title()))
    #se valida que el parametro ingresado este dentro del rango que se requiere de lo contrario no sale del bucle
    while check == True:

        while opt != 1 and opt != 2 and opt !=3 and opt != 4 and opt != 5 and opt != 6 and opt != 7:
            opt = int(input(("Error. Ingrese una de las opciones a realizar: ").title()))
        

        if opt == 1:
            print()
            #se llama la funcion adt
                
            adt(alimentos,bebidas)
            print()
            print((msg1).title())
            print(("1.Agregar Platos.\n2.Mostrar Platos.\n3.Modificar Productos.\n4.Eliminar Platos\n5.Combos.\n6. buscar\n7.Salir").title())
            print()
            opt = int(input(("Ingrese una de las opciones a realizar: ").title()))
                
        elif opt == 2:
            print()
            #llamado a la funcion show_food
            show_food(alimentos)
            print(''''
            ---------
            Bebidas
            ---------
            ''')
            # a su vez se llama a la funcion show_drinks
            show_drinks(bebidas)
            print()
            #se llama otra vez a la variable opt para reiniciar el ciclo y volver asi otra vez al menu
            print((msg1).title())
            print(("1.Agregar Platos.\n2.Mostrar Platos.\n3.Modificar Productos.\n4.Eliminar Platos\n5.Combos.\n6. buscar\n7.Salir").title())
            print()
            opt = int(input(("Ingrese una de las opciones a realizar: ").title()))
        elif opt == 3:
            print("--"*25)
            mod(alimentos,bebidas)
            print()
            print((msg1).title())
            print(("1.Agregar Platos.\n2.Mostrar Platos.\n3.Modificar Productos.\n4.Eliminar Platos\n5.Combos.\n6. buscar\n7.Salir").title())
            print()
            opt = int(input(("Ingrese una de las opciones a realizar: ").title()))
        elif opt == 4:
            print()
                
            elim(alimentos,bebidas) 
            print()
            #se llama otra vez a la variable opt para reiniciar el ciclo y volver asi otra vez al menu
            print((msg1).title())
            print(("1.Agregar Platos.\n2.Mostrar Platos.\n3.Modificar Productos.\n4.Eliminar Platos\n5.Combos.\n6. buscar\n7.Salir").title())
            print()
            opt = int(input(("Ingrese una de las opciones a realizar: ").title()))
        elif opt == 5:
            print()
            menu_combos(combos)
            print()
            print((msg1).title())
            #se llama otra vez a la variable opt para reiniciar el ciclo y volver asi otra vez al menu
            print(("1.Agregar Platos.\n2.Mostrar Platos.\n3.Modificar Productos.\n4.Eliminar Platos\n5.Combos.\n6. buscar\n7.Salir").title())
            print()
            opt = int(input(("Ingrese una de las opciones a realizar: ").title()))
            
        elif opt == 6:
            print()
            search(alimentos,bebidas,combos)
            print()
            print((msg1).title())
            #se llama otra vez a la variable opt para reiniciar el ciclo y volver asi otra vez al menu
            print(("1.Agregar Platos.\n2.Mostrar Platos.\n3.Modificar Productos.\n4.Eliminar Platos\n5.Combos.\n6. buscar\n7.Salir").title())
            print()
            opt = int(input(("Ingrese una de las opciones a realizar: ").title()))


        elif opt == 7:
            print('---'*10)
            print("Nos Vemos Pronto")
            break
            
            
            


#def main():
    

    #print(msg1)
    #menu(alimentos,bebidas)
    
    
    



#main()