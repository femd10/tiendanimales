from tienda import *


t=Tienda()

t.agregar_animal(Perro("akita",2,50))
t.agregar_animal(Dragon("europeo",5000,1000000))
t.agregar_animal(Dragon("oriental",534323,245235))
t.agregar_animal(Gato("Mainecoon",10,6))
t.agregar_animal(Gato("naranja",24,4))
t.agregar_animal(Pez("mojarra",10,3))
t.agregar_animal(Ave("halcon",30,5))

for i in range (5):
    a= t.entregar_animal()
    print(a.saludar(), a.mostrar_informacion())
    