import random

#Cambiar tecla por posicion en la matriz
def getPos(key):
    keys = {"7":[0,0], "8":[0,1], "9":[0,2], "4":[1,0], "5":[1,1], "6":[1,2], "1":[2,0], "2":[2,1], "3":[2,2]}
    try:
        return keys[key]
    except KeyError:
        return None

def printIntro(introFile):
    '''
        Firma:
            (string) -> ()

        Sinopsis:
            función que imprime el contenido de un archivo en pantalla, en este
    		caso, el mensaje de bienvenida al juego

        Entradas y salidas:
            - inputFile: Nombre del archivo que contiene la presentación del juego
            - returns: None, solo imprime el archivo leído en pantalla

        Ejemplos de uso:

            >>> printIntro("intro.txt")

            ████████╗██████╗ ██╗ ██████╗ ██╗   ██╗██╗
            ╚══██╔══╝██╔══██╗██║██╔═══██╗██║   ██║██║
               ██║   ██████╔╝██║██║   ██║██║   ██║██║
               ██║   ██╔══██╗██║██║▄▄ ██║██║   ██║██║
               ██║   ██║  ██║██║╚██████╔╝╚██████╔╝██║
               ╚═╝   ╚═╝  ╚═╝╚═╝ ╚══▀▀═╝  ╚═════╝ ╚═╝
        '''

    # Desarrolle el cuerpo de la función aquí...

    archivo = open(introFile, "r")
    print(archivo.read())

def drawBoard(board):
    # Esta función imprime el tablero en la consola
    # Argumentos:
    # Board: Lista de strings que representa el estado del tablero

    # Desarrolle el cuerpo de la función aquí...

    tablero = ""
    for i in range(len(board)):
        tablero += (" "*20)
        for j in range(len(board[i])):
            tablero += " "+board[i][j]+" |"
        tablero = tablero[:-1]+"\n"
        tablero += (" "*20)+"---+---+---\n"
    tablero = tablero[:-13]
    print(tablero)

def inputPlayerLetter():
    # Esta función le permite escoger al usuario entre la letra "X" y la letra "O".

    # retorna una lista de strings donde la letra escogida por el usuario
    # ocupa la primera posición y la letra que le corresponde a la computadora
    # ocupa la segunda posición.

    # Desarrolle el cuerpo de la función aquí...
    letter = [0, 0]
    while True:
        letter[0] = input("Elije X u O: ")
        if letter[0] == "X":
            letter[1] = "O"
            break
        elif letter[0] == "O":
            letter[1] = "X"
            break
        else:
            print("Debes elegir entre la X y la O")
    return letter 
        
def whoGoesFirst():
    # Esta función escoge de forma aleatoria quien inicial el juego.

    # Retorna el string "Usuario" si el usuario inicia el juego o
    # el string "Computadora" si la computadora inicia el juego.

    # Desarrolle el cuerpo de la función aquí...

    turn = random.choice(["Usuario", "Computadora"])  # Indica quién tiene el turno para jugar, el usuario o la computadora.

    return turn

def makeMove(board, letter, move):
    # Esta función actualiza el estado del tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # letter: Es la marca que se desea poner en el tablero ("X" o "O").
    # move: Es el número de la casilla donde se desea poner la marca.

    # Desarrolle el cuerpo de la función aquí...
    board[move[0]][move[1]] = letter
    return board

def isWinner(board, letter):
    # Esta función debe verificar si hay una jugada ganadora en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # letter: La marca que se desea verificar ("X" o "O").

    # Esta función debe retornar el valor lógico True, si hay una jugada ganadora o
    # debe retornar el valor lógico False, si no hay una jugada ganadora.

    # Desarrolle el cuerpo de la función aquí...
    flag = False

    # Verificar si hay un ganador en las filas
    for i in board:
        if i == [letter]*3:
            flag = True
            break

    for i in range(len(board)):
        if [board[0][i], board[1][i], board[2][i]] == [letter]*3:
            flag = True
            break

    line = []
    for i in range(len(board)):
        line.append(board[i][i])
    if line == [letter]*3:
        flag = True

    line = []
    for i in range(len(board)):
        line.append(board[i][2-i])
    if line == [letter]*3:
        flag = True

    return flag


def isSpaceFree(board, move):
    # Esta función verifica si hay una casilla vacía en el tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # move: Es el número de la casilla que se desea verificar.

    # Esta función debe retornar el valor lógico True, si la casilla está vacía
    # en caso contrario, debe retornar el valor lógico False.

    # Desarrolle el cuerpo de la función aquí...
    if board[move[0]][move[1]] == " ":
        return True
    else:
        return False

def getPlayerMove(board):
    # Esta función le pide al usuario que ingrese el número de la casilla
    # que quiere marcar.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función retorna el número de la casilla seleccionada por el usuario.


    # Desarrolle el cuerpo de la función aquí...
    key = input("Ingrese un número del 1 al 9 para realizar un movimiento: ")
    while True:
        while getPos(key) == None:
            key = input("Ingrese un número del 1 al 9 para realizar un movimiento: ")

        print(getPos(key))
        if isSpaceFree(board, getPos(key)):
            return getPos(key)
        else:
            print("Debes seleccionar un espacio libre")
            key = "texto para que getPos me devuelva 0"


def chooseRandomMoveFromList(board, movesList):
    # Esta función escoge de forma aleatoria una casilla vacía del tablero.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # moveList: Lista que contiene los números de las casillas a verificar (ver documento de la práctica).

    # Esta función debe retornar alguno de los números de casillas en moveList
    # desde que dicha casilla esté vacía. Si ninguna de las casillas está vacía,
    # esta función debe retornar el valor None.

    # Desarrolle el cuerpo de la función aquí...
    posibleMoves = []
    for i in movesList:
        if board[i[0]][i[1]] == " ":
            posibleMoves.append(i)
    if len(posibleMoves) == 0:
        return None
    else:
        return random.choice(posibleMoves)

def getComputerMove(board, computerLetter):
    # Esta función implementa la estrategia de juego de la computadora.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.
    # computerLetter: La marca que está usando la computadora.

    # Desarrolle el cuerpo de la función aquí...

    playerLetter = {"X":"O", "O":"X"}

    print("otra cosa")
    # 1. Verificar si la computadora puede ganar...
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                board2 = []
                board2 = board.copy()
                board2[i][j] = computerLetter
                print(board2)
                if isWinner(board2, computerLetter):
                    print(i, j)
                    return [i, j]

    # 2. Si no, verificar si el usuario puede ganar en la siguiente jugada, si si, bloquear esta jugada...
    
    print("algo")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                board2 = board.copy()
                board2[i][j] = playerLetter[computerLetter]
                if isWinner(board2, playerLetter[computerLetter]):
                    return [i, j]

    # 3. Si no, tratar de poner una marca en alguna de las esquinas, si alguna está vacía...
    move = chooseRandomMoveFromList([[0,0],[0,2],[2,2],[2,0]])
    print(move)
    if move != None:
        return move
    # 4. Si no, tratar de marcar la casilla del centro, si esta está vacía...
    if board[1][1] == " ":
        return [1, 1]
    # 5. Si no, tratar de poner una marca en alguna de las casillas de los lados...
    move = chooseRandomMoveFromList([[0,1],[1,2],[2,1],[1,0]])
    print(move)
    if move != None:
        return move
    

def isBoardFull(board):
    # Esta función verifica si el tablero está lleno.

    # Argumentos:
    # board: Lista de strings que almacena el estado del tablero.

    # Esta función debe retorna el valor lógico True, si el tablero está lleno.
    # En caso contrario debe retornar el valor lógico False.

    # Desarrolle el cuerpo de la función aquí...
    flag = True
    for i in board:
        if " " in i:
            flag = False
            break

    return flag
