print('\n' * 30 + ' ' * 60 + 'Welcome To Tic Tac Toe')
board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

game_going = True
winner = None
current_player = 'x'

def print_board():
    print('\n')
    print(board[0] + '  |  ' + board[1] + '  |  ' + board[2])
    print(board[3] + '  |  ' + board[4] + '  |  ' + board[5])
    print(board[6] + '  |  ' + board[7] + '  |  ' + board[8])
    print('\n')

def play_game():

    print_board()

    while game_going:
        handle_turn(current_player)
        check_for_winner()
        flip_player()
        check_for_tie()

        if winner == 'x' or winner == 'o':
            print('\n' + winner + ' is the winner!')
        else: pass

def handle_turn(current_player):
    print(current_player + " turn")
    position = input('Enter a position between 1 and 9: ')
    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print('Invalid input! Please try again')
        position = input('Enter a position between 1 and 9: ')
    if position.isdigit(): position = int(position) - 1
    if board[position] != "-": print('The slot is taken! Go again')
    board[position] = current_player
    print_board()


def check_for_winner():
    global winner

    row_winner = check_rows()
    col_winner = check_cols()
    diag_winner = check_daigs()

    if row_winner: winner = check_rows()
    if col_winner: winner = check_cols()
    if diag_winner: winner = check_daigs()

def check_for_tie():
    global game_going
    if "-" not in board:
        print('\nThe game is tied!\n')
        game_going = False
    return


def check_rows():
    global game_going
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3 is True:
        game_going = False
    if row1: return board[0]
    if row2: return board[3]
    if row3: return board[6]


def check_cols():
    global game_going
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3 is True:
        game_going = False
    if col1: return board[0]
    if col2: return board[1]
    if col3: return board[2]


def check_daigs():
    global game_going
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"

    if diag1 or diag2 is True:
        game_going = False
    if diag1: return board[0]
    if diag2: return board[2]


def flip_player():
    global current_player
    if current_player == 'x':
        current_player = 'o'
    elif current_player == 'o':
        current_player = 'x'
        return


play_game()