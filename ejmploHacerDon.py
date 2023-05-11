
def hacer_don(lista):
    for i in range(len(lista)):
        lista[i] = "Don " + lista[i]

    #print(lista)
    return lista


datos = ["Luis","Pedro","Fernando","Víctor"]

datos_con_don  = hacer_don(datos)

print(datos_con_don)
