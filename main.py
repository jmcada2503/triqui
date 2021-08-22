import triqui as tr
import random

print()
tr.printIntro("intro.txt")
# 1. Mostrar mensaje de bienvenida
while True:

    turn = tr.whoGoesFirst()  # Indica quién tiene el turno para jugar, el usuario o la computadora.
    # 2. Crear el tablero
    board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    # 3. El usuario debe seleccionar la marca
    player = tr.inputPlayerLetter()
    # 4. Quién va primero el usuario o la computadora?

    print(turn + ' va primero.')

    jugando = True # El juego ha iniciado

    while jugando:
        if turn == 'Usuario': # 5. Turno del usuario

            # a. Mostrar tablero
            tr.drawBoard(board)
            # b. Pedir jugada al usuario
            move = tr.getPlayerMove(board)
            # c. Actualizar el tablero
            board = tr.makeMove(board, player[0], move)
            # d. Verificar si el usuario ha ganado el juego.
            #    Si si, mostrar tablero, mostrar mensaje de felicitación y terminar el juego.
            if tr.isWinner(board, player[0]):
                print(f"{turn} ha ganado el juego")
                break

            # e. Verificar si hay empate.
            elif tr.isBoardFull(board):
                print("Hubo un empate. El juego ha terminado")
                break
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.

            # f. Si el usuario no ha ganado y no hay empate, la computadora
            #    toma el siguiente turno

            turn = 'Computadora'

        else: # 6. Turno de la computadora.

            # a. Computadora hace jugada.
            move = tr.getComputerMove(board, player[1])
            # b. Actualizar el tablero.
            board = tr.makeMove(board, player[1], move)

            # c. Verificar si la computadora ha ganado el juego.
            if tr.isWinner(board, player[1]):
                tr.drawBoard(board)
                print(f"{turn} ha ganado el juego")
                break

            #    Si si, mostrar tablero, mostrar mensaje indicando al usuario que ha perdido y terminar el juego.
            
            # d. Verificar si hay empate.
            #    Si si, mostrar tablero, mostar mensaje de empate y terminar el juego.
            
            elif tr.isBoardFull(board):
                print("Hubo un empate. El juego ha terminado")
                break

            # f. Si la computadora no ha ganado y no hay empate, el usuario
            #    toma el siguiente turno.

            turn = 'Usuario'

    # 7. Preguntar si el usuario quiere jugar una vez mas
    #    Si no, finalizar el programa.
    continuar = input("Desea jugar nuevamente? (s/n) ")
    if continuar == "n":
        break
