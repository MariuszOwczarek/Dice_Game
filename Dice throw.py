import random
import matplotlib.pyplot as plt
from enum import Enum


class Lists(Enum):
    player_result = ' Player Wins !'
    player = 'Player'
    computer_result = ' Computer Wins !'
    computer = 'Computer'
    draw_result = ' There is a DRAW !'
    draw = 'Draw'


def play_game():
    # Variables
    player_wins = 0
    computer_wins = 0
    draw = 0
    rounds = int(input('How many rounds do you want to play? '))

    line1 = f'----------------------------------------\n' \
            f'  Round   | Player  | Computer | Points \n' \
            f'----------------------------------------\n'
    with open("dice_game.txt", 'w') as file1:
        file1.write(line1)

    for i in range(1, rounds+1):
        player_throw = random.randint(1, 6)
        computer_throw = random.randint(1, 6)

        # add points to points_variables based on ones throws
        if player_throw > computer_throw:
            player_wins += 1
        elif computer_throw > player_throw:
            computer_wins += 1
        else:
            draw += 1

        # save each round data to separate line in file
        lines = f'    {i}     |    {player_throw}    |    {computer_throw}     |    {player_wins}/{computer_wins}\n'
        with open("dice_game.txt", 'a') as file2:
            file2.write(lines)

    line5 = f'----------------------------------------\n' \
            f' Result:  |    {player_wins}    |    {computer_wins}     |\n' \
            f' Draws:   |    {draw}\n'
    with open("dice_game.txt", 'a') as file3:
        file3.write(line5)

    # graph title logic
    if player_wins - computer_wins > 0:
        winner = Lists.player_result.value
    elif computer_wins - player_wins > 0:
        winner = Lists.computer_result.value
    else:
        winner = Lists.draw_result.value

    with open("dice_game.txt", 'a') as file4:
        file4.write(winner)

    # draw a graph
    fig, ax = plt.subplots(figsize=(6, 6))
    results = [player_wins, computer_wins, draw]
    ax.pie(x=results, labels=[Lists.player.value, Lists.computer.value, Lists.draw.value],
           autopct=lambda p: f'{p*sum(results)/100 :.0f}points\n({p:.2f}%)',
           wedgeprops={'linewidth': 2.5, 'edgecolor': 'white'},
           textprops={'size': 'x-large'})
    ax.set_title(winner, fontsize=18)
    fig.savefig("dice_game.jpg")
    plt.show()


play_game()
