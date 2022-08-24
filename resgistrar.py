
class User():
    correo = ""
    clave = ""
    estado = "activo"
u = User()
#funcion para validar que la contraseña es valida
def validar_clave(clave):
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
                    return True
                    #Cumple el requisito de tener mayuscula, minuscula, numeros y simbolos
                else:
                    print("La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")
                    #uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple  
            else:
                print("Mínimo 8 caracteres")
                #no se cumple el requisito móinimo de caracteres
        else:
            print("La contraseña no puede contener espacios")
#funcion para cifrar la contraseña
def cifrar_clave(clave):
    textofinal = ''
    for letra in clave:
        ascii = ord(letra)
        ascii += 1
        textofinal += chr(ascii)
    return textofinal
# valida  el dominio
def validar_dominio(correo):
    dominio_valido = 'misena.edu.co'
    validar = False
    validar_arroba= ''
    for i in correo:#ciclo for que recorre caracter por caracter en email
        if i == ' ':
            validar  = True
        if i == '@': #para asignar a una variable el arroba del correo si  este contiene uno
            validar_arroba = i
    if validar == False:
        if validar_arroba == '@': #verificar que el corrreo ingresado tenga un arroba
            nuevo_email = correo.split('@')
            dominio = nuevo_email[1]
            if dominio == dominio_valido: # valida que el dominio ingresado es valido
                return True 
            else:
                return False
        else:
            return False
    else:
        return False
# busca el los datos 
def buscar_usuario(opcion, obj):
    archivo = open("usuarios.txt", "r")
    for indice, linea in enumerate(archivo):
        if opcion == '1':
            if obj.correo in linea :
                x = "correo existe"
                return x           
        elif opcion == '2':
            if obj.correo in linea :
                print(linea)
                print('correo')
                print(obj.estado)
                if obj.estado in linea:
                    print(obj.estado)
                    print('estado')
                    if obj.clave in linea :
                        print(linea)
                        print('clave')
                        return True
                    else: 
                        return False
                else:
                    return 'no'
            else: 
                continue
                print("usuario y/o clave incorrectas ") 
# registra los usuarios en la base de datos usuarios.txt
def registrar(objeto):
    archivo = open('usuarios.txt', 'a')
    archivo.write(objeto.correo + ';' + objeto.clave + ';' + objeto.estado + ';' +'\n') 
    archivo.close()
# ingresa los usuarios y los registra en la base de datos usuarios.txt
def  registrar_usuario(opcion,obj):
    while True:
        correo = input('ingrese su correo electronico')
        clave = input('Crea una contraseña que tenga al menos ocho caracteres')
        confimacion_clave = input('Confirme su contrseña')
        if clave == confimacion_clave:
            clave_cifrada = cifrar_clave(clave)
            obj.correo = correo
            obj.clave = clave_cifrada
            dominio_valido = validar_dominio(correo)
            correo_valido = buscar_usuario(opcion,obj)
            clave_valida = validar_clave(clave)
            if correo_valido != "correo existe":
                if dominio_valido == True:
                    if clave_valida == True:
                        registrar(obj)
                        return True
                else:
                    continue
            else:
                print('usuario existe')
                continue
        else:
            continue
# ingresa los datos para iniciar sesion
def iniciar_sesion(opcion, obj):
    while True:
        correo = input('ingrese el correo electronico ')
        clave = input ('ingrese la clave ')
        clave_cifrada = cifrar_clave(clave)
        obj.correo = correo
        obj.clave = clave_cifrada
        usuario = buscar_usuario(opcion, obj)
        if usuario == True:
            print('bienvenido')
            return True
        elif usuario == 'no':
            print('usuario bloqueado')
        else:
            continue
        






#opciones del programa
def opciones_del_programa(u):
    while True:
        print('[1] registrar usuario.' )
        print('[2] iniciar sesion.' )
        print('[3] salir.' )
        opcion = input("seleecione su opción :  ")
        if opcion == '1':
            registrar = registrar_usuario(opcion, u)
            if registrar == True:
                print('registro exitosamente')
                continue
            

        #def_registrar_datos():
        elif opcion == '2':
            usuario = iniciar_sesion(opcion, u)
            if usuario == True:
                print('cerrar_sesion')
            continue

        elif opcion  == '3' :
            break
        else:
            print('la opcion ingresada no es valida')
            continue

opciones_del_programa(u)

print(u.correo )