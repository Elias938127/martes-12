def cargar_datos():
    nom = []
    ed = []
    for x in range(5):
        v1 = input("ingrese el nombre de la persona")
        nom.append(v1)
        v2 =int(input("ingrese la edad:"))
        ed.append(v2)
    return[nom,ed]
def mayores_edad(nom,ed):
    print("nombres depersonas mayores de edad:")
    for x in range(len(nom)):
        if ed[x] >=18:
            print(nom[x])

def promedio_edades(ed):
    suma = 0
    for x in range(len(ed)):
        suma = suma + ed [x]
    promedio = suma //5
    print("edad promedio de las personas: " , promedio)

# bloque principal
nombres,edades = cargar_datos()
mayores_edad(nombres, edades)
promedio_edades(edades)
