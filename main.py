from board import *


player = Player()
computer = Player(False)
board = Board()

def main():
    print("*********************************")
    print("\n Welcome to Tic Tac Toe Game")
    print("\n*********************************")

    while True:
        board.reset_game()  # Reset the board at the start of each game
        play()
        want_to_continue = input('Do you want to play again? (Y for yes, N for no) ').strip().lower()
        if want_to_continue == "n":
            print("See you soon 😊")
            break
        else:
            print("Good luck! 🌺")

def play():
    while True:
        # Player's Turn
        last_move = player.get_move()
        board.submit_moves(player, last_move)
        board.print_board()
        if board.check_if_game_over(player, last_move):
            if board.check_tie():
                print('DRAW 🤝🤝')
            else:
                print("YOU WIN 🎉🎉")
            return  # Exit game loop after win/draw

        # Computer's Turn
        print('\nComputer Turn:')
        last_move = computer.get_move()
        board.submit_moves(computer, last_move)
        board.print_board()
        if board.check_if_game_over(computer, last_move):
            if board.check_tie():
                print('DRAW 🤝🤝')
            else:
                print("Computer Wins 😜😜")
            return  # Exit game loop after win/draw

if __name__ == "__main__":
    main()
