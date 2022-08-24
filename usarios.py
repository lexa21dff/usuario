# -*- coding: utf-8 -*-
'''
Ejercicio 

Elabore un programa con Python que permita a un usuario registrarse con correo y contraseña, 
el correo únicamente debe pertenecer al dominio @misena.edu.co, la contraseña debe tener mínimo caracteres (1 Mayúscula), 
Números (1 numero)  y símbolos (1 símbolo).

Al registrarse el usuario debe ser único y mencionarle si ese usuario ya está registrado previamente en el sistema, 
La contraseña debe estar cifrada puede usar el método Cesar o cualquier otro método de cifrado en la "base de datos" llamada usuarios.txt    
El sistema debe permitir el acceso por medio de una opción de inicio de sesión y una vez inicie sesión deberá mostrarle un mensaje de bienvenida (Hola Usuario XXXXX)
En caso de que el usuario ingrese mal la clave 3 veces el usuario se deberá bloquear 
El sistema debe permitirle ejecutar estas acciones hasta que el usuario decida salir de la aplicación 

Para el desarrollo de este ejercicio debe emplear todos los temas vistos anteriormente (condiciones, ciclos, funciones, registros, archivos)   
Recuerde Elaborar el Análisis, Diseño y Comentar su Código 
Tiempo a Emplear 10 Horas (2 Jornadas)


Autor : alexandra
Cliente : SENA
Fecha: dd/mm/aaaa
Version: 1.0.0

'''

#	Constantes
#--------------------
# Variables Globales
#--------------------
# Procedimientos
#--------------------
# Funciones

class User():
    correo = ""
    clave = ""
    estado = "activo"


u = User()
u.correo = "qwerty@misena.edu.co"
u.clave = "Qwerty123."

# buscar_usuario()
def buscar_usuario(obj):
    archivo = open("usuarios.txt", "r")
    for indice, linea in enumerate(archivo):
        if obj.correo in linea :
            x = "correo existe"
            if cifrar_clave(obj.clave) in linea:
                print("usuario existe")
                print(indice)
                return indice
            return x    
        else: 
            continue
            print("usuario y/o clave incorrectas ")
    return False    

    


# registrar_usuario():
# iniciar_sesion()
# validar_clave()
# validar_dominio()
# cifrar_clave()
# bloquear_usuario()x
# saludar_usuario()x
# desbloquear_usuario()x
# recuperar_clave()x
# cerrar_sesion()x



# funcion para validar  que el correo únicamente pertenece al dominio @misena.edu.co
def validar_correo():
    dominio_valido = 'misena.edu.co'
    validar = False
    while True:
        validar_arroba= ''
        email = input('ingrese su correo electronico')
        for i in email:#ciclo for que recorre caracter por caracter en email
            if i == ' ':
                validar  = True
            if i == '@': #para asignar a una variable el arroba del correo si  este contiene uno
                validar_arroba = i
        if validar == False:
            if validar_arroba == '@': #verificar que el corrreo ingresado tenga un arroba
                nuevo_email = email.split('@')
                nombre_usuario = nuevo_email[0]
                dominio = nuevo_email[1]
                if dominio == dominio_valido: # valida que el dominio ingresado es valido
                    usuario = [nombre_usuario,email]
                    return email 
                else:
                        print('El correo electronico no es valido')
                        continue
            else:
                print('El  correo electronico no es valido')
                continue
        else:
            print('El correo electronico no es valido ESPACIOS')
            continue

#funcion para validar que la contraseña es valida
def validar_clave():
        while True :
            clave = input('ingrese la contraseña')
            longitud =len(clave) #Calcula la longitud de la contraseña
            espacio=False  #variable para identificar espacios
            mayuscula=False #variable para identificar letras mayúsculas
            minuscula=False #variable para contar identificar letras minúsculas
            numeros=False #variable para identificar números
            simbolos=clave.isalnum()#si es alfanumérica retona True
            for carac in clave: #ciclo for que recorre caracter por caracter en la contraseña
                if carac.isspace()==True: #Saber si el caracter es un espacio
                    espacio=True #si encuentra un espacio se cambia el valor clave
                if carac.isupper()== True: #saber si hay mayuscula
                    mayuscula=True  #si encuentra una letra mayuscula se cambia el valor de mayuscula a True
                if carac.islower()== True: #saber si hay minúsculas
                    minuscula=True 
                
                if carac.isdigit()== True: #saber si hay números
                    numeros=True #acumulador o contador de numeros
                            
            if espacio==False: #no hay espacios en blanco
                #se cumple el primer requisito que no hayan espacios
                if longitud >=8 :
                    #se cumple el requisito minimo de caracteres
                    if mayuscula == True and minuscula ==True and numeros == True and simbolos== False :
                        return clave
                        #Cumple el requisito de tener mayuscula, minuscula, numeros y simbolos
                    else:
                        print("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")
                        continue #uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple  
                else:
                    print("Mínimo 8 caracteres")
                    #no se cumple el requisito móinimo de caracteres
                    continue
            else:
                print("La contraseña no puede contener espacios")
                continue

#funcion para encriptar la contraseña
def cifrar_clave(clave):
    textofinal = ''
    for letra in clave:
        ascii = ord(letra)
        ascii += 1
        textofinal += chr(ascii)
    return textofinal
# funcion para desencriprar 
def desifrar_clave (clave):
    print('el texto a desencriptar es: ',clave)
    textofinal = ''
    for letra in clave:
        ascii = ord(letra)
        ascii -= 1
        textofinal += chr(ascii)
    return textofinal



def registrar_usuario(objeto):
    archivo = open('usuarios.txt', 'a')
    archivo.write(objeto.correo + ';' + objeto.clave + ';' + objeto.estado + ';' +'\n') 
    archivo.close()

# registrar_usuario(u)

# procedimiento para boquear un usuario
def modificar_dato(ruta, filas, nuevo_dato):
    contenido = list ()
    with open(ruta, 'r+') as archivo:
        contenido = archivo.readlines()
        columnas = contenido[filas-1].split(';')
        columnas[2] = nuevo_dato
        contenido[filas-1] = ';'.join(columnas) 
    with open(ruta, 'w') as archivo:
        archivo.writelines(contenido)   

# funcion para comparar los datos ingresados del usuario para iniciar sesion con la base de datos usuarios.txt
def registros_usuarios(email,clave,intentos): 
    usuarios = open('usuarios.txt', 'r' )
    conteo = 0
    fila = 0
    for linea in usuarios:
        conteo += 1
        registros = ''
        usuario = []
        for i in linea:
            registros += i
            if i == ';':
                registro = ''
                for j in registros:
                    if j != ';':
                        registro += j
                usuario.append(registro)
                registros = ''
        if usuario[0]==email:
            fila = conteo
            if usuario[2]== 'activo': 
                if usuario[1]==clave:
                    return True
                else:
                    if intentos == 0 :
                        nuevo = 'inactivo'
                        modificar_dato('usuarios.txt',fila,nuevo)

                    return False
    
            else:
                return 'inactivo'


# funcion para iniciar ses ion y validar que el usuario este registrado en la base de datos usuarios
def validar_usuario():
    intentos = 3
    while True:
        print(intentos)
        email = input('ingrese el correo electronico')
        clave = input('ingrese la clave')
        clave_cifrada = cifrar_clave(clave)
        validar = registros_usuarios(email,clave_cifrada,intentos)
        if validar == True:

            return True
        elif validar == 'inactivo':
            print('usuario bloqueado')
            return validar
        elif validar == False:
            intentos -= 1
            if intentos == 0:
                registros_usuarios(email,clave,intentos)
                return intentos
        else:
            continue
        
        
def opciones_del_programa():
    while True:
        print('ingrese la opcion que desea realizar.' )
        print('[1] registrar usuario.' )
        print('[2] iniciar sesion.' )
        print('[3] salir.' )
        opcion = input("seleecione su opción :  ")
        if opcion == '1':

        #def_registrar_datos():
        elif opcion == '2':
            print('iniciar secion')
            iniciar1 = validar_usuario()
            if iniciar1 == True:
                print('bienvenido')
                continue
            elif iniciar1 == 'inactivo':
                continue
            elif iniciar1 == 0:
                print('usuario bloqueado')
                continue

        elif opcion  == '3' :
            break
        else:
            print('la opcion ingresada no es valida')
            continue


def main ():
    buscar_usuario(u)
    opciones_del_programa()

if __name__ == '__main__':
    main()
