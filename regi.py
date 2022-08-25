import os
def archivo ():
    va = os.path.exists('usuarios.txt')
    if va == True:
        pass
    else:
        print('crear')
        ar = open('usuarios.txt', 'x')
        ar.close
    
    

archivo()