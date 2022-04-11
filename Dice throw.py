import random
import matplotlib.pyplot as plt

# Variables
player_wins = 0
comp_wins = 0
draw = 0
who_won = ["Player Wins !", "Computer Wins !", "There is a DRAW !"]
rounds = int(input('How many rounds ? '))


def play_game():
    global comp_wins, draw, player_wins, who_won, rounds

    for i in range(1, rounds+1):
        player_throw = random.randint(1, 6)
        comp_throw = random.randint(1, 6)

        # add points to points_variables based on ones throws
        if player_throw > comp_throw:
            player_wins += 1
        elif comp_throw > player_throw:
            comp_wins += 1
        else:
            draw += 1

        # save each round data to separate line in file
        lines = f'    {i}     |    {player_throw}    |    {comp_throw}     |    {player_wins}/{comp_wins}\n'
        with open("dice_game.csv", 'a') as file2:
            file2.write(lines)


def save_data_to_file():
    line1 = f'----------------------------------------\n' \
            f'  Round   | Player  | Computer | Points \n' \
            f'----------------------------------------\n'

    with open("dice_game.csv", 'w') as file1:
        file1.write(line1)

    play_game()

    line5 = f'----------------------------------------\n' \
            f' Result:  |    {player_wins}    |    {comp_wins}     |\n' \
            f' Draws:   |    {draw}\n'

    line6 = " " + winner_title()

    with open("dice_game.csv", 'a') as file3:
        file3.write(line5)
        file3.write(line6)


def winner_title():
    # graph title logic
    if player_wins - comp_wins > 0:
        title = who_won[0]
    elif comp_wins - player_wins > 0:
        title = who_won[1]
    else:
        title = who_won[2]
    return title


def graph():
    # draw a graph
    fig, ax = plt.subplots(figsize=(6, 6))
    results = [player_wins, comp_wins, draw]
    ax.pie(x=results, labels=['Player', 'Computer', 'Draw'],
           autopct=lambda p: f'{p*sum(results)/100 :.0f}points\n({p:.2f}%)',
           wedgeprops={'linewidth': 2.5, 'edgecolor': 'white'},
           textprops={'size': 'x-large'})
    ax.set_title(winner_title(), fontsize=18)
    fig.savefig("dice_game.jpg")
    plt.show()


# Main Program
save_data_to_file()
graph()
