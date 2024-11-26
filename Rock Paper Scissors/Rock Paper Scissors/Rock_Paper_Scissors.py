
def haveTurn(Player):
    print("Player" + Player)
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    playerChoice = input("Select your choice: ")
    return playerChoice

def CheckResults(choiceOne,choiceTwo):
    if(choiceOne == choiceTwo):
        print("Draw!")
        return 0

inGame = True
while(inGame):
    One = haveTurn("1")
    Two = haveTurn("2")
    CheckResults(One, Two)
    NewGame = input("Play again? (Y/N) ")
    if(NewGame == "N"):
        inGame = False
        


