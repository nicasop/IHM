### PRACTICA 1 ###
#Integrantes Sebastian Sandova - Alexis Villavicencio

def mostrarNotas(lista):
    for i in range(len(lista)):
        print('nota:',lista[i]["nota"],' --> peso:',lista[i]["peso"])

def mediaPonderada(lista):
    mP = 0
    for i in range(len(lista)):
        mP += lista[i]["nota"] * lista[i]["peso"]
    return round(mP,2)

def sumarPesos(lista, peso=0):
    suma = peso
    for i in range(len(lista)):
        suma += lista[i]["peso"]
    return round(suma,2)

def validarPeso(lista):
    if sumarPesos(lista) >= 1:
        print("La suma de los pesos ingresados anteriormente ha llegado al 100%. El peso de la nota ingresada sera de 0%")
        peso = 0
    else:
        if len(lista) == 0:
            while True:
                peso = int(input("Ingreso el peso en porcentajes enteros por ejemplo 40%: "))/100
                if 0 <= peso < 1:
                    break
                else:
                    print('El peso no puede ser inferior a 1% y superior a 100%')
        else:
            while True:
                peso = int(input("Ingreso el peso en porcentajes enteros por ejemplo 40%: "))/100
                if 0 <= peso < 1:
                    if 0 <= sumarPesos(lista, peso) <= 1:
                        break
                    else:
                        print('La suma del peso ingresado y los anteriores supera el 100%. Solo puede agregar un peso de',int(round(1-sumarPesos(lista),2)*100),'%')
                        if not (True if input('Desea ingresar otro peso. En caso de elegir no se asignará el peso restante mostrado anteriormente (s/n): ').lower() == 's' else False):
                            peso = round(1-sumarPesos(lista),2)
                            break
                else:
                    print('El peso no puede ser inferior a 1% y superior a 100%')
    return peso

notas = []
print('Ingrese las notas y sus respectivos pesos')
while True:
    nota = float(input("Ingrese la nota: "))
    peso = validarPeso(notas)
    objeto = {
        "nota": nota,
        "peso": peso
    }
    notas.append(objeto)
    if not (True if input('Desea ingresar otra nota(s/n): ').lower() == 's' else False):
        pesoFinal = sumarPesos(notas)
        if pesoFinal < 1:
            print('La suma de los pesos no ha alcanzado el 100% es necesario ingresar al menos una nota más. El valor del peso disponible es de',int(round(1 - pesoFinal,2)*100),'%')
        else:
            break
print('Notas ingresadas con sus respectivos pesos')
mostrarNotas(notas)
print('La media ponderada de las notas ingresadas es: ',mediaPonderada(notas))