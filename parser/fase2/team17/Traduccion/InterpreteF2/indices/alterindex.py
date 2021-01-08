from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Reporteria.ReporteTS_Indice import ReportIndice


class alterindex(NodoArbol):

    def __init__(self, name, newname , line, coliumn):
        super().__init__(line, coliumn)
        self.name = name
        self.rename = newname

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        i=0
        while i < len(arbol.ReporteTS_Indices):
            report:ReportIndice = arbol.ReporteTS_Indices[i]
            if str(report.nombre) == str(self.name):
                arbol.ReporteTS_Indices[i].nombre = str(self.rename)
                arbol.ReporteTS_Indices[i].alias = str(self.rename)
                return
            i+=1



    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        pass