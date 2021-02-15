import libreria
def agregardatos():
    nombre=libreria.pedir_primer_nombre("ingrese su primer nombre:")
    apellidos=libreria.pedir_apellidos("ingrese sus apellidos:")
    codigo_trabajo=libreria.pedir_codigo("ingrese codigo:")
    link=libreria.pedir_link("ingrese link:")
    nota=libreria.pedir_nota("ingrese nota:")
    suma_datos=nombre+" "+apellidos #suma nombre mas apellidos
    contenido=suma_datos+","+codigo_trabajo+","+link+","+str(nota)+"\n"
    libreria.guardar_datos("trabajos.txt", contenido, "a")
    print("DATOS GUARDADOS")

def leerdatos():
    # 1. Abrir el archivo trabajos.txt y mostrar sus datos
    datos = libreria.obtener_datos_lista("trabajos.txt")
    # 2. COmprobar si hay datos
    if ( datos != ""):
        for item in datos:
            suma_datos,codigo_trabajo,link,nota=item.split(",")
            suma_datos=suma_datos.replace("\n","")
            codigo_trabajo=codigo_trabajo.replace("\n","")
            link=link.replace("\n","")
            nota=nota.replace("\n","")
            #sacar datos de nombre y apellid.
            extraer=suma_datos.split(" ")
            nombre=extraer[0]
            apellidos=extraer[1]+" "+extraer[2]
            #datos para el reporte
            alumno=apellidos+" "+nombre
            alumno=alumno.upper()
            print(libreria.reporte(alumno,codigo_trabajo,link,nota))
opc=0
max=3
while(opc!=3):
    print("############ MENU #############")
    print("1.AGREGAR DATOS               #")
    print("2.LEER DATOS                  #")
    print("3.SALR                        #")
    print("###############################")
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    if(opc==1):
        agregardatos()
    if(opc==2):
        leerdatos()
    #fin_while
#fin_while
print("FIN DEL PROGRAMA")



