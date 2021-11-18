'''
Universidad del Valle de Guatemala
Sistema de telecomunicaciones 1
Proyecto HTTP(Navegador)
Luis Gómez 18291
Helder Ovalle 18349
'''

#Librerias
import socket
opcion=0
while opcion!=2: #Mientras no sea la opcion de salir
    print("OPCIONES\n1. HTTP\n2. Salir")
    opcion = input("Escoga una opcion (1-2):\n")
    while not opcion.isdigit(): #Mientras la opcion no sea digito
          opcion = input("Escoga una opcion (1-2):\n") #Vuelve a preguntar
    opcion = int(opcion) #Se vuelve entera la variable
    if opcion == 1:
            #PARTE : HTTP 

            #http://gaia.cs.umass.edu/search.html
            #http://gaia.cs.umass.edu/kurose_ross/about.php
            #http://gaia.cs.umass.edu/networks/education/index.html
            #http://www.asifunciona.com/inicio.htm
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp
            
            server = input("Ingrese URL:\n") #URL
            REAL_HOST = server.replace("http://", "").split("/")[0] #reemplaza lo ingresado 
            print(REAL_HOST) #se verifica el ingreso del host
            port = 80 #puerto http 
            server_ip = socket.gethostbyname(REAL_HOST) #se obtiene la ip del host
            print(server_ip) #se imprime la ip
            
            get = input("Ingrese path name:\n") #se ingresa el path name del url
            request = "GET /"+get+"\r\nHost: "+REAL_HOST+"\n\n" #se realiza el request mediante get
            s.connect((REAL_HOST,port)) #conectar via socket
            s.send(request.encode())#enviar el request
            result = s.recv(4096)#recibir

            #print(result)
            while (len(result) > 0):
                print(result) #imprime el resultado
                result = s.recv(4096)
                
    elif opcion == 2:
            print("Gracias por utilizar el programa\n") #salir del programa
    else:
            print("Opcion no valida\n")
