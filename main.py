board = list(range(1, 10))

def make_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-" * 13)


def take_item(player_item):
        p_answer = int(input("Выберите клетку для " + player_item + "?"))
        if p_answer >= 1 and p_answer <= 9:
            if (str(board[p_answer-1]) not in "XO"):
                board[p_answer-1] = player_item
            else:
                print("Эта клетка занята")
        else:
            print("Попробуйте ещё раз.")


def check(board):
    win_board = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for a in win_board:
        if board[a[0]] == board[a[1]] == board[a[2]]:
            return board[a[0]]
    return False


def main_def(board):
    counter = 0
    c = False
    while not c:
        make_board(board)
        if counter % 2 == 0:
            take_item("X")
        else:
            take_item("O")
        counter += 1
        if counter > 4:
            t = check(board)
            if t:
                print(t, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    make_board(board)


main_def(board)