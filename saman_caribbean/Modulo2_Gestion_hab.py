# SE LLAMA EL IMPORT PARA HACER UN REQUEST A LA API Y OBTENER LOS DATOS DE LOS BARCOS
import requests

r = requests.get("https://saman-caribbean.vercel.app/api/cruise-ships")

d = '---'*100
dic = r.json()

# habs de barco 1                  2 4 8
# { simple  [4,10]
#   premium [3,9]
#    vip    [1,6]
# }

# habs de barco 2                  2 4 8  
# { simple  [6,10] piso 1
#   premium [4,8] piso 2 
#    vip    [2,4] piso 3
# }
 # habs de barco 3                     3 5 12
# { simple  [6,8] piso 1
#   premium [4,6] piso 2 
#    vip    [4,2] piso 3
# }

 # habs de barco 4                       3 5 10
# { simple  [4,12] piso 1
#   premium [3,7] piso 2 
#    vip    [2,4] piso 3
# }

    


def form(count):
    name = str(input("Ingrese Su nombre: "))
    
    dni = int(input("Ingrese El Numero De su numero De Identidad: "))
    
    age = int(input("Ingrese Su edad: "))
    people = int(input("Desea Agregar a otra persona? (1. Si 2. No)"))
    while people != 1 and people != 2:
        people = int(input('Error. Ingrese Una opcion valida: '))
    if people == 1:
        print(count - 1)
        return count
        if count == 0:
            print("No Puede Seguir agregando Personas")
        name_1 = str(input("Ingrese Su nombre: "))
    
        dni_2 = int(input("Ingrese El Numero De su numero De Identidad: "))
    
        age_2 = int(input("Ingrese Su edad: "))

        people1 = int(input("Desea Agregar a otra persona? (1. Si 2. No)"))

        
    elif people == 2:
        print("Muy Bien!")

    



 #Se define una funcion para vender las habitaciones o bien segun el barco o bien segun el destino
 # Luego dependiendo de la opcion selecionada se dan o bien los nombres de los barcos o los destino para luego preguntar que timpo de habitacion se desea
 # para luego proceder con el registro del cliente     
def sell_habs():
    opt = int(input("Saman Caribbean Posee Varias habitaciones segun el barco o el destino. Como deseas realizar tu busqueda?\n1.Segun el Barco\n2.Segun El destino\n>> "))
    while opt != 1 and opt != 2:
        opt = int(input("Error. Ingrese Un  caracter valido.\n Como deseas realizar tu busqueda?\n1.Segun el Barco\n2.Segun El destino\n>> "))
    if opt == 1:
        print('--'*25)
        print(f"Segun El barco possemos lo siguiente:\n1.{dic[0]['name']}\n2.{dic[1]['name']}\n3.{dic[2]['name']}\n4.{dic[3]['name']}")
        boat_name = int(input("Ingrese El Numero Correspondiente A su Seleccion: "))
        while boat_name != 1 and boat_name != 2 and boat_name != 3 and boat_name != 4:
            boat_name = int(input("Error. Ingrese Un Caracter Valido: "))
        if boat_name == 1:
            print("--"*25)
            print(f"Para el barco {dic[0]['name']} tenemos las siguientes habitaciones:\n1. sencilla >> capacidad {dic[0]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[0]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[0]['capacity']['vip']} personas.")
            hab_selected = int(input("Ingrese El caracter correspondiente a su seleccion: "))
            while hab_selected != 1 and hab_selected != 2 and hab_selected !=3:
                hab_selected = int(input(f"Error. Ingrese Un caracter valido.\n1. sencilla >> capacidad {dic[0]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[0]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[0]['capacity']['vip']} personas."))
            if hab_selected == 1:
                print('\n')
                print(f"Muy Bien haz seleccionado la habitacion simple con capacidad para {dic[0]['capacity']['simple']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 2 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[0]['cost']['simple']}
                    ♦ Impuestos % 16 :  $ {(dic[0]['cost']['simple'])*0.16}
                    ♦ Total : $ {(dic[0]['cost']['simple'])+(dic[0]['cost']['simple'])*0.16}


                    '''
                    print(msgf)
            elif hab_selected == 2:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion premium con capacidad para {dic[0]['capacity']['premium']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 4 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[0]['cost']['premium']}
                    ♦ Impuestos % 16 :  $ {(dic[0]['cost']['premium'])*0.16}
                    ♦ Total : $ {(dic[0]['cost']['premium'])+(dic[0]['cost']['premium'])*0.16}


                    '''
                    print(msgf)
            elif hab_selected == 3:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion vip con capacidad para {dic[0]['capacity']['vip']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 8 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[0]['cost']['vip']}
                    ♦ Impuestos % 16 :  $ {(dic[0]['cost']['vip'])*0.16}
                    ♦ Total : $ {(dic[0]['cost']['vip'])+(dic[0]['cost']['vip'])*0.16}


                    '''
                    print(msgf)

        elif boat_name == 2:
            print("--"*25)
            print(f"Para el barco {dic[1]['name']} tenemos las siguientes habitaciones:\n1. sencilla >> capacidad {dic[1]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[1]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[1]['capacity']['vip']} personas.")
            hab_selected = int(input("Ingrese El caracter correspondiente a su seleccion: "))
            while hab_selected != 1 and hab_selected != 2 and hab_selected !=3:
                hab_selected = int(input(f"Error. Ingrese Un caracter valido.\n1. sencilla >> capacidad {dic[1]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[1]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[1]['capacity']['vip']} personas."))
            if hab_selected == 1:
                print('\n')
                print(f"Muy Bien haz seleccionado la habitacion simple con capacidad para {dic[1]['capacity']['simple']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 2 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[1]['cost']['simple']}
                    ♦ Impuestos % 16 :  $ {(dic[1]['cost']['simple'])*0.16}
                    ♦ Total : $ {(dic[1]['cost']['simple'])+(dic[1]['cost']['simple'])*0.16}


                    '''
                    print(msgf)
            elif hab_selected == 2:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion premium con capacidad para {dic[1]['capacity']['premium']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 4 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[1]['cost']['premium']}
                    ♦ Impuestos % 16 :  $ {(dic[1]['cost']['simple'])*0.16}
                    ♦ Total : $ {(dic[1]['cost']['premium'])+(dic[1]['cost']['premium'])*0.16}


                    '''
                    print(msgf)
            elif hab_selected == 3:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion vip con capacidad para {dic[1]['capacity']['vip']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 8 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[1]['cost']['vip']}
                    ♦ Impuestos % 16 :  $ {(dic[1]['cost']['vip'])*0.16}
                    ♦ Total : $ {(dic[1]['cost']['vip'])+(dic[1]['cost']['vip'])*0.16}


                    '''
                    print(msgf)
        elif boat_name == 3:
            print("--"*25)
            print(f"Para el barco {dic[2]['name']} tenemos las siguientes habitaciones:\n1. sencilla >> capacidad {dic[2]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[2]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[2]['capacity']['vip']} personas.")
            hab_selected = int(input("Ingrese El caracter correspondiente a su seleccion: "))
            while hab_selected != 1 and hab_selected != 2 and hab_selected !=3:
                hab_selected = int(input(f"Error. Ingrese Un caracter valido.\n1. sencilla >> capacidad {dic[2]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[2]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[2]['capacity']['vip']} personas."))
            if hab_selected == 1:
                print('\n')
                print(f"Muy Bien haz seleccionado la habitacion simple con capacidad para {dic[2]['capacity']['simple']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 3 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[2]['cost']['simple']}
                    ♦ Impuestos % 16 :  $ {(dic[2]['cost']['simple'])*0.16}
                    ♦ Total : $ {(dic[2]['cost']['simple'])+(dic[2]['cost']['simple'])*0.16}


                    '''
                    print(msgf)
            elif hab_selected == 2:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion premium con capacidad para {dic[2]['capacity']['premium']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 5 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[2]['cost']['premium']}
                    ♦ Impuestos % 16 :  $ {(dic[2]['cost']['premium'])*0.16}
                    ♦ Total : $ {(dic[2]['cost']['premium'])+(dic[2]['cost']['premium'])*0.16}


                    '''
                    print(msgf)
            elif hab_selected == 3:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion vip con capacidad para {dic[2]['capacity']['vip']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 12 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[2]['cost']['vip']}
                    ♦ Impuestos % 16 :  $ {(dic[2]['cost']['vip'])*0.16}
                    ♦ Total : $ {(dic[2]['cost']['vip'])+(dic[2]['cost']['vip'])*0.16}


                    '''
                    print(msgf)
        elif boat_name == 4:
            print("--"*25)
            print(f"Para el barco {dic[3]['name']} tenemos las siguientes habitaciones:\n1. sencilla >> capacidad {dic[3]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[3]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[3]['capacity']['vip']} personas.")
            hab_selected = int(input("Ingrese El caracter correspondiente a su seleccion: "))
            while hab_selected != 1 and hab_selected != 2 and hab_selected !=3:
                hab_selected = int(input(f"Error. Ingrese Un caracter valido.\n1. sencilla >> capacidad {dic[3]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[3]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[3]['capacity']['vip']} personas."))
            if hab_selected == 1:
                print('\n')
                print(f"Muy Bien haz seleccionado la habitacion simple con capacidad para {dic[3]['capacity']['simple']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 3 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[3]['cost']['simple']}
                    ♦ Impuestos % 16 :  $ {(dic[3]['cost']['simple'])*0.16}
                    ♦ Total : $ {(dic[3]['cost']['simple'])+(dic[3]['cost']['simple'])*0.16}


                    '''
                    print(msgf)
            elif hab_selected == 2:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion premium con capacidad para {dic[3]['capacity']['premium']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 5 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[3]['cost']['premium']}
                    ♦ Impuestos % 16 :  $ {(dic[3]['cost']['premium'])*0.16}
                    ♦ Total : $ {(dic[3]['cost']['premium'])+(dic[3]['cost']['premium'])*0.16}


                    '''
                    print(msgf)
            elif hab_selected == 3:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion vip con capacidad para {dic[3]['capacity']['vip']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 10 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[3]['cost']['vip']}
                    ♦ Impuestos % 16 :  $ {(dic[3]['cost']['vip'])*0.16}
                    ♦ Total : $ {(dic[3]['cost']['vip'])+(dic[3]['cost']['vip'])*0.16}


                    '''
                    print(msgf)
    elif opt == 2:
        print('--'*25)
        print(f"Segun El destino possemos lo siguiente:\n1.{dic[0]['route']}\n2.{dic[1]['route']}\n3.{dic[2]['route']}\n4.{dic[3]['route']}")
        dest_name = int(input("Ingrese El Numero Correspondiente A su Seleccion: "))
        while dest_name != 1 and dest_name != 2 and dest_name != 3 and dest_name != 4:
            dest_name = int(input("Error. Ingrese Un Caracter Valido: "))
        if dest_name == 1:
            print("--"*25)
            print(f"Para el barco {dic[0]['name']} tenemos las siguientes habitaciones:\n1. sencilla >> capacidad {dic[0]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[0]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[0]['capacity']['vip']} personas.")
            hab_selected = int(input("Ingrese El caracter correspondiente a su seleccion: "))
            while hab_selected != 1 and hab_selected != 2 and hab_selected !=3:
                hab_selected = int(input(f"Error. Ingrese Un caracter valido.\n1. sencilla >> capacidad {dic[0]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[0]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[0]['capacity']['vip']} personas."))
            if hab_selected == 1:
                print('\n')
                print(f"Muy Bien haz seleccionado la habitacion simple con capacidad para {dic[0]['capacity']['simple']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 2 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[0]['cost']['simple']}
                    ♦ Impuestos % 16 :  $ {(dic[0]['cost']['simple'])*0.16}
                    ♦ Total : $ {(dic[0]['cost']['simple'])+(dic[0]['cost']['simple'])*0.16}


                    '''
                    print(msgf)
            elif hab_selected == 2:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion premium con capacidad para {dic[0]['capacity']['premium']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 4 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones :  
                    ♦ Monto Total: % {dic[0]['cost']['premium']}
                    ♦ Impuestos % 16 :  $ {(dic[0]['cost']['premium'])*0.16}
                    ♦ Total : $ {(dic[0]['cost']['premium'])+(dic[0]['cost']['premium'])*0.16}


                    '''
                    print(msgf)
            elif hab_selected == 3:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion vip con capacidad para {dic[0]['capacity']['vip']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 8 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[0]['cost']['vip']}
                    ♦ Impuestos % 16 :  $ {(dic[0]['cost']['vip'])*0.16}
                    ♦ Total : $ {(dic[0]['cost']['vip'])+(dic[0]['cost']['vip'])*0.16}


                    '''
                    print(msgf)

        elif dest_name == 2:
            print("--"*25)
            print(f"Para el barco {dic[1]['name']} tenemos las siguientes habitaciones:\n1. sencilla >> capacidad {dic[1]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[1]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[1]['capacity']['vip']} personas.")
            hab_selected = int(input("Ingrese El caracter correspondiente a su seleccion: "))
            while hab_selected != 1 and hab_selected != 2 and hab_selected !=3:
                hab_selected = int(input(f"Error. Ingrese Un caracter valido.\n1. sencilla >> capacidad {dic[1]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[1]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[1]['capacity']['vip']} personas."))
            if hab_selected == 1:
                print('\n')
                print(f"Muy Bien haz seleccionado la habitacion simple con capacidad para {dic[1]['capacity']['simple']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 2 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones :  
                    ♦ Monto Total: % {dic[1]['cost']['simple']}
                    ♦ Impuestos % 16 :  $ {(dic[1]['cost']['simple'])*0.16}
                    ♦ Total : $ {(dic[1]['cost']['simple'])+(dic[1]['cost']['simple'])*0.16}


                    '''
                    print(msgf)
            elif dest_name == 2:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion premium con capacidad para {dic[1]['capacity']['premium']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 4 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[1]['cost']['premium']}
                    ♦ Impuestos % 16 :  $ {(dic[1]['cost']['simple'])*0.16}
                    ♦ Total : $ {(dic[1]['cost']['premium'])+(dic[1]['cost']['premium'])*0.16}


                    '''
                    print(msgf)
            elif dest_name == 3:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion vip con capacidad para {dic[1]['capacity']['vip']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 8 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[1]['cost']['vip']}
                    ♦ Impuestos % 16 :  $ {(dic[1]['cost']['vip'])*0.16}
                    ♦ Total : $ {(dic[1]['cost']['vip'])+(dic[1]['cost']['vip'])*0.16}


                    '''
                    print(msgf)
        elif dest_name == 3:
            print("--"*25)
            print(f"Para el barco {dic[2]['name']} tenemos las siguientes habitaciones:\n1. sencilla >> capacidad {dic[2]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[2]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[2]['capacity']['vip']} personas.")
            hab_selected = int(input("Ingrese El caracter correspondiente a su seleccion: "))
            while hab_selected != 1 and hab_selected != 2 and hab_selected !=3:
                hab_selected = int(input(f"Error. Ingrese Un caracter valido.\n1. sencilla >> capacidad {dic[2]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[2]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[2]['capacity']['vip']} personas."))
            if hab_selected == 1:
                print('\n')
                print(f"Muy Bien haz seleccionado la habitacion simple con capacidad para {dic[2]['capacity']['simple']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 3 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[2]['cost']['simple']}
                    ♦ Impuestos % 16 :  $ {(dic[2]['cost']['simple'])*0.16}
                    ♦ Total : $ {(dic[2]['cost']['simple'])+(dic[2]['cost']['simple'])*0.16}


                    '''
                    print(msgf)
            elif hab_selected == 2:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion premium con capacidad para {dic[2]['capacity']['premium']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 5 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[2]['cost']['premium']}
                    ♦ Impuestos % 16 :  $ {(dic[2]['cost']['premium'])*0.16}
                    ♦ Total : $ {(dic[2]['cost']['premium'])+(dic[2]['cost']['premium'])*0.16}


                    '''
                    print(msgf)
            elif hab_selected == 3:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion vip con capacidad para {dic[2]['capacity']['vip']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 12 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[2]['cost']['vip']}
                    ♦ Impuestos % 16 :  $ {(dic[2]['cost']['vip'])*0.16}
                    ♦ Total : $ {(dic[2]['cost']['vip'])+(dic[2]['cost']['vip'])*0.16}


                    '''
                    print(msgf)
        elif dest_name == 4:
            print("--"*25)
            print(f"Para el barco {dic[3]['name']} tenemos las siguientes habitaciones:\n1. sencilla >> capacidad {dic[3]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[3]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[3]['capacity']['vip']} personas.")
            hab_selected = int(input("Ingrese El caracter correspondiente a su seleccion: "))
            while hab_selected != 1 and hab_selected != 2 and hab_selected !=3:
                hab_selected = int(input(f"Error. Ingrese Un caracter valido.\n1. sencilla >> capacidad {dic[3]['capacity']['simple']} personas.\n2. premium >> capacidad {dic[3]['capacity']['premium']} personas.\n3. vip >> capacidad {dic[3]['capacity']['vip']} personas."))
            if hab_selected == 1:
                print('\n')
                print(f"Muy Bien haz seleccionado la habitacion simple con capacidad para {dic[3]['capacity']['simple']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 3 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[3]['cost']['simple']}
                    ♦ Impuestos % 16 :  $ {(dic[3]['cost']['simple'])*0.16}
                    ♦ Total : $ {(dic[3]['cost']['simple'])+(dic[3]['cost']['simple'])*0.16}


                    '''
                    print(msgf)
            elif hab_selected == 2:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion premium con capacidad para {dic[3]['capacity']['premium']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 5 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[3]['cost']['premium']}
                    ♦ Impuestos % 16 :  $ {(dic[3]['cost']['premium'])*0.16}
                    ♦ Total : $ {(dic[3]['cost']['premium'])+(dic[3]['cost']['premium'])*0.16}


                    '''
                    print(msgf)
            elif hab_selected == 3:
                print("\n")
                print(f"Muy Bien haz seleccionado la habitacion vip con capacidad para {dic[3]['capacity']['vip']} personas.")
                amount_travelers = int(input("Ingrese La cantidad de personas que viajan: "))
                if amount_travelers <= 10 and amount_travelers > 0:
                    count = amount_travelers
                    form(count)
                    msgf = f'''
                    ------------------------
                            FACTURA
                    -------------------------
                    ♦ N De personas : {amount_travelers}
                    ♦ Habitaciones : 
                    ♦ Monto Total: % {dic[3]['cost']['vip']}
                    ♦ Impuestos % 16 :  $ {(dic[3]['cost']['vip'])*0.16}
                    ♦ Total : $ {(dic[3]['cost']['vip'])+(dic[3]['cost']['vip'])*0.16}


                    '''
                    print(msgf)

                      
                    



                
   
    

       
    

      

msgb = "---------------------------------------------------------------------\nBienvenido Al sistema de Gestion De Habitaciones De Saman Caribbean\n---------------------------------------------------------------------"

def main():
    print((msgb).title(),"\n")
    selection = int(input("Desea Vender Una Habitacion? \n1.Si!, Vender Habitacion\n2.No, Salir\n>>"))
    while selection != 1 and selection != 2:
        print("Error")
        selection = int(input("Ingrese Un Valor Numerico valido \n1.Vender Habitacion\n2.Salir\n>>"))
    if selection == 1:
        sell_habs()
        print((msgb).title(),"\n")
        selection = int(input("Desea Vender Una Habitacion? \n1.Si!, Vender Habitacion\n2.No, Salir\n>>"))
    elif selection == 2:
        print("Muy bien!. Nos Vemos Pronto.")



    

