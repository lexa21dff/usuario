def registrar(objeto):
    archivo = open('usuarios.txt', 'a')
    archivo.write(objeto.correo + ';' + objeto.clave + ';' + objeto.estado + ';' +'\n') 
    archivo.close 


registrar()