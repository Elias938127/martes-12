#Confeccionar un programa que permita:
# Cargar una lista de 10 elementos enteros.
# Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
# Imprimir las dos listas generadas.

def cargar():
    lista= []
    for x in range(10):
        valor = int(input("ingrese un valor:"))
        lista.append(valor)
    return lista

def generar_listas(listas):
    listanega=[]
    listaposi=[]
    for x in range(len(listas)):
        if listas[x]<0:
            listanega.append(listas[x])
        else:
            if listas[x]>0:
                listaposi.append(listas[x])
    return [listanega,listaposi]

def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x])






#bloque principal
lista=cargar()
listanega,listaposi=generar_listas(lista)
print("lista con los valores negativos")
imprimir(listanega)
print("lista con los valores positivos")
imprimir(listaposi)
