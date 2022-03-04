import random

if __name__ == '__main__':

    diccionario = ["perro", "gato", "gallina", "dinisaurio"]

escenario = \
    '''   
    |
    |
    |
 0123456   
  
'''

simbolos = '\(X-X)/'

#bienvenida 
print( "hola,¿Quieres jugar al ahorcado?\n" )
print("PISTA: Empieza con una de las vocales mas usadas")

#1
def inicializar(diccionario):
    palabra = random.choice(diccionario).lower()
    tablero = ['_'] * len(palabra)
    return tablero, palabra, []

#2
def mostrar(errores):
    escena = escenario
    for i in range(0, len(simbolos)):
        simbolo = simbolos[i] if i < errores else ' '
        escena = escena.replace(str(i), simbolo)
    print(escena)

#3
def tablero(tablero, letras_erroneas):
    for casilla in tablero:
        print(casilla, end=' ')
    print()
    print()
    if len(letras_erroneas) > 0:
        print('Letras erróneas:', *letras_erroneas)
        print()

#4
def pedir_letra(tablero, letras_erroneas):
    valida = False
    while not valida:
        letra = input(" Introduce una letra entre (a-z) ").lower()
        valida = "a" <= letra <= "z" and len(letra) == 1 
        if not valida:
            print(" Error, la letra tiene que estar entre (a-z) ")
        else:
            valida = letra not in tablero + letras_erroneas
            if not valida:
                print("Letra repetida")

    return letra

#5
def procesar_letra(letra, palabra, tablero, letras_erroneas):
    if letra in palabra:
        print(" ¡Genial! ")
        tablero(letra, palabra, tablero)
    else:
        print(" Has fallado ")
        letras_erroneas.append(letra)


def actualizar_tablero(letra, palabra, tablero):
    for indice, letra_palabra in enumerate(palabra):
        if letra == letra_palabra:
            tablero[indice] = letra

#6
def comprobar_palabra(tablero):
    return '_' not in tablero

#juego
def jugar_al_ahorcado(diccionario):

    tablero, palabra, letras_erroneas = inicializar(diccionario) 
    while len(letras_erroneas) < len(simbolos): 
        mostrar(len(letras_erroneas)) 
        tablero(tablero, letras_erroneas)
        letra = pedir_letra(tablero, letras_erroneas) 
        procesar_letra(letra, palabra, tablero, letras_erroneas)
        if comprobar_palabra(tablero):
            print("¡Ganaste!")
            break
    else:
        print(f"¡Has perdido! La palabra a adivinar era {palabra}.")
        mostrar(len(letras_erroneas))  

    tablero(tablero, letras_erroneas)

#7
def despedida():
  print(input("gracias por jugar"))


