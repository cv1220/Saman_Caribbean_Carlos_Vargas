import requests
#utilizando el request de llama al metodo GET para asi obtener la info de la api para luego almacenarla en la varibale dic dandole un formato de diccionario
#utilizando el .json()
r = requests.get("https://saman-caribbean.vercel.app/api/cruise-ships")

d = '---'*100
dic = r.json()

msg1 = '''                   
            ------------------------ Saman caribbean ------------------------
                                                        
              ¡Se Bienvenido a nuesta cadena de cruceros Saman Caribbean!
      podras disfrutar de 4 maravillos cruceros con todos los lujos que puedas imaginar 
        Con destinos turisticos unicos que te haran vivir una experiencia inigualable
      Preparate para embarcarte en una gran aventura y llevarte recuerdos inolvidables!

                        1. Muestrame Los Barcos!
                        2. Lo siento creo que no es lo que buscaba

'''
# Se define una funcion para cada barco disponible
#dentro De esa funcion se muestran los datos de los barcos respectivamente basando en la informacion que se encuentra en dic, tales como nombre, ruta, fecha de salida 
#coste del boleto tanto como su capacidad
def ship_1():
    print((f'''
                        ------------{dic[0]['name']}------------

                Presenta La siguiente ruta {dic[0]['route']}
                Fecha De Salida: {dic[0]['departure']}
                Coste de boleto por tipo de habitacion:
                    °hab simple: ${dic[0]['cost']['simple']} 
                    °hab Premium: ${dic[0]['cost']['premium']}
                    °hab VIP: ${dic[0]['cost']['vip']}
                Capacidad de personas por habitacion:
                    ° simple -- {dic[0]['capacity']['simple']} personas
                    ° premium -- {dic[0]['capacity']['premium']} personas
                    ° VIP -- {dic[0]['capacity']['vip']} personas

    
    ''').title())

def ship_2():
    print((f'''
                        ------------{dic[1]['name']}------------

                Presenta La siguiente ruta {dic[1]['route']}
                Fecha De Salida: {dic[1]['departure']}
                Coste de boleto por tipo de habitacion:
                    °hab simple: ${dic[1]['cost']['simple']} 
                    °hab Premium: ${dic[1]['cost']['premium']}
                    °hab VIP: ${dic[1]['cost']['vip']}
                Capacidad de personas por habitacion:
                    ° simple -- {dic[1]['capacity']['simple']} personas
                    ° premium -- {dic[1]['capacity']['premium']} personas
                    ° VIP -- {dic[1]['capacity']['vip']} personas

    
    ''').title())

def ship_3():
    print((f'''
                        ------------{dic[2]['name']}------------

                Presenta La siguiente ruta {dic[2]['route']}
                Fecha De Salida: {dic[2]['departure']}
                Coste de boleto por tipo de habitacion:
                    °hab simple: ${dic[2]['cost']['simple']} 
                    °hab Premium: ${dic[2]['cost']['premium']}
                    °hab VIP: ${dic[2]['cost']['vip']}
                Capacidad de personas por habitacion:
                    ° simple -- {dic[2]['capacity']['simple']} personas
                    ° premium -- {dic[2]['capacity']['premium']} personas
                    ° VIP -- {dic[2]['capacity']['vip']} personas

    
    ''').title())    

def ship_4():
    print((f'''
                        ------------{dic[3]['name']}------------

                Presenta La siguiente ruta {dic[3]['route']}
                Fecha De Salida: {dic[3]['departure']}
                Coste de boleto por tipo de habitacion:
                    °hab simple: ${dic[3]['cost']['simple']} 
                    °hab Premium: ${dic[3]['cost']['premium']}
                    °hab VIP: ${dic[3]['cost']['vip']}
                Capacidad de personas por habitacion:
                    ° simple -- {dic[3]['capacity']['simple']} personas
                    ° premium -- {dic[3]['capacity']['premium']} personas
                    ° VIP -- {dic[3]['capacity']['vip']} personas

    
    ''').title())
 # se crea un funcion llamada start que sirve para inicializar el codigo dentro del modulo de menu princicpal
def start():
    print((msg1).title())
    tmp = str(input("Ingrese La Opcion que desea Realizar: "))
    
    if tmp == '1':
        
        print("Muy Bien Tenemos A Disposicion los siguiente barcos: ")
        ship_1()
        ship_2()
        ship_3()
        ship_4()
    elif tmp == '2':
        print("\nLamentamos Verte Marchar. Por Parte Del Equipo De Saman Caribbean Le Deseamos Buenos Dias.")
    else:
        print()
        print(("\nError intentelo de nuevo").title())
        
        

        
    
    


    

    
    

    
    


    

#main()