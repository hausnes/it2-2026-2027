import os 

board = [
    [-1,-1,-1],
    [-1,-1,-1],
    [-1,-1,-1]
    ]

#Vi kommer til å gange med -1 for å bytte mellom spillerne
player = 1
usedCoordinatesUpdating = []

def clearScreen(): 
    #Kilde: https://www.geeksforgeeks.org/clear-screen-python/ (Jeg har bare gjort dette for Windows brukere)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def printBoard():
    for i in board:
        print("|", end="")

        for j in i:
            if j == 10:
                print("X", end="|")
            elif j == 0:
                print("0", end="|")
            else:
                print(" ", end="|")

        print("\n")

def turn(player, usedCoordinates):
    #Denne løkken sjekker om det er gyldige koordinater
    while True:         
        try:
            #Sjekker om de er kun tall og mapper dem 
            coordinates = list(map(int, input("Hvor vil du plassere brikken din? Oppgi 2 tall som x og y koordinat (for eksempel: 2 2) ").split()))

            #Sjekker om det kun er 2 tall
            if len(coordinates) == 2:
                #Sjekker om tallene er innenfor grensene
                if 1 <= coordinates[0] <= 3 and 1 <= coordinates[1] <= 3:
                    if coordinates in usedCoordinates:
                        print("Koordinatene er brukt")
                    else:
                        #Siden de er gyldige koordinater kan vi gå til neste steg av turen: logikken
                        usedCoordinates.append(coordinates[:])
                        break
                else:
                    print("Tallene må være innenfor brettet")
            else:
                print("Du må kun ha 2 tall")

        #Hvis det ikke er tall får brukeren beskjed at de må kun få tall
        except:
            print("Du må kun oppgi tall")

    coordinates.reverse()

    #Bytter fra 1 index til 0 index
    coordinates[0] -= 1
    coordinates[1] -= 1

    #Hvis det er spiller 1
    if player == 1: 
        board[coordinates[0]][coordinates[1]] = 10 #X
    else:
        board[coordinates[0]][coordinates[1]] = 0 #0
    
    return usedCoordinates, coordinates

def gameLogic(coordinates, usedCoordinates):
    """
    Her sjekker vi om noen har vunnet spillet. Siden jeg har gitt alle verdiene et tall
    0 er 0, X er 10 og ikke fullført = -1 kan jeg bare summere sammen radene/kolonene/diagonalene. 
    Hvis sum = 30 er X vinner, 0 er 0 vinner og noe annet er det ingen vinner. 
    
    Det som er ganske greit er at vi kommer maks til å endre 3 forskjellige rader, så vi må ikke se
    på alle. Da kan man gjøre litt grei logikk for å sjekke rundt de områdene som har blitt endret
    """

    #Først sjekker vi om vi må sjekke en diagonal
    diagonal = False

    if coordinates[0] == 0:
        if coordinates[1] == 0 or coordinates[1] == 2: 
            diagonal = True
    elif coordinates[0] == 2:
        if coordinates[1] == 0 or coordinates[1] == 2: 
            diagonal = True

    if sum(board[coordinates[0]]) == 30:
        print("Congratulations! Player 1 wins!")
        return True
    elif sum(board[coordinates[0]]) == 0:
        print("Congratulations! Player 1 wins!")
        return True
    elif (board[0][coordinates[1]] + board[1][coordinates[1]] + board[2][coordinates[1]]) == 30:
        print("Congratulations! Player 1 wins!")
        return True
    elif (board[0][coordinates[1]] + board[1][coordinates[1]], + board[2][coordinates[1]]) == 0:
        print("Congratulations! Player 2 wins!")
        return True

    if diagonal: 
        if (board[0][0] + board[1][1] + board[2][2]) == 30 or (board[0][2] + board[1][1] + board[2][0]) == 30: 
            print("Congratulations! Player 1 wins!")
            return True
        elif (board[0][0] + board[1][1] + board[2][2]) == 0 or (board[0][2] + board[1][1] + board[2][0]) == 0: 
            print("Congratulations! Player 2 wins!")
            return True
        
    if len(usedCoordinates) == 9: 
        #Det er kun 9 steder å spille  
        print("It was a draw!")
        return True
        
def noughtsAndCrosses(player=1, usedCoordinatesUpdating=[]):
    gameOver = False
    while not gameOver:
        usedCoordinatesUpdating, coordinates = turn(player, usedCoordinatesUpdating)
        player *= -1
        clearScreen()
        printBoard()
        gameOver = gameLogic(coordinates, usedCoordinatesUpdating)

if __name__ == "__main__":
    clearScreen()
    printBoard()
    noughtsAndCrosses()
    while True: 
        fortsett = input("Vil du fortsette? Y/N ").upper()
        if fortsett == "Y":
            print("Ny runde")
            
            board = [
                     [-1,-1,-1],
                     [-1,-1,-1],
                     [-1,-1,-1]
                    ]
            
            clearScreen()
            noughtsAndCrosses()
        elif fortsett == "N":
            break
