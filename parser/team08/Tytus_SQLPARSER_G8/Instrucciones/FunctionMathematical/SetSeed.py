import math
import random
from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class SetSeed(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        #print(random.seed(self.valor))
        arbol.consola.append('Función en proceso...')
