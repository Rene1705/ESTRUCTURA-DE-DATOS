class NodoBST:  
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
      
def insertar _en_bst(raiz, valor):
    if raiz is None:
        return NodoBST(valor)
    else:
       if valor < raiz.valor:
          raiz.izquierdo = insetar_en_bst(raiz.izquierdo, valor)
    else:
        raiz.derecho = insertar_en_bst(raiz.derecho, valor)
    return raiz

def lista_a_bst(lista):
    raiz = None
    for valor in lista:
        raiz = insertar_en_bst(raiz, valor)
    return raiz

def imprimir_bst(raiz):
    if raiz is not None:
        imprimir_bst(raiz.izquierdo)
        print(raiz.valor, end= ' ')
        imprimir_bst(raiz.derecho)


lista = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]


arbol = lista_a_bst(lista)


imprimir_bst(arbol)
