

print("\n==========================Rock Paper Scissors Game==========================\n")
print('\nRock = 1, Paper = 2, Scissors = 3 Quit = 0')
print("\nPlease enter the correct value, follow the insutructions above")

p1 = int(input("Player 1, select your move. Enter 0 to end:"))
p2 = int(input("Player 2 select your move. Enter 0 to end:"))

while p1 and p2 != 0:
    if p1 == 1 and p2 == 2:
        print("Player 2 Wins")
    elif p1 == 1 and p2 == 1:
        print("Draw")
    elif p1 == 1 and p2 == 3:
        print("player 1 Wins")
    elif p1 == 2 and p2 == 1:
        print("Player 1 wins!")
    elif p1 == 3 and p2 == 1:
        print("Player 2 wins")
    elif p1 == 3 and p2 == 3:
        print("Draw")
    elif p1 == 2 and p2 == 2:
        print("Draw")
    elif p1 == 2 and p2 == 3:
        print("Player 2 wins")
    else:
        print("INVALID ENTRY")

    p1 = int(input("Player 1, select your move. Enter 0 to end:"))
    p2 = int(input("Player 2 select your move. Enter 0 to end:"))
