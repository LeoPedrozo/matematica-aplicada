#Oscar Pedrozo
#ci: 4472036

#Operador de Godel
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

#     1    2   3    4   5
A = [0.3, 0.5, 1, 0.7, 0.2]

#   a    b     c   d  e  f
B= [0.3, 0.5, 0.8, 1, 0, 0]


#Obs. Los valores estan formateados para mostrar
# 3 decimales
print("imprimir en forma matricial Godel")
for a in A:
    for b in B:
        print("%0.2f"%godel(a,b),end='\t\t')
    print()

print("imprimir en forma matricial Lukasiewicz")
for a in A:
    for b in B:
        print("%0.2f"%lukasiewicz(a,b),end='\t\t')
    print()

print("imprimir en forma matricial Goguen")
for a in A:
    for b in B:
        print("%0.2f"%goguen(a,b),end='\t\t')
    print()