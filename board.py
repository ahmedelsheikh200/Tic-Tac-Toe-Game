from player import *
class Board :
    Empty_Cell = 0
    def __init__ (self):
        self.game_board  = [[0,0,0],
                            [0,0,0],
                            [0,0,0]]
    
    def print_board(self):
        print ("\nPositions :")
        self.print_board_with_positions()
        print ("\n Board:")
        for row in self.game_board:
            print("|", end="")
            for column in row:
                # If the column is empty, print a blank space.
                if column == Board.Empty_Cell:
                    print("   |", end="")
                # If the column is not empty, print the value.
                else:
                    print(f" {column} |", end="")
            print()
        print()

    def submit_moves(self,player,move):
        row = move.get_row()
        col = move.get_column()
        value = self.game_board[row][col]

        if value == Board.Empty_Cell :
            self.game_board[row][col] = player.marker
        else:
            print("This position is taken , Take Care 😁")
        
        


    def print_board_with_positions(self):
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")

    def check_if_game_over(self,player,last_move):
        return (self.check_row(player,last_move) or 
                self.check_col(player,last_move) or
                self.check_diagonal(player)or
                self.check_antidiagonal(player) 
                or self.check_tie())
    
    def check_row(self ,player,last_move):
        row_index =last_move.get_row()
        board_row = self.game_board[row_index]
        return board_row.count(player.marker)==3
    

    def check_col(self ,player,last_move):
        markers_count = 0
        col_index =last_move.get_column()
        for i in range (3):
            if self.game_board[i][col_index] == player.marker:
                markers_count += 1
        return markers_count == 3
    
    def check_diagonal(self , player) :
        markers_count = 0
        for i in range (3):
            if self.game_board[i][i] == player.marker:
                markers_count += 1
        return markers_count == 3   
    
    def check_antidiagonal(self , player) :
        markers_count = 0
        for i in range (3):
            if self.game_board[i][2-i] == player.marker:
                markers_count += 1
        return markers_count == 3   
    
    def check_tie(self):
        empyt_counter = 0 
        for row in self.game_board :
            empyt_counter += row.count(Board.Empty_Cell)


        return empyt_counter == 0
    
    def reset_game (self):
        self.game_board  = [[0,0,0],
                            [0,0,0],
                            [0,0,0]]





# board = Board()
# player = Player()
# board.print_board()
# move = player.get_move()
# board.submit_moves(player , move)
# board.print_board()
