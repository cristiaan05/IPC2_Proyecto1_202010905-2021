from Nodo import nodo
class terreno:
    def __init__(self,nombre,filas,columnas,xPosInicio,yPosInicio,xPosFinal,yPosFinal):
        self.nombre=nombre
        self.filas=filas
        self.columnas=columnas
        self.xPosInicio=xPosInicio
        self.yPosInicio=yPosInicio
        self.xPosFinal=xPosFinal
        self.yPosFinal=yPosFinal
class lista_terreno:
    def __init__(self):
        self.primero=None
        
    def insertar(self, terreno):
        if self.primero is None:
            self.primero = nodo(terreno=terreno)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(terreno=terreno)
    def recorrer(self):
        actual= self.primero
        while actual != None:
            print("Nombre",actual.terreno.nombre,"Dimension:",actual.terreno.filas,", ",actual.terreno.columnas,"Posicion Inical:",actual.terreno.xPosInicio,", ",actual.terreno.yPosInicio,"Posicion Final: ",actual.terreno.xPosFinal,", ",actual.terreno.yPosFinal)
            actual=actual.siguiente



        