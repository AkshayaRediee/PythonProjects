import random

def roll():
    min_val = 2
    max_val = 5
    roll = random.randint(min_val, max_val)

    return roll


while  True:
      players = input("Enter the no.of players(2-5): ")
      if players.isdigit():
         players = int(players)
         if 2<= players <= 5:
             break
         else:
             print("Enter a valid no.of players")
      else:
         print("Invalid, Try again")

print(players)
players_score = [0 for _ in range(players)]   
print(players_score)
max_score = 50
while max(players_score) < max_score:
    for player_index in range(players):
        print("\nPlayer number", player_index + 1, "turn has just begun!")
        print("Your total score is:", players_score[player_index], "\n")
        current_score = 0

        while True:
               should_roll = input("Would you like to roll (y)?") 
               if should_roll.lower() != "y":
                  break
               value = roll()
               if value == 1:
                  print("You rolled a 1! Turn done!")
                  current_score = 0
                  break
               else:
                  current_score += value
                  print("You rolled a :" , value)

               print("Your score is:", current_score)

        players_score[player_index] += current_score
        
        print("Your total score is: ", players_score[player_index])
        
max_score = max(players_score)
winning_index = players_score.index(max_score)

print("Player number", winning_index +1, "is the winner with the score of:", max_score)      


