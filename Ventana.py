from Arbol import Arbol
#.llama a la clase Arbol


# importacion de la libreria Tkinter para invocar el modo grafico
from tkinter import *
# Implementacion de la clase grafica Ventana
class Ventana(object):
    # Metodo que instancia la clase Ventana e inicializa el modo grafico
    def __init__(self,master):
        self.tree = Arbol()
        self.master = master #Instancias de Widget sobre lo que se va pintar
        #self.master.geometry('400x500+0+0')
        self.inicializar_gui()
      
        self.lienzo = Canvas(self.master,width=500,height=600) # Canvas objeto que permite pintar
        
    # creamos los widget dentro del canvas       
    def inicializar_gui(self):
        Button(self.master,text='Dibujar',command=lambda: (self.circulo() ) ).pack()
        Button(self.master,text='limpiar',command=lambda: (self.limpiar() ) ).place(x=10,y=10)
        Button(self.master,text='AVL',command=lambda: (self.AVL() ) ).place(x=60,y=10)
        Button(self.master,text='DELETE',command=lambda: (self.DELETE( dato.get() ) ) ).place(x=95,y=10)
        Button(self.master,text='Agregar nodo',command=lambda: ( self.addnodo(dato.get()) ) ).pack()
        dato = IntVar()
        dato.set(100)

        ADD = Entry(self.master,textvariable=dato).pack()
        self.crear_menu()


    def crear_menu(self):
        '''crea el menu principal'''
        self.miMenu = Menu(self.master)
        self.barraMenu = Menu(self.miMenu, tearoff=0)
        self.barraMenu.add_command(label='Abrir')
        self.miMenu.add_cascade(label='Archivo',menu=self.barraMenu)
    

    def circulo(self):
        '''funcion que crea un circulo con canvas en el lienzo'''
        #self.tree.InsertarNodo(100)
        #self.tree.InsertarNodo(200)
        #self.tree.InsertarNodo(50)
        #self.tree.InsertarNodo(60)
        #self.tree.InsertarNodo(5)
        #self.tree.InsertarNodo(1)
        #self.tree.InsertarNodo(300)
        #self.tree.InsertarNodo(150)
        #self.lienzo.create_text(50, 10, text="HELLO WORLD", fill="black", font=('Helvetica 10 bold'))
        self.tree.dibujar_in_orden(self.master,self.lienzo)
        #self.lienzo.pack(expand=YES,fill=BOTH)
        #self.lienzo.create_oval( (self.ancho/2),20,((self.ancho/2)+30),50,width=2,fill='white')
    def addnodo(self,data):
        self.tree.InsertarNodo(data)
        
    def limpiar(self):
        '''funcion que limpia el lienzo -  canvas'''
        self.lienzo.delete('all') 
        self.tree = Arbol()
    def AVL(self):
        '''funcion que Balancea el Arbol AVL -  canvas'''
        self.tree.avl()  
        self.lienzo.delete('all') 
    def DELETE(self,data):
        '''funcion que elimina un dato de Arbol -  canvas'''
        self.tree.deleteNodevalue(data)  
        self.lienzo.delete('all') 

def main():
    master = Tk()
    master.title("Disenio Grafico ABB") 

    master.geometry('500x500+0+0') 
    
    MiVentana = Ventana(master)
    
    master.mainloop()     

if __name__ == "__main__":
    main()     