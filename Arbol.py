'''

Titulo: Estructura que me permite almacenar datos (Arbol)
Autor : Gonzalo Tarqui Ignacio
Fecha : 03/10/2022
Version: 3.0

'''
from tkinter import *

from Nodo import Node
#.llama a la calse Nodo
from collections import deque
#. class Arbol
class Arbol:

    root = Node
    '''metodo que crea la instancia de la clase'''
    def __init__(self):
        self.__root = None
        self.__amplitud = 0
        self.__altura = 0
        self.__nivel = 0
        self.__cantidad = 0
        self.master = None
    
    def getRoot(self):
        '''selector de la raiz'''
        return self.__root; 

    def setRoot(self, x):
        '''modificador de la raiz'''
        self.__root = x

    def getAmplitud(self):
        '''selector del atributo amplitud'''
        return self.__amplitud; 

    def setAmplitud(self, x):
        '''modificador del atributo amplitud'''
        self.__amplitud = x

    def getNivel(self):
        '''selector del atributo nivel'''
        return self.__nivel; 

    def setNivel(self, x):
        '''modificador del atributo nivel'''
        self.__nivel = x

    def getAltura(self):
        '''selector del atributo altura'''
        return self.__altura;

    def setAltura(self, x):
        '''modificador del atributo altura'''
        self.__altura = x

    def getCantidad(self):
        '''selector del atributo cantidad'''
        return self.__cantidad; 
    def setCantidad(self, x):
        '''modificador del atributo cantidad'''
        self.__cantidad = x 


    def esVacio(self):
        '''funcion que devuelve true si esta vacio el nodo raiz'''
        return self.getRoot() is None
    def esVacio2(self, nodo):
        '''funcion que devuelve si el nodo esta vacio , ingresando el nodo'''
        if (nodo is None):
            return True
        else:
            return False


    def esHoja(self, nodo):
        '''metodo que devuelve true si el nodo es hoja'''
        if(nodo.getLeft() is None and
           nodo.getRight() is None):
              return True
        else:
              return False   


    def Additerativo(self, dato):   #. ingresa el 100 , 50   , 25 , 60 , 100
        nodo = Node(dato)             #.nuevo dato
        if(self.esVacio()):         #, no esta vacio ; sigue apunta a la raiz
            self.setRoot(nodo)
        else: 
            aux = self.getRoot()     # 100
            while(aux is not None and aux.getData() != dato ):      # 100!=100 and aux.getData() != dato
                if(dato < aux.getData()):   # 25<100   60<100
                    if(aux.getLeft() is None):  # su hijo izquierdo esta vacio?
                        aux.setLeft(nodo)
                    else:
                        #lo que hacemos aca es avanzar al siguiente     
                        aux = aux.getLeft()  # ahora es 50

                else:
                    if(aux.getRight() is None):  # su hijo derecho esta vacio?
                        aux.setRight(nodo)
                    else:
                        #lo que hacemos aca es avanzar al siguiente     
                        aux = aux.getRight() 


  
    def InsertarNodo(self,dato):
        '''metodo que inserta un nodo a la raiz'''
        nodo1 = Node(dato)
        if (self.esVacio()):
            self.setRoot(nodo1)
        else:
            self.addrecursivo1(self.getRoot(),dato)

    def addrecursivo1(self,nodoraiz,dato):
        '''parte del metodo InsertarNodo'''
        if ( nodoraiz is not None ):
            if (dato < nodoraiz.getData()):
                if (nodoraiz.getLeft() is None):
                    nodoraiz.setLeft(Node(dato))
                else:
                    self.addrecursivo1(nodoraiz.getLeft(),dato)
            else:
                if (dato > nodoraiz.getData()):
                    if (nodoraiz.getRight() is None):
                        nodoraiz.setRight(Node(dato))
                    else:
                        self.addrecursivo1(nodoraiz.getRight(),dato)
    
    def buscar(self,dato):
        '''metodo que busca un elemento en el arbol'''
        if (self.esVacio()):
            return None
        else:
            return self.buscar1( self.getRoot(),dato )

    def buscar1(self,nodoraiz,dato):
        '''parte del emtodo busqueda'''
        if (nodoraiz is not None):
            if (nodoraiz.getData()  == dato):
                return nodoraiz
            else: 
                if(dato < nodoraiz.getData()):
                    return self.buscar1(nodoraiz.getLeft(),dato)
                else:
                    return self.buscar1(nodoraiz.getRight(),dato)
        else:
            return Node(-1) # si no pilla retorna -1, pero deberia ser None

    def buscariterativo(self,dato):
        '''metodo buscar de forma itereativa'''
        if(self.esVacio()):
            return None 

        else:
            nav = self.getRoot()
            while(nav is not None):
                if (nav.getData() == dato):
                    return nav
                else:
                    if (dato < nav.getData()):
                        nav = nav.getLeft()
                    else:
                        nav = nav.getRight()
        return Node(-1) # si no pilla retorna -1, pero deberia ser None
    
    def inOrden(self, nodo):
        '''metodo de ordemaniento in orden'''
        if(  nodo is not None ):
                self.inOrden(nodo.getLeft())
                print(nodo.getData())
                self.inOrden(nodo.getRight()) 
    def inOrden1(self):
        self.inOrden(self.getRoot())


    def DIBUJARinOrden(self, nodo,masters,lienzos,x,y,fe):
        
        '''metodo de ordemaniento in orden'''
        if(  nodo is not None ):
                #.crea el circulo para el nodo
                lienzos.create_oval( x, y , x + 30 ,y + 30,width=2,fill='white')
                t = str(nodo.getData())
                #.crea el numero del nodo
                lienzos.create_text(x+14, y+14, text=t, fill="black", font=('Helvetica 10 bold'))

                #.CREA LAS LINEAS HACIA LOS HIJOS
                lienzos.create_line(x  +5   , y + 25, x -20  , y+40,  width=2, fill='black')

                lienzos.create_line(x + 25, y + 25, x +40  , y+40,  width=2, fill='red')


                self.DIBUJARinOrden(nodo.getLeft() ,masters,lienzos,(x-60+fe),y+30,fe+20)
                #print(nodo.getData())
                
                self.DIBUJARinOrden(nodo.getRight(),masters,lienzos,(x+60-fe),y+30,fe+20) 


    def dibujar_in_orden(self,masters,lienzos):
        self.master=masters
        #lienzos = Canvas(self.master) 
        #Button(self.master,text='Ad' ).pack()

        lienzos.pack(expand=YES,fill=BOTH)
        
        self.DIBUJARinOrden(self.getRoot(),masters,lienzos,200,20,0)




    # Función iterativa para realizar un recorrido posorden en el árbol
    def postorderIterative(self,root):
    
        # regresa si el árbol está vacío
        if root is None:
            return
    
        # crea una stack vacía y empuja el nodo raíz
        stack = deque()
        stack.append(root)
    
        # crea otra stack para almacenar el recorrido posterior al pedido
        out = deque()
    
        # Bucle # hasta que la stack esté vacía
        while stack:
    
            # saca un nodo de la stack y envía los datos a la stack de salida
            curr = stack.pop()
            out.append(curr.getData())
    
            # empuja el hijo izquierdo y derecho del nodo emergente en la stack
            if curr.getLeft():
                stack.append(curr.getLeft())
    
            if curr.getRight():
                stack.append(curr.getRight())
    
        # recorrido posterior al pedido de impresión
        while out:
            print(out.pop(), end=' ')
    
   



    def preOrden(self, nodo):
        '''metodo de ordenamiento preorden'''
        if(nodo is not None):
                print(nodo.getData())
                self.preOrden(nodo.getLeft())
                self.preOrden(nodo.getRight())

    def postOrden(self, nodo):
        '''metodo de ordenamiento post orden'''
        if(nodo is not None):
                self.postOrden(nodo.getLeft())
                self.postOrden(nodo.getRight())
                print(nodo.getData())

    def altura(self,nodoraiz):
        '''metodo que devuelve la altura del arbol'''
        if ( nodoraiz is None):
            return 0
        return 1 + max(self.altura( nodoraiz.getLeft()) , self.altura(nodoraiz.getRight()) )

    def cantidad(self,nodoraiz):
        '''metodo que devuelve la cantidad de nodos que tiene un arbol'''
        if (nodoraiz is None ):
            return 0
        return 1 + self.cantidad( nodoraiz.getLeft()) + self.cantidad(nodoraiz.getRight()) 

    def amplitud(self,nodoraiz):
            if (self.esVacio2(nodoraiz)):
                return 0
            if (self.esHoja(nodoraiz)):
                return 1 
            return self.amplitud( nodoraiz.getLeft()) + self.amplitud(nodoraiz.getRight())



    def ARBOLAVL(self, nodo):
        '''metodo que retorna un arbol valanceado por rotacion simple o doble LEFT - RIGHT'''
        alturaLeft= self.altura(nodo.getLeft())
        alturaRight = self.altura(nodo.getRight())
        #.la altura de los nodos derechos e izqu
        if ( (alturaLeft-alturaRight) > 1 ):
            nodoLeft = nodo.getLeft()

            if ( self.altura( nodoLeft.getRight() ) > self.altura( nodoLeft.getLeft()) ):
                return self.rotacionDobleDerecha(nodo)
            else:
                return self.rotacionDerecha(nodo)
        
        else:

            if ( (alturaRight - alturaLeft) > 1):
                nodoRight = nodo.getRight()
                if ( self.altura(nodoRight.getLeft()) > self.altura( nodoRight.getRight()) ):
                    return self.rotacionDobleIzquierda(nodo)

                else:
                    return self.rotacionIzquierda(nodo)
        return nodo



#.rotacion simple izquierda
    def rotacionIzquierda(self, nodo):                          
        '''metodo que rotacion simple hacia la izquierda
        cuando el subarbol izquierdo del hijo izquierdo del nodoX  es mas
        grande que el hijo derecho del nodoX'''
        newNodo = nodo.getRight()
        nodo.setRight( newNodo.getLeft() )
        newNodo.setLeft(nodo)
        return newNodo

    def rotacionDerecha(self,nodo):
        '''metodo que rotacion simple hacia la derecha
            cuando el subarbol derecho del hijo derecho del nodoX 
            es masn grande que el hijo izquierdo del nodoX'''
        newnodo = nodo.getLeft()
        nodo.setLeft( newnodo.getRight())
        newnodo.setRight(nodo)
        return newnodo

    def rotacionDobleIzquierda(self,nodo):
        '''metodo que rota doble a la izquierda cuando
           el subarbol izquierdo del hijoderecho del nodoX es mas grande que 
           el hijo izquierdo del nodoX'''
        nodo.setRight(self.rotacionDerecha( nodo.getRight()))
        return self.rotacionIzquierda(nodo)

    def rotacionDobleDerecha(self,nodo):
        ''' metodo que rota doble a la derecha cuando
        el subarbol derecho del hijo izquierdo del nodoX es mas grande que 
        el hijo derecho del nodoX '''
        nodo.setLeft(  self.rotacionIzquierda(nodo.getLeft()) )
        return self.rotacionDerecha(nodo)


#.-------------------------------------------------------------------------


    def getMinimumKey(self, subar):
        '''funcion que devuelve el minimo en el subarbol'''
        while subar.getLeft():
            subar = subar.getLeft()
        return subar


    def deleteNode(self, root, key):
        ''' funcion que elimina el nodo key del arbol root'''
 
        # Puntero # para almacenar el padre del nodo actual
        parent = None
    
        # comienza con el nodo raíz
        curr = root
    
        # Clave de búsqueda # en el BST y establezca su puntero principal
        while curr and curr.getData() != key:
    
            # actualiza el padre al nodo actual
            parent = curr
    
            # si la clave dada es menor que el nodo actual, vaya al subárbol izquierdo;
            # de lo contrario, ve al subárbol derecho
            if key < curr.getData():
                curr = curr.getLeft()
            else:
                curr = curr.getRight()
    
        # retorno si no se encuentra la clave en el árbol
        if curr is None:
            return root
    
        # Caso 1: el nodo a eliminar no tiene hijos, es decir, es un nodo hoja
        if curr.getLeft() is None and curr.getRight() is None:
    
            # si el nodo a eliminar no es un nodo raíz, configure su
            # padre izquierdo/derecho hijo a Ninguno
            if curr != root:
                if parent.getLeft() == curr:
                    parent.setLeft(None)
                else:
                    parent.setRight(None)
    
            # si el árbol solo tiene un nodo raíz, configúrelo en Ninguno
            else:
                root = None
    
        # Caso 2: el nodo a eliminar tiene dos hijos
        elif curr.getLeft() and curr.getRight():
            # encuentra su nodo sucesor en orden
            successor = self.getMinimumKey(curr.getRight())
    
            # Valor del sucesor de la tienda
            val = successor.getData()
    
            # elimina recursivamentemente al sucesor. Nótese que el sucesor
            # tendrá como máximo un hijo (hijo derecho)
            self.deleteNode(root, successor.getData())
    
            # copia el valor del sucesor del nodo actual
            curr.setData(val) 
    
        # Caso 3: el nodo a eliminar solo tiene un hijo
        else:
    
            # elige un nodo secundario
            if curr.getLeft():
                child = curr.getLeft()
            else:
                child = curr.getRight()
    
            # si el nodo a eliminar no es un nodo raíz, configure su padre
            # a su hijo
            if curr != root:
                if curr == parent.getLeft():
                    parent.setLeft( child)
                else:
                    parent.setRight( child)
    
            # si el nodo que se va a eliminar es un nodo raíz, establezca la raíz en el hijo
            else:
                root = child
 
        return root

    def avl( self):
        self.setRoot(self.ARBOLAVL( self.getRoot()))

    def deleteNodevalue(self, value):
        self.setRoot(self.deleteNode(self.getRoot(),value ))


    def preOrdenDirect(self):
        self.preOrden(self.getRoot())

        
def main():
    pass
if __name__ == '__main__':
    main()        
    


 