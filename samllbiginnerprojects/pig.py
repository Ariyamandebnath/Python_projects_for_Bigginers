import random

def roll():
    min_value =1
    max_value = 6
    roll = random.randint(min_value,max_value)
    
    return roll
while True:
    players =input("enter the number og players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
            break
        else:
            print("players must be within 2 to 4 players")
        
    else:
        print("Invalid , try again")
        

max_score =50

player_scores =[0 for _ in range(players)]

while max(player_scores)< max_score:
    should_roll = input("would you like to roll (y)?")
    if should_roll.lower()!="y":
        break
    
    value= roll()
    if value ==0:
        print("You rolled a 1! Turn done!")
        
    else:
        current_score += value
        print("you rolled a:", value)
        
    print("your socre is:", current_score)

            
    