from xml.dom import minidom
from Terreno import terreno,lista_terreno

def cargarArchivo():
    global path
    path = input("Ingrese la ruta del archivo: ")
    try:
        file = open(path)
        global text
        parsear=file.read()
        text = parsear.lower()
        print("Exito!!!")
    except:
        print("Ruta invalida")
        
def procesarArchivo():
    global terr
    lista_terr=lista_terreno()
    archivo= str(path)
    mydoc = minidom.parse(archivo)
    terrenos = mydoc.getElementsByTagName('TERRENO')
    # dim=mydoc.getElementsByTagName('m')
    # print('Valor de Atributos de elementos:')
    # print(items[0].attributes['name'].value)
    # for d in dim:
    #     print(d.firstChild.data)
    for e in terrenos:
        nombre=e.attributes["nombre"].value
        # dimension=dim.attributes["DIMENSION"].value
        dimension=e.getElementsByTagName('DIMENSION')
        posicionInicial=e.getElementsByTagName('posicioninicio')
        posicionFinal=e.getElementsByTagName('posicionfin')
        for dimen in dimension:
            fila=dimen.getElementsByTagName('m')[0].firstChild.data
            columna=dimen.getElementsByTagName('n')[0].firstChild.data
        # xPosI=e.getElementsByTagName('x')[0].firstChild.data
        # yPosI=e.getElementsByTagName('y')[0].firstChild.data
        # xPosF=e.getElementsByTagName('x')[0].firstChild.data
        # yPosF=e.getElementsByTagName('y')[0].firstChild.data
        #print(nombre,fila,columna,xPosI,yPosI,xPosF,yPosF)
        # for dim in dimension:
        #     fila=mydoc.getElementsByTagName('m')
        #     columna=mydoc.getElementsByTagName('n')
        #     for f in fila:
        #         fi=f.firstChild.data
        #         # co=columna.firstChild.data
        #         print(fi)
        #     break
        for posI in posicionInicial:
            xPosI=posI.getElementsByTagName('x')[0].firstChild.data
            yPosI=posI.getElementsByTagName('y')[0].firstChild.data
        for posF in posicionFinal:
            xPosF=posF.getElementsByTagName('x')[0].firstChild.data
            yPosF=posF.getElementsByTagName('y')[0].firstChild.data
        #print(nombre,fila,columna,xPosI,yPosI,xPosF,yPosF)
        terr=terreno(nombre,fila,columna,xPosI,yPosI,xPosF,yPosF)
        lista_terr.insertar(terr)
    #print(nombre,fila,columna,xPosI,yPosI,xPosF,yPosF)
    lista_terr.recorrer()
    
    # posiciones= mydoc.getElementsByTagName("posicion")
    # for posi in posiciones:
    #     x=posi.attributes["x"].value
    #     y=posi.attributes["y"].value
    #     valor=posi.firstChild.data
    #     print("Posicion",x,y,"Valor",valor)
        

    # print("forma 1:", items[0].childNodes[0].data)
    # print("forma 2:", items[0].firstChild.data)



if __name__ == '__main__':
    print("Menu Principal: ")
    print("     1. Cargar Archivo")
    print("     2. Procesar Archivo")
    print("     3. Escribir Archivo de Salida")
    print("     4. Mostrar Datos del Estudiante")
    print("     5. Generar Grafica")
    print("     6. Salida")
    opcion=input("Ingrese la opcion que desea:  ")
    
    if opcion=="1":
        cargarArchivo()
        procesarArchivo()
    elif opcion=="2":
        print("-Calculando la mejor ruta")
        print("-Calculando cantidad de combustible")
    elif opcion=="3":
        print("Escribir una ruta especifica: ")
    elif opcion=="4":
        print("Cristian Hernandez")
        print("202010905")
        print("Introduccion a la Programacion y Computacion 1 E")
        print("Ingenieria en Ciencias y Sistemas")
        print("4to Semestre")
                
        
        
        
    
