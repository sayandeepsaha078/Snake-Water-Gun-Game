import random

print("                                                  ****** SNAKE, WATER AND GUN *******                  ")
print(" ")
a=0
b=0
while(True):
    
    print("Player 1- choose an object : snake , water or gun? ")
    rand = random.randint(1,3)
    if rand == 1:
        computer ="snake"
    elif rand == 2:
        computer = "water"
    elif rand == 3:
        computer = "gun"
    print("Player 2- choose an object : snake , water or gun?")
    m=input()
    player =m.lower()
    if player =="snake" or player =="water" or player =="gun":
        if computer == player:
            print("Tie match") 
            a+=1
            b+=1
        elif computer =="snake":
                if player =="water":
                    print("Player 1 won the match")
                    a+=1
                elif player =="gun":
                    print("Player 2 won the match")
                    b+=1
        elif computer =="water":
                if player =="gun":
                    print("Player 1 won the match")
                    a+=1
                elif player =="snake":
                    print("Player 2 won the match")
                    b+=1
        elif computer =="gun":
                if player =="snake":
                    print("Player 1 won the match")
                    a+=1
                elif player =="water":
                    print("Player 2 won the match")
                    b+=1
    elif player == "stop":
        break
    else:  
        print("Option not found , please try again")    
        
    print(f"Player 1 choose {computer}")
    print(f"Player 2 choose {player}")
print(f"Score of player 1 :{a}")
print(f"Score of player 2 :{b}")
if a>b:
    print("Congratulations! Player 1 won the game")
elif b>a:
    print("Congratulations! Player 2 won the game")
else:
    print("Congratulations!  Both player 1 and player 2 won the game")
print(" ")
print("                                                        ***** GAME OVER ******                 ")