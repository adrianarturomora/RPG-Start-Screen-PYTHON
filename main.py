def displayPlayers(playerList):
    for player in playerList:
            print(player["name"] + " " + player["class"] + " " + player["sex"] + " " + player["gold"])

def addPlayer(playerList, name, user_Class, sex, gold):
        player = {"name" : name, "class" : user_Class, "sex" : sex, "gold" : gold}
        playerList.append(player)
        return playerList

def removePlayer(playerList, playerName):
        index = 0
        removeIndex = -1
        while index < len(playerList):
                if playerList[index]["name"] == playerName:
                        removeIndex = index
                        index = len(playerList)
                index += 1
        if removeIndex >= 0:
                del (playerList[removeIndex])
        return playerList

def savePlayers(playerList):
        playerFile = open("rpg.txt", "w")
        for player in playerList:
                print(player["name"], player["class"], player["sex"], player["gold"], sep = ",", file = playerFile)
        playerFile.close()

def menu():
        print("Show - Display all players")
        print("Add - Add a player")
        print("Delete - Delete a player")
        print("Exit - Exit program")

def run():
    runProgram = True
    playerList = []
    menu()
    print("\nList is empty by default, to load students select option 6")
    while runProgram:
        invalidOption = False
        option = input("\nSelect a menu option: ")
        if option == "Show" or option == "Add" or option == "Delete" or option == "Exit" or option == "Save" or option == "Menu":
            if option == "Exit":
                runProgram = False
                print("Goodbye.")
            elif option == "Show":
                displayPlayers(playerList)
            elif option == "Add":
                print("Create a Mage, Warrior, Bowman, or Thief")
                name = input("Name: ")
                inputClass = True
                while inputClass:
                        user_Class = input("Class: ")
                        if user_Class == "Mage" or user_Class == "Warrior" or user_Class == "Bowman" or user_Class == "Thief":
                            inputClass = False
                        else:
                            inputClass = True
                        if inputClass:
                            print("Invald Class, Try again")
                sex = input("Sex: ")
                gold = input("Gold: ")
                addPlayer(playerList, name, user_Class, sex, gold)
                savePlayers(playerList)
            elif option == "Delete":
                playerName = input("Enter the name of the player to remove: ")
                removePlayer(playerList, playerName)
                savePlayers(playerList)
            elif option == "Menu":
                menu()
            else:
                invalidOption = True
        else:
            invalidOption = True
        if invalidOption:
            print("Invalid Option.")
run()



