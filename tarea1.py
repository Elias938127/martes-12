#Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros. Implementar una
#función que imprima el mayor y el menor valor de la lista.


def mayormenor(lista):
    may=lista[0]
    men=lista[0]
    for x in range(1, len(lista)):
        if lista[x] > may:
            may=lista[x]
        else:
            if lista[x] < men:
                men= lista[x]
    print("el valor mayor de la lista es ", may)
    print("el valor menor de la lista es ", men)

# bloque principal
lista=[]
for x in range(5):
    valor=int(input("ingrese el valor:"))
    lista.append(valor)
mayormenor(lista)