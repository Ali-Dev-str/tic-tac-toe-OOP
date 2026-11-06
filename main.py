import os 

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (characters only): ")
            if name.isalpha():
                self.name = name
                break
            else:
                print("Please choose a name with characters only. Thanks (:")

    def choose_symbol(self):
        while True:
            symbol = input("Enter your symbol (exactly 1 character): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol
                break
            else:
                print("Please enter a valid single character symbol.")

class Menu:
    def display_main_menu(self):
        print("Welcome to Tic Tac Toe Game (X & O)")
        print("1- Start Game")
        print("2- Quit Game")
        while True:
            choise = input("Enter your choice (1 Or 2): ")
            if choise in ["1", "2"]:
                return choise
            else:
                print("Invalid choice! Please choose 1 or 2.")

    def display_endgame_menu(self):
        main_endgame = """
    Game Over!
    1. Restart Game
    2. Quit Game
    Please enter Choice 1 or 2: """
        while True:
            choise = input(main_endgame)
            if choise in ["1", "2"]:
                return choise
            else:
                print("Please choose a valid number (1 or 2).")

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        print("\n")
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("-" * 9)
        print("\n")

    def update_board(self, choise, symbol):
        if self.is_valid_move(choise):
            self.board[choise-1] = symbol
            return True
        return False

    def is_valid_move(self, choise):
        return self.board[choise-1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

class Game:
    def __init__(self):
        self.Players = [Player(), Player()]
        self.Board = Board()
        self.Menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choise = self.Menu.display_main_menu()
        if choise == "1":
            self.setup_player()
            self.play_game()
        else:
            self.Quit_game()

    def setup_player(self):
        for number, player in enumerate(self.Players, start=1):
            print(f"\n--- Player {number} Details ---")
            player.choose_name()
            player.choose_symbol()
            clear_screen()

    def play_game(self):
        while True:
            self.play_turn()
            clear_screen()
            
            if self.check_win():
                self.Board.display_board()
                winner = self.Players[1 - self.current_player_index]
                print(f" Congratulations! {winner.name} ({winner.symbol}) Wins!")
                if self.handle_end_game(): break
                else: continue

            if self.check_draw():
                self.Board.display_board()
                print(" It's a Draw!")
                if self.handle_end_game(): break
                else: continue

    def play_turn(self):
        player = self.Players[self.current_player_index]
        self.Board.display_board()
        print(f" {player.name}'s turn ({player.symbol})")
        
        while True:
            try:
                cell_choice = int(input("Choose a cell (1 - 9): "))
                if 1 <= cell_choice <= 9:
                    if self.Board.update_board(cell_choice, player.symbol):
                        break 
                    else:
                        print("Cell already taken! Try another one.")
                else:
                    print(" Number out of range! Enter 1 to 9.")
            except ValueError:
                print(" Please enter a valid number from 1 to 9.")
                
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index 

    def check_win(self):
        win_combinations = [, [3,4,5], [6,7,8],  ]
        for compo in win_combinations:
            if self.Board.board[compo[0]] == self.Board.board[compo[1]] == self.Board.board[compo[2]]:
                return True 
        return False 

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.Board.board)

    def handle_end_game(self):
        choice = self.Menu.display_endgame_menu()
        if choice == "1":
            self.restart_game()
            return False  
        else:
            self.Quit_game()
            return True  

    def restart_game(self):
        self.Board.reset_board()
        self.current_player_index = 0
        clear_screen()

    def Quit_game(self):
        print("\nThank you for playing! Goodbye! ") 

if __name__ == "__main__":
    game = Game()
    game.start_game()