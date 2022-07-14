#Programa 5:
#Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir
# una lista y retornar el mayor y el menor
#valor de la lista. Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista.

def carga_lista():
    li= []
    for x in range(5):
        valor=int(input("ingrese el valor:"))
        li.append(valor)
        return li

def imprimir_mayor10(li):
    print("elementos de la lista mayores a 10")
    for x in range(len(li)):
        if li[x]>10:
            print(li[x])

#bloque principal del programa

lista=carga_lista()
imprimir_mayor10(lista)
