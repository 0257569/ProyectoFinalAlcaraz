
class Nodo:
    def __init__ (self, valor):
        self.valor = valor
        self.padre = None
        self.izquierdo = None
        self.derecho = None

class Arbol:
    def __init__ (self):
        self.raiz = None
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.raiz:
            self.raiz = nuevo
            return nuevo
        explorador = self.raiz
        while True:
            if valor < explorador.valor:
                if explorador.izquierdo:
                    explorador = explorador.izquierdo
                else:
                    explorador.izquierdo = nuevo
                    nuevo.padre = explorador
            elif valor > explorador.valor:
                if explorador.derecho:
                    explorador = explorador.derecho
                else:
                    explorador.derecho = nuevo
                    nuevo.padre = explorador
                    return nuevo
            else: return explorador

    def inorden(self, nodo):
        if not nodo: return []
        return self.inorden(nodo.izquierdo)+[nodo.valor]+self.inorden(nodo.derecho)
    def buscar (self, valor): 
        explorador = self.raiz
        while True:
            if not explorador:
                return None
            if explorador.valor == valor:
                return explorador
            elif valor<explorador.valor:
                explorador = explorador.izquierdo
            else:
                explorador = explorador.derecho
    def anterior(self, valor):
        explorador = self.buscar(valor)
        if explorador.izquierdo:
            explorador = self.maximo(explorador.izquierdo)
        return explorador.valor

    def siguiente(self, nodo):
        explorador = nodo
        if explorador.derecho:
            explorador = self.minimo(explorador.derecho)
        return explorador.valor
    def minimo(self, nodo):
        explorador = nodo
        while True:
            if explorador.izquierdo:
                explorador = explorador.izquierdo
            else:
                return explorador
    def maximo(self, nodo):
        explorador = nodo
        while True:
            if explorador.derecho:
                explorador = explorador.derecho
            else:
                return explorador
    def buscarNivel(self, nodo):
        nivel = 0
        explorador = nodo
        while explorador != self.raiz:
            if explorador.padre:
                explorador = explorador.padre
                nivel += 1
        return nivel
    def profundidad(self):
        profundidad = self.buscarNivel(self.raiz)
        for basura in self.inorden(self.raiz):
            if self.buscarNivel(self.buscar(basura)) > profundidad:
                profundidad = self.buscarNivel(self.buscar(basura))
        return profundidad
        

arbol = Arbol()
valores = [34, 15, 80, 7, 21, 30, 42, 100]
for valor in valores:
    arbol.insertar(valor)
print(arbol.profundidad())
print(2**(arbol.profundidad()))
for i in range(3):
    print(i)