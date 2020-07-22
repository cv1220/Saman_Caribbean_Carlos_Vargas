def tour_port():
    cupos_max = 10
    cupos = []
    print("Muy bien, el precio para el tour por el puerto es de $30/persona")
    var = int(input("Ingrese el numero de personas a registrar en el tour (maximo 4 personas): "))
    
    if  var > 4:
        print(("Se ha excedido el numero de personas validas. intentelo de nuevo").title())
        var = int(input("Ingrese el numero de personas a registrar en el tour (maximo 4 personas): "))
    elif var == 1 or var == 2:
        print((f"Muy bien, se han registrado {var} personas en el tour").title())
        
        
        print(f"""              ---------Resumen de compra---------
        ^- El Tour Comienza A Las 7 A.M Hora Local
        ^- Numero de personas inscritas {var}
        ^- El Monto Total A pagar Es De {var*30} $ y no aplica ningun descuento
        
        Por parte de Saman Caribbean Le deseamos felices vacaciones""")
        cupos = cupos_max- var
        print(f"cupos restantes {cupos}")
    elif var == 3:
        print((f"Muy bien, se han registrado {var} personas en el tour").title())
        
        
        print(f"""              ---------Resumen de compra---------
        ^- El Tour Comienza A Las 7 A.M Hora Local
        ^- Numero de personas inscritas {var}
        ^- El Monto Total A pagar Es De {var*30 -(var*30)*0.1} $ y se aplico un descuento del 10%
        
        Por parte de Saman Caribbean Le deseamos felices vacaciones""")
        cupos = cupos_max- var
        print(f"cupos restantes {cupos}")
    elif var == 4:
        print((f"Muy bien, se han registrado {var} personas en el tour").title())
        
        
        print(f"""              ---------Resumen de compra---------
        ^- El Tour Comienza A Las 7 A.M Hora Local
        ^- Numero de personas inscritas {var}
        ^- El Monto Total A pagar Es De {var*30 -(var*30)*0.2} $ y se aplico un descuento del 10%
        
        Por parte de Saman Caribbean Le deseamos felices vacaciones""")
        cupos = cupos_max- var
        print(f"cupos restantes {cupos}")

    
def food_tour():
    while True:
        print(''' \n---Bienvenido Al Servicio de Degustación de comida local---
        El precio por persona para disfrutar de este tour es de $100/persona''')
        var2 = int(input(("Por favor, Ingrese el numero de personas a inscribir:")).title())
        if var2  == 1 or var2 == 2:
            print((f"Muy bien, se han registrado {var2} personas en el tour").title())
        
        
            print(f"""              ---------Resumen de compra---------
            ^- El Tour Comienza A Las 12:00 PM Hora Local
            ^- Numero de personas inscritas {var2}
            ^- El Monto Total A pagar Es De ${var2*100} 
        
            Por parte de Saman Caribbean Le deseamos felices vacaciones""")
            break
        elif var2 < 1:
            print(("\nPor favor Ingrese un numero de personas mayor a 0").title())
        else:
            print(("\nEl numero maximo de personas por compra ha sido excedido. Por favor, intentelo de nuevo").title())
        

def runner_tour():
    while True:

        print(''' \n---Bienvenido Al Servicio trote de la zona local---
            Este servicio es completamente Gratis y no tiene limite de cupos
            Desea inscribirse en el tour (s/n):''')
        var3 = (input("Por favor Ingrese Alguna De Las opciones:").lower())
        
        if var3 == 's':
            var3_1 = int(input("Ingrese el numero de personas a registrar:"))
            print()
            print(f"""              ---------Resumen de compra---------
                ^- El Tour Comienza A Las 12:00 PM Hora Local
                ^- Numero de personas inscritas {var3_1}
                ^- El Monto Total A pagar Es De $0
            
                Por parte de Saman Caribbean Le deseamos felices vacaciones""")
            break
        elif var3 == 'n':
            print(('\nMuchas Gracias por pensar en nosotros como su opcion para un paquete de tour le deseamos felices vacaciones').title())
            break
        else:
            print("Error Ingrese una opcion valida.")
            print()
            var3 = (input("Por favor Ingrese Alguna De Las opciones:").lower())

def historic_tour():
    
    cupos_max4 = 15
    cupos4 = []

    print("Muy bien, el precio para el tour por el puerto es de $40/persona")
    var4 = int(input("Ingrese el numero de personas a registrar en el tour (maximo 4 personas): "))
    
    if  var4 > 4:
        print(("Se ha excedido el numero de personas validas. intentelo de nuevo").title())
        var4 = int(input("Ingrese el numero de personas a registrar en el tour (maximo 4 personas): "))
    elif var4 == 1 or var4 == 2:
        print((f"Muy bien, se han registrado {var4} personas en el tour").title())
        
        
        print(f"""              ---------Resumen de compra---------
        ^- El Tour Comienza A Las 10:00 AM Hora Local
        ^- Numero de personas inscritas {var4}
        ^- El Monto Total A pagar Es De ${var4*40}  y no aplica ningun descuento
        
        Por parte de Saman Caribbean Le deseamos felices vacaciones""")
        cupos4 = cupos_max4- var4
        print(f"cupos restantes {cupos4}")
    elif var4 == 3:
        print((f"Muy bien, se han registrado {var4} personas en el tour").title())
        
        
        print(f"""              ---------Resumen de compra---------
        ^- El Tour Comienza A Las 10:00 AM Hora Local
        ^- Numero de personas inscritas {var4}
        ^- El Monto Total A pagar Es De {var4*30 -(var4*40)*0.1} $ y se aplico un descuento del 10%
        
        Por parte de Saman Caribbean Le deseamos felices vacaciones""")
        cupos4 = cupos_max4- var4
        print(f"cupos restantes {cupos4}")
    elif var4 == 4:
        print((f"Muy bien, se han registrado {var4} personas en el tour").title())
        
        
        print(f"""              ---------Resumen de compra---------
        ^- El Tour Comienza A Las 10:00 A.M Hora Local
        ^- Numero de personas inscritas {var4}
        ^- El Monto Total A pagar Es De {var4*40 -(var4*40)*0.2} $ y se aplico un descuento del 10%
        
        Por parte de Saman Caribbean Le deseamos felices vacaciones""")
        cupos4 = cupos_max4- var4
        print(f"cupos restantes {cupos4}")

        


        


        


    

def intro_tour():
    print(("""Bienvenido a nuestro seccion de tours
    1. Tour En el puerto
    2. Degustación de comida local
    3. Trotar por el pueblo/ ciudad
    4. Visita a lugares historicos
    ----------------------------------
    5. Salir
    """).title())


def main():
    tours_vendidos = 0
    while True:
        intro_tour()
        dni = input("Por Favor Ingrese su dni: ")
        seleccion = int(input('Por favor indique el tour que desea seleccionar: '))

        if seleccion != 1 and seleccion != 2 and seleccion != 3 and seleccion !=4 and seleccion != 5:
            print(('Por favor indique un numero valido').title())
            seleccion = int(input('Por favor indique su seleccion: '))
        elif seleccion == 1:
            tour_port()
        elif seleccion == 2:
            food_tour()
        elif seleccion == 3:
            runner_tour()
        elif seleccion == 4:
            historic_tour()

        elif seleccion == 5:
            print(("""\n
            -----------------------------------------------------------------------------------------
            Gracias por tomarnos en consideracion como opcion para su tour durantes estas vacaciones!
            
            Por Parte del equipo de Saman Caribbean le deseamos felices vacaciones!""").title())
            break

        


