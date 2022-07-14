#Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. Si hay más
#de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja. En el
#bloque principal iniciamos por asignación la lista de string.

def mascaracteres(lista):
    pos =0
    for x in range(1,len(lista)):
        if len(lista[x])>len(lista[pos]):
            pos=x
    return lista[pos]





#bloque principal
palabras=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
print(palabras)
print("palabras con mas caracteres:" ,mascaracteres(palabras))