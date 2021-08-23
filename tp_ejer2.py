#Oscar Pedrozo
#ci: 4472036


def cerar(R,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            R[i][j] = 0


def godel(a,b):
    if a <= b :
        return 1
    else:
        return b

#Operador de Lukasiewicz
def lukasiewicz(a,b):
    return min(1, 1-a+b)

#Operador de Goguen
def goguen(a,b):
    if a <= b:
        return 1
    else:
        return b/a

#Interseccion drastica
def tnormDegenerada(x,y):
    if y == 1:
        return x
    elif x == 1:
        return y
    else:
        return 0

#     1    2   3    4   5
A = [0.3, 0.5, 1.0, 0.7, 0.2]

#   a    b     c   d    e     f
B= [0.3, 0.5, 0.8, 1.0, 0.0, 0.0]

filas = 5
columnas = 6
# El tamanho de A'
tamAA= 5
#     1   2    3   4    5
AA = [0.5,0.7,0.9, 0.5, 0.3]
#para el ejercicio resuelto 2
#Crear la matriz de godel de 3 filas x 2 columnas
R = [[0 for x in range(filas+1)] for y in range(columnas+1)]

#Crear la matriz de la relacion anterior usando Godel
for i in range(filas):
    for j in range(columnas):
        R[i][j] = godel(A[i],B[j])


#Para guardar los valores obtenidos en la interseccion drastica (T-norm degenerada)
aux = [0 for k in range(tamAA+1)]

print("Usando la relacion obtenida con Godel\nt-normas:Interseccion drastica")
#Hallar MAX
for j in range(columnas):
    for i in range(filas):
        aux[i] = tnormDegenerada(AA[i], R[i][j]) #Hallar el minimo de cada columna
    print("%0.2f"%max(aux))    #El maximo de la columna


print("Usando la relacion obtenida con Godel\nt-normas:Diferencia limitada")
#Hallar MAX
for j in range(columnas):
    for i in range(filas):
        #diferencia limitada (Lukasiewicz)
        aux[i] = max(0,AA[i] +R[i][j] -1) #Hallar el minimo de cada columna
    print("%0.2f"%max(aux))    #El maximo de la columna



cerar(R,filas,columnas)    
#crear la matriz con Lukasiewicz
for i in range(filas):
    for j in range(columnas):
        R[i][j] = lukasiewicz(A[i],B[j])



print("Usando la relacion obtenida con Lukasiewicz\nt-normas:Interseccion drastica")
#Hallar MAX
for j in range(columnas):
    for i in range(filas):
        aux[i] = tnormDegenerada(AA[i], R[i][j]) #Hallar el minimo de cada columna
    print("%0.2f"%max(aux))    #El maximo de la columna


print("Usando la relacion obtenida con Lukasiewicz\nt-normas:Diferencia limitada")
#Hallar MAX
for j in range(columnas):
    for i in range(filas):
        #diferencia limitada (Lukasiewicz)
        aux[i] = max(0,AA[i] +R[i][j] -1) #Hallar el minimo de cada columna
    print("%0.2f"%max(aux))    #El maximo de la columna




cerar(R,filas,columnas)
#crear la matriz con Goguen
for i in range(filas):
    for j in range(columnas):
        R[i][j] = goguen(A[i],B[j])


print("Usando la relacion obtenida con Goguen\nt-normas:Interseccion drastica")
#Hallar MAX
for j in range(columnas):
    for i in range(filas):
        aux[i] = tnormDegenerada(AA[i], R[i][j]) #Hallar el minimo de cada columna
    print("%0.2f"%max(aux))    #El maximo de la columna


print("Usando la relacion obtenida con Goguen\nt-normas:Diferencia limitada")
#Hallar MAX
for j in range(columnas):
    for i in range(filas):
        #diferencia limitada (Lukasiewicz)
        aux[i] = max(0,AA[i] +R[i][j] -1) #Hallar el minimo de cada columna
    print("%0.2f"%max(aux))    #El maximo de la columna




