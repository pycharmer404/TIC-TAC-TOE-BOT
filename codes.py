from random import randint


def initialize():
    global grid, bot, player, won, moves
    print("'O' gets the first turn")
    grid = [["   " for col in range(3)]for row in range (3)]
    won = False
    moves = 1

def print_grid():
    global grid, bot, player, won, moves
    print("TIC TAC TOE (X||O)")
    print("   +---+---+---+")
    for row in range(3):
        line = "   |"
        for col in range(3):
            line = line + grid[row][col] + "|"
        print (line)
        print("   +---+---+---+")

def game():
 global grid, bot, player, won, moves
 if moves < 10:
   while True:
     p = input("Enter your choice(O/X): ")
     if p == "O":
        print()
        print("You are 'O'")
        print("'X' is bot")
        player = " O "
        bot = " X "
        player_turn()
        break
     elif p == "X":
        print()
        print("You are 'X'")
        print("'O' is bot")
        player = " X "
        bot = " O "
        bots()
        break
     else:
        print("Invalid :: Enter 'O' or 'X'")
 else:
     print("GAME ENDED")

def player_turn():   
        global grid, bot, player, won, moves
        while True:
            ur = int(input("Enter row: ")) - 1
            uc = int(input("Enter col: ")) - 1
            if (0<=ur<=2) and (0<=uc<=2) and grid[ur][uc] == "   ":
                moves += 1
                grid[ur][uc] = player
                break
            else:
                print("Invalid")
        update()
        check()
        if check() == True:
            print("You won")
            moves=15
            game()
        else:
            bots()

def bots():
        global grid, bot, player, won, moves
        while True:
            ur = randint(0, 2)
            uc = randint(0, 2)
            if grid[ur][uc] == "   ":
                moves += 1
                grid[ur][uc]=bot
                break
        update()
        check()
        if check() == True:
            print("Bot won")
            moves=15
            game()
        else:
            player_turn()

def update():
        global grid, bot, player, won, moves
        print("TIC TAC TOE (X||O)")
        print("   +---+---+---+")
        for row in range(3):
          line = "   |"
          for col in range(3):
              line = line + grid[row][col] + "|"
          print (line)
          print("   +---+---+---+")
        check()

def check():
      global grid, bot, player, won, moves
      if grid[0][0] == grid[1][1] == grid[2][2] != "   "\
         or grid[0][2] == grid[1][1] == grid[2][0] != "   ":
          won = True
          return(won)
      for i in range(3):
          if grid[i][0] == grid[i][1] == grid[i][2] != "   "\
           or grid[0][i] == grid[1][i] == grid[2][i] != "   ":
            won = True
            return (won)



initialize()
print_grid()
game()
