import random

win_score = 50
players_total_score = []

no_of_player = int(input('Enter no. of player will play (limit: 1 to 4) : '))
for i in range(no_of_player):
    players_total_score.append(0)

while max(players_total_score) < win_score:
    for i in range(no_of_player):
        print(f'\nPlayer {i+1} has just started!')
        current_score = 0
        while True:
            user_input = input('Do you want to [R]OLL or [H]OLD : ')
            if user_input in 'Rr':
                dice_value = random.randint(1,6)
                if dice_value != 1:
                    current_score = dice_value + current_score
                    print(f'Dice Value: {dice_value} and Current Score: {current_score}')
                else:
                    current_score = 0
                    print(f'Dice Value: {dice_value} and Current Score: {current_score}')
                    print(f'Total Score: {players_total_score[i]}')
                    break
            elif user_input in 'Hh':
                if players_total_score[i] < win_score:
                    players_total_score[i] = players_total_score[i] + current_score
                    print(f'Total Score: {players_total_score[i]}')
                    break
            else:
                print('Invaild input try again')

print(f'Player {i + 1} has WON with Total Score of {players_total_score[i]}')
    