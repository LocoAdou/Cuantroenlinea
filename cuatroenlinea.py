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


secuencia = [7, 4, 2, 1, 4]
if validar_secuencia(secuencia):
    dibujar_tablero(completar_tablero_orden(secuencia, tablero_vacio()))
else:
    print("Secuencia no válida, las columnas deben estar entre los valores 1 al 7")