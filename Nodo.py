'''

Titulo: Estructura que me permite almacenar datos (Nodo)
Autor : Gonzalo Tarqui Ignacio
Fecha : 28/09/2022
Version: 2.7

'''
#. class Nodo
class Node:

    def __init__(self, value, padre=None):
        self.__left = None
        self.__right = None
        self.__data = value
        self.__padre = padre


    def getData(self):
        '''selector del atributo raiz'''
        return self.__data; 

    def setData(self, x):
        '''selector del atributo data'''
        self.__data = x

    def getLeft(self):
        '''selector del atributo izquierdo'''
        return self.__left; 

    def setLeft(self, x):
        '''modificador del atributo izquierdo'''
        self.__left = x
        
    def getRight(self):
        '''selector del atributo hijo derecho'''
        return self.__right; 

    def setRight(self, x):
        '''modificador del atributo hijoDer'''
        self.__right = x
        

    def getPadre(self):
        '''selector del padre si es que utiliza'''
        return self.__padre; 

    def setPadre(self, x):
        '''modificador del atributo padre'''
        self.__padre = x

    def __str__(self) -> str:
        return self.getData()
    


def main():
  pass
  

if __name__ == '__main__':
    main()
   



    
