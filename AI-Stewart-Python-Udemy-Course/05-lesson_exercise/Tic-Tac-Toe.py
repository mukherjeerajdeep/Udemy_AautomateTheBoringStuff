from IPython.display import clear_output
import random

def display_board_init():
    print('1' + '|' + '2' + '|' + '3')
    print('-' * 5)
    print('4' + '|' + '5' + '|' + '6')
    print('-' * 5)
    print('7' + '|' + '8' + '|' + '9')


def display_board(game_data):
    print("Updated game data")
    clear_output()
    print(game_data['up-left'] + '|' + game_data['up-center'] + '|' + game_data['up-right'])
    print('-' * 5)
    print(game_data['mid-left'] + '|' + game_data['mid-center'] + '|' + game_data['mid-right'])
    print('-' * 5)
    print(game_data['low-left'] + '|' + game_data['low-center'] + '|' + game_data['low-right'])


def player_position_choice(game_data, player_data):
    position = validate_position(game_data, player_data)
    choice = player_data.get('choice')
    return update_board(game_data, choice, position)

# This is the validator for the input position
def validate_position(game_data, player_data):
    while True:
        position = input(f"{player_data.get('name')}, please enter a position between 1-9: ")

        if position.isdigit() and int(position) in range(1, 10):
            position = int(position)
            if is_an_empty_position(game_data, position):
                return position
            else:
                print("The position is already occupied, please chose another position")
                pass


def is_an_empty_position(game_data, position):
    position = position_to_key(position)
    if game_data[position] == ' ':
        return True

    return False

def update_board(game_data, choice, position):
    position = position_to_key(position)
    game_data[position] = choice

    return game_data


def is_board_full(game_data):
    for position in range(1, 10):
        if is_an_empty_position(game_data, position):
            return False

    return True

# Utility function to convert
def position_to_key(argument):
    switcher = {
        1: 'up-left',
        2: 'up-center',
        3: 'up-right',
        4: 'mid-left',
        5: 'mid-center',
        6: 'mid-right',
        7: 'low-left',
        8: 'low-center',
        9: 'low-right'
    }

    return switcher.get(argument, "wrong choice")


def wish_to_continue():
    while True:
        replay = input("Do you want to continue Y/N: ")

        if replay.upper() not in ['Y', 'N']:
            replay = input("Do you want to continue Y/N: ")

        return replay.upper() == 'Y'


def wish_to_replay():
    while True:
        replay = input("Do you want to replay Y/N: ")

        if replay.upper() not in ['Y', 'N']:
            replay = input("Do you want to replay Y/N: ")

        return replay.upper() == 'Y'


def is_game_won(game_data, choice):
    return game_data['up-left'] == game_data['up-center'] == game_data['up-right'] == choice or \
           game_data['mid-left'] == game_data['mid-center'] == game_data['mid-right'] == choice or \
           game_data['low-left'] == game_data['low-center'] == game_data['low-right'] == choice or \
           game_data['up-left'] == game_data['mid-center'] == game_data['low-right'] == choice or \
           game_data['up-right'] == game_data['mid-center'] == game_data['low-left'] == choice or \
           game_data['up-left'] == game_data['mid-left'] == game_data['low-left'] == choice or \
           game_data['up-center'] == game_data['mid-center'] == game_data['low-center'] == choice or \
           game_data['up-right'] == game_data['mid-right'] == game_data['low-right'] == choice


def init():
    players_data = {
                   'Player1': {
                                'name': '',
                                'choice': ''
                              },
                   'Player2': {
                                'name': '',
                                'choice': ''
                              }
                   }

    players_input(players_data)

    game_data = {'up-left': ' ', 'up-center': ' ', 'up-right': ' ',
                 'mid-left': ' ', 'mid-center': ' ', 'mid-right': ' ',
                 'low-left': ' ', 'low-center': ' ', 'low-right': ' '}

    return players_data, game_data


def players_input(players_data):
    print("Player 1, please enter your name: ")
    players_data['Player1']['name'] = input().upper()
    print("Player 1, please enter your choice between X/O: ")
    player_choice = input()

    player_choice = validate_choice(player_choice, players_data)
    players_data['Player1']['choice'] = player_choice.upper()

    print("Player 2, please enter your name: ")
    players_data['Player2']['name'] = input().upper()

    if player_choice.upper() == 'X':
        players_data['Player2']['choice'] = 'O'
    else:
        players_data['Player2']['choice'] = 'X'


def validate_choice(player_choice, players_data):
    while player_choice.upper() not in ['X', 'O']:
        print("Not a valid choice, please select between 'X' or 'O'")
        player_choice = input()

    return player_choice


def turn_flipper(players_data):
    flip = random.randint(0, 1)

    if flip == 0:
        print(f"{players_data['Player1']} starts")
        player = players_data['Player1'] # Player1
    else:
        print(f"{players_data['Player2']} starts")
        player = players_data['Player2'] # Player2

    return player


def game_start():
    game_on = True
    print("initial board data")
    display_board_init()

    while True:
        # Initialize the data for players and game

        players_data, game_data = init()
        # Flip the coin, and select the player
        current_player = turn_flipper(players_data)
        print(f"{current_player.get('name')} goes first")

        play_game = input('Ready to play? y or n?')

        if play_game.upper() == 'N':
            game_on = False

        while game_on:
            # Start asking the user for choice
            if current_player == players_data['Player1']:
                display_board(game_data) # show the board
                # chose a position
                game_data = player_position_choice(game_data, current_player)
                # display the board to user
                display_board(game_data)
                # check if they won
                if is_game_won(game_data, current_player.get('choice')):
                    print(f"{current_player.get('name')} won")
                    display_board(game_data)
                    break
                # or check if it is a tie
                else:
                    if is_board_full(game_data):
                        print("It's a tie")
                        display_board(game_data)
                        break
                    else:
                        current_player = players_data['Player2']
                # if no ties or wins then next players turn
            else:
                current_player = players_data['Player2']
                display_board(game_data)  # show the board
                # chose a position
                game_data = player_position_choice(game_data, current_player)
                # display the board to user
                display_board(game_data)
                # check if they won
                if is_game_won(game_data, current_player.get('choice')):
                    print(f"{current_player.get('name')} won")
                    display_board(game_data)
                    break
                # or check if it is a tie
                else:
                    if is_board_full(game_data):
                        print("It's a tie")
                        display_board(game_data)
                        break
                    else:
                        current_player = players_data['Player1']

        # Check if user want to replay
        if wish_to_replay():
            display_board_init()
        else:
            break


game_start()
