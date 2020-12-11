
import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Log10(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("LOG_10")
        print(math.log10(self.valor))
        return math.log10(self.valor)

instruccion = Log10(10,None, 1,2)

instruccion.ejecutar(None,None)