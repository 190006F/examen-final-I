#VALIDAR NUMERO ENTERO
def validar_entero(n):
    if(isinstance(n,bool)):
        return False
    if (isinstance(n, int)):
        return True
    else:
        return False
#FIN_DEF

#VALIDAR RANGO
def validar_rango(n, ri, rf):
    if ( validar_entero(n) == True):
        if (n >= ri and n <= rf):
            return True
        else:
            return False
    else:
        return False
#fin_def

#VALIDAR NOMBRE
def validar_primer_nombre(nombre):
    if(isinstance(nombre,bool)):
        return False
    if ( isinstance(nombre, str)):
        if (len(nombre) >= 3):
            if(nombre.isdigit()!=True):
                primer_nombre=nombre.split(" ")
                if(len(primer_nombre)==2):
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False
    else:
        return False
#fin_def

def pedir_numero(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
#fin_pedir_numero

#PEDIR NOMBRE
def pedir_primer_nombre(msg):
    nombre=""
    while ( validar_primer_nombre(nombre) == False ):
        nombre=input(msg)
    #fin_while
    return nombre
#fin_DEF
#VALIDAR APELLIDOS
def validar_apellidos(apellidos):
    if(isinstance(apellidos,str)):
        #.los apellidos deben ser 2
         apellidos=apellidos.split(" ")
         if(len(apellidos)!=2):
             return False
         #.apellidos deben ser letras
         apellido1=apellidos[0]
         apellido2=apellidos[1]
         if(apellido1.isalpha()==False or apellido2.isalpha()==False):
             return False
         if (len(apellido1)<3 or len(apellido2)<3):
             return False
         #si llego hasta aqui es por que es un apellido valido
         return True
    else:
        return False
#fin_def

#PEDIR APELLIDOS
def pedir_apellidos(msg):
    apellidos=""
    while(validar_apellidos(apellidos)==False):
        apellidos=input(msg)
    #fin_while
    return apellidos
#fin_def

#validar codigo de trabajo
def validar_codigo_trabajo(codigo_trabajo):
    if(isinstance(codigo_trabajo,str)):
        codigo_trabajo=codigo_trabajo.upper()
        if(codigo_trabajo=="T1" or codigo_trabajo=="T2"):
            return True
        else:
            return False
    else:
        return False
#fin_def

#pedir codigo
def pedir_codigo(msg):
    codigo_trabajo=""
    while(validar_codigo_trabajo(codigo_trabajo)==False):
        codigo_trabajo=input(msg)
    #fin_while
    return codigo_trabajo
#fin_def

#validar nota
def validar_nota(nota):
    if(isinstance(nota,bool)):
        return False
    if(isinstance(nota,int) or isinstance(nota,float)):
        if(nota>=0 and nota<=20):
            return True
        else:
            return False
    else:
        return False
#fin_def

#pedir nota
def pedir_nota(msg):
    nota=-4
    while(validar_nota(nota)==False):
        nota=input(msg)
        if(nota.isdigit()==True):
           nota=int(nota)
    #fin_while
    return nota
#fin_def

#VALIDAR DOMINIO
def validar_dominio(dominio):
    if(isinstance(dominio,str)):
        #dividision en dos partes(nombre y extesion)
        partes=dominio.split(".")
        if(len(partes)!=2):
            return False
        nombre=partes[0]
        extension=partes[1]
        #el nombre no debe ser un numero
        if(nombre.isdigit()==True):
            return False
        #la extension debe ser estrictamente "com"  y no usar conversion en caso fuera "COM"
        if(extension!="com"):
            return False
        #si llego hasta aqui es por que es un dominio valido
        return True
    else:
        return False
#fin_def

#validar usuario
def validar_usuario(usuario):
    if(isinstance(usuario,bool)):
        return False
    if ( isinstance(usuario, str)):
        if (len(usuario) >= 3):
            if(usuario.isalnum()==True):
                usuario=usuario.split(" ")
                if(len(usuario)==2):
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False
    else:
        return False
#fin_def

#VALIDAR REPOSITORIO
def validar_repositorio(repositorio):
    if(isinstance(repositorio,str)):
        #dividision en dos partes(nombre y extesion)
        partes=repositorio.split(".")
        if(len(partes)!=2):
            return False
        nombre=partes[0]
        extension=partes[1]
        #el nombre del repositorio debe ser alfanumerico
        if(nombre.isalnum()!=True):
            return False
        #la extension debe ser estrictamente "git"  y no usar conversion en caso fuera "GIT"
        if(extension!="git"):
            return False
        #si llego hasta aqui es por que es un dominio valido
        return True
    else:
        return False
#fin_def

#VALIDAR LINK
def validar_link(link):
    #revisar si es cadena
    #formato con sinbolo "/"
    if(isinstance(link,str)):
        data=link.split("/")
        if(len(data)!=3):
            return False
        dominio=data[0]
        usuario=data[1]
        repositorio=data[2]
        if(validar_dominio(dominio)==True and validar_usuario(usuario)==True and validar_repositorio(repositorio)==True):
            return True
        else:
            return False
    else:
        return False
#fin_def

#pedir_link
def pedir_link(msg):
    link=""
    while(validar_link(link)==False):
        link=input(msg)
    #fin_while
    return link
#fin_def

#GUARDAR DATOS
def guardar_datos(nombre_archivo, contenido, modo):
    archivo=open(nombre_archivo, modo)
    archivo.write(contenido)
    archivo.close()
#fin_def

#OBTENER DATOS
def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido = archivo.read()
    archivo.close()
    return contenido
#fin_def

#OBTENER DATOS DE LISTA
def obtener_datos_lista(nombre_archivo):
    archivo=open(nombre_archivo)
    lista = archivo.readlines()
    archivo.close()
    return lista
#fin_def

#reporte de trabajos
def reporte(alumno,codigo_trabajo,link,nota):
    codigo_trabajo=codigo_trabajo.upper()
    if(codigo_trabajo=="T1"):
        msg="TRABAJO 1"
    else:
        msg="TRABAJO 2"
    url="https://"+link
    print(" ")
    print("############################################################################3###")
    print("#REPOTE DE TRABAJOS GIT")
    print("################################################################################")
    print("#ALUMNO             TAREA           URL                              NOTA       ")
    print("################################################################################")
    print("#"+alumno+"    "+msg+"       "+url+"      "+str(nota))
    print("################################################################################")
    print("  ")
