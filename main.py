class Nodo:
    def __init__(self, valor, izq=None, der = None):
        self.valor = valor
        self.izq = izq
        self.der = der

def sumar(arbol):
    if arbol == None: return 0
    return sumar(arbol.izq) + arbol.valor + sumar(arbol.der)
    
def a_lista(arbol):
    if arbol == None: return []
    return a_lista(arbol.izq) + [arbol.valor] + a_lista(arbol.der)
    
def buscar(arbol, valor):
    if arbol == None: return False
    if arbol.valor == valor: return True
    if arbol.valor < valor: return buscar(arbol.der, valor)
    return buscar(arbol.izq, valor)

def insert(arbol, data):
    if arbol is None: 
        return Nodo(data)
    else: 
        if data < arbol.valor:
            return Nodo(arbol.valor, insert(arbol.izq, data), arbol.der)
        return Nodo(arbol.valor, arbol.izq, insert(arbol.der, data))

def listToTree(arbol, list):
    for x in list:
        insert(arbol, x)
