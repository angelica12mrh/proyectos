import random

escenario = \
    '''   
    |
    |
    |
 0123456   
  
'''

simbolos = '\(X-X)/'


def bienvenida():
    print('*' * 68)
    print('* Te doy la bienvenida al juego del ahorcado de codigopiton.com :) *')
    print('*' * 68)


# paso 1
def inicializar_juego(diccionario):
    palabra = random.choice(diccionario).lower()
    tablero = ['_'] * len(palabra)
    return tablero, palabra, []


# paso 2
def mostrar_escenario(errores):
    escena = escenario
    for i in range(0, len(simbolos)):
        simbolo = simbolos[i] if i < errores else ' '
        escena = escena.replace(str(i), simbolo)
    print(escena)


# paso 3
def mostrar_tablero(tablero, letras_erroneas):
    for casilla in tablero:
        print(casilla, end=' ')
    print()
    print()
    if len(letras_erroneas) > 0:
        print('Letras erróneas:', *letras_erroneas)
        print()


# paso 4
def pedir_letra(tablero, letras_erroneas):
    valida = False
    while not valida:
        letra = input('Introduce una letra (a-z): ').lower()
        valida = 'a' <= letra <= 'z' and len(letra) == 1 # es una letra
        if not valida:
            print('Error, la letra tiene que estar entre a y z.')
        else:
            valida = letra not in tablero + letras_erroneas
            if not valida:
                print('Letra repetida, prueba con otra.')

    return letra


# paso 5
def procesar_letra(letra, palabra, tablero, letras_erroneas):
    if letra in palabra:
        print('¡Genial! Has acertado una letra.')
        actualizar_tablero(letra, palabra, tablero)
    else:
        print('¡Oh! Has fallado.')
        letras_erroneas.append(letra)


# paso 5 (auxiliar)
def actualizar_tablero(letra, palabra, tablero):
    for indice, letra_palabra in enumerate(palabra):
        if letra == letra_palabra:
            tablero[indice] = letra


# paso 6
def comprobar_palabra(tablero):
    return '_' not in tablero


# bucle principal de juego
def jugar_al_ahorcado(diccionario):

    tablero, palabra, letras_erroneas = inicializar_juego(diccionario)  # paso 1
    while len(letras_erroneas) < len(simbolos):  # pasos 7 y 8
        mostrar_escenario(len(letras_erroneas))  # paso 2
        mostrar_tablero(tablero, letras_erroneas)  # paso 3
        letra = pedir_letra(tablero, letras_erroneas)  # paso 4
        procesar_letra(letra, palabra, tablero, letras_erroneas)  # paso 5
        if comprobar_palabra(tablero):  # paso 6
            print('¡Enhorabuena, lo has logrado!')
            break
    else:
        print(f'¡Lo siento! ¡Has perdido! La palabra a adivinar era {palabra}.')
        mostrar_escenario(len(letras_erroneas))  # paso 7

    mostrar_tablero(tablero, letras_erroneas)


def jugar_otra_vez():
    return input('Deseas jugar otra vez (introduce s para sí o cualquier otra cosa para no): ')


def despedida():
    print('*' * 68)
    print('* Gracias por jugar al ahorcado de codigopiton.com. ¡Hasta pronto! *')
    print('*' * 68)


if __name__ == '__main__':

    diccionario = ['casa', 'pescado', 'calamar', 'monigote', 'codigopiton']

    bienvenida()
    while True:
        jugar_al_ahorcado(diccionario)
        if jugar_otra_vez() != 's': break
    despedida()