from IPython.display import clear_output
import random

def display_board_init():
    print('1' + '|' + '2' + '|' + '3')
    print('-' * 5)
    print('4' + '|' + '5' + '|' + '6')
    print('-' * 5)
    print('7' + '|' + '8' + '|' + '9')


def display_board(game_data):
    clear_output()
    print("Updated game data")
    print(game_data['up-left'] + '|' + game_data['up-center'] + '|' + game_data['up-right'])
    print('-' * 5)
    print(game_data['mid-left'] + '|' + game_data['mid-center'] + '|' + game_data['mid-right'])
    print('-' * 5)
    print(game_data['low-left'] + '|' + game_data['low-center'] + '|' + game_data['low-right'])


def position_choice(game_data, player_data):
    position, choice = input_validator(game_data, player_data)

    # if not is_position_empty(game_data, position):
    #     update_choice(game_data)

    # position = int(position)
    return update_board(choice, game_data, position)

# This is the validator for the input
def input_validator(game_data, player_data):
    while True:
        position = input(f"{player_data.get('name')}, please enter a position between 1-9: ")
        # choice = ' '
        choice = player_data.get('choice')

        if position.isdigit() and int(position) in range(1, 10):
            position = int(position)

            if is_position_empty(game_data, position):
                # while choice.upper() not in ['X', 'O']:
                #     choice = input("Please enter your choice with 'X' or 'O': ")
                #     return position, choice
                return position, choice
            else:
                pass

# Return True/False based on the position
def is_position_empty(game_data, position):
    position = position_to_key(position)

    if game_data[position].upper() in ['X', 'O']:
        print("The position is already occupied, please chose another position")
        return False

    return True

#
def update_choice(game_data):
    position, choice = input_validator(game_data)
    position = position_to_key(position)

    game_data[position] = choice

    return game_data


def update_board(choice, game_data, position):
    position = position_to_key(position)
    game_data[position] = choice

    return game_data


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


def is_game_finished(game_data, players_data):
    isWin = False
    choice = ' '

    if game_data['up-left'] == game_data['up-center'] == game_data['up-right']\
            and game_data['mid-left'].upper() in ['X', 'O']:
        if game_data['up-left'] == 'X':
            choice = 'X'
        else:
            choice = 'O'

        isWin = True
    # elif game_data['mid-left'] == game_data['mid-center'] == game_data['mid-right'] \
    #         and game_data['mid-left'].upper() in ['X', 'O']:
    #     return winner_name_selection(game_data['up-left'], players_data)
    # elif game_data['low-left'] == game_data['low-center'] == game_data['low-right']\
    #         and game_data['low-left'].upper() in ['X', 'O']:
    #     return winner_name_selection(game_data['up-left'], players_data)
    # elif game_data['up-left'] == game_data['mid-center'] == game_data['low-right']\
    #         and game_data['up-left'].upper() in ['X', 'O']:
    #     return winner_name_selection(game_data['up-left'], players_data)
    # elif game_data['up-right'] == game_data['mid-center'] == game_data['low-left']\
    #         and game_data['up-right'].upper() in ['X', 'O']:
    #     return winner_name_selection(game_data['up-left'], players_data)
    # elif game_data['up-left'] == game_data['mid-left'] == game_data['low-left']\
    #         and game_data['up-left'].upper() in ['X', 'O']:
    #     return winner_name_selection(game_data['up-left'], players_data)
    # elif game_data['up-center'] == game_data['mid-center'] == game_data['low-center']\
    #         and game_data['up-center'].upper() in ['X', 'O']:
    #     return winner_name_selection(game_data['up-left'], players_data)
    # elif game_data['up-right'] == game_data['mid-right'] == game_data['low-right']\
    #         and game_data['up-right'].upper() in ['X', 'O']:
    #     return winner_name_selection(game_data['up-left'], players_data)

    if isWin:
        return winner_name_selection(choice, players_data)

    return False


def winner_name_selection(choice, players_data):
    for values in players_data.values():
        if values.get('choice').upper() == choice:
            print(f"{values.get('name')} won the match")
    return True


def update_player_details():
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

    print("Player 1, please enter your name: ")
    players_data['Player1']['name'] = input()
    print("Player 1, please enter your choice: ")
    players_data['Player1']['choice'] = input()

    print("Player 2, please enter your name: ")
    players_data['Player2']['name'] = input()

    if players_data['Player1']['choice'].upper() == 'X':
        players_data['Player2']['choice'] = 'O'
    else:
        players_data['Player2']['choice'] = 'X'

    return players_data


def game_start():
    game_on = True
    replay = True

    print("initial board data")
    display_board_init()
    game_data = {'up-left': ' ', 'up-center': ' ', 'up-right': ' ',
                 'mid-left': ' ', 'mid-center': ' ', 'mid-right': ' ',
                 'low-left': ' ', 'low-center': ' ', 'low-right': ' '}

    players_data = update_player_details()

    while replay:
        while game_on:
            # Display the board first time
            display_board(game_data)

            # Start asking the user for choice
            randint = random.randint(0, 1)
            if randint == 0:
                print("Player1 starts")
                game_data = position_choice(game_data, players_data['Player1'])
            else:
                print("Player2 starts")
                game_data = position_choice(game_data, players_data['Player2'])

            # Display the board again to user
            display_board(game_data)

            if is_game_finished(game_data, players_data):
                break

            # Check user wish to continue
            if not wish_to_continue():
                break

        # Check if user want to replay
        if wish_to_replay():
            display_board_init()
        else:
            break

game_start()
