def tablero_vacio():
     return [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
            ]

def completar_tablero_orden(secuencia, tablero):
    for jugador, columna in enumerate(secuencia):
        ficha_j = jugador % 2 + 1
        soltar_ficha(ficha_j,columna,tablero)
    return tablero
            
def soltar_ficha(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            return            

def dibujar_tablero(tablero):
    for fila in tablero:
        for columna in fila:
            if columna == 0:
                print('   ', end='')
            else:
                print(' %s ' %columna, end='')
        print('')
            
def validar_secuencia(secuencia):
    for columna in secuencia:
        if columna < 1 or columna > 7:
            return False
    return True

def contenido_columna(nro_columna, tablero):
    columna = []   
    for fila in tablero:
        celda = fila[nro_columna-1]
        columna.append(celda)
    return columna

def contenido_fila(nro_fila, tablero):
    return tablero[nro_fila-1]
    
secuencia = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]

tablero = []
if validar_secuencia(secuencia):
    tablero =completar_tablero_orden(secuencia, tablero_vacio())
    dibujar_tablero(tablero)

    print(contenido_columna(2, tablero))
#    print("%s",)
    print(contenido_fila(1, tablero))
else:
    print("Secuencia no válida, las columnas deben estar entre los valores 1 al 7")