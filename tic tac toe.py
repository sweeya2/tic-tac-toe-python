win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#these are the combinations in which the player or the computer can win

def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
    end = False  #this is true when this round ends, either of them wins or draw
    one = ''  #stores who is first (player/computer)
    two = ''  #stores who is second (player/computer)
    onee = ''  #stores the X/O variable player one has
    twoo = ''   #stores the X/O variable player two has
    univ = ''   #stores the value of the X/O which player chooses
    notuniv = ''   #stores the value of the X/O which computer gets
    
    def choice():

      # Lets the player type if they want to go first.
      # Returns either Y/N 
      
      letter = ''

      while not (letter == 'Y' or letter == 'N'):   #runs as long neither letter is Y or N
          
          print('Do you want to play first?\nChoose Y if you want to play first or N otherwise.')

          letter = input().upper()  #changes input to uppercase
          try:
                if letter == "Y" or letter == "N":
                    return letter
                else:
                    print("\nInput either Y or N\n")    #when you input a wrong letter
                    continue
          except ValueError:
               print("\nThat's not a letter. Try again\n")   #when you don't input a letter
               continue

    def inputPlayerLetter():

      # Lets the player type which letter they want to be.
      # Returns either X/O

      letter = ''

      while not (letter == 'X' or letter == 'O'):    #runs as long neither letter is X or O

          print('Do you want to choose X or O?')

          letter = input().upper()    #changes input to uppercase
          try:
                if letter == "X" or letter == "O":
                    return letter
                else:
                    print("\nInput either X or O\n")  #when you input a wrong letter
                    continue
          except ValueError:
               print("\nThat's not a letter. Try again\n")   #when you don't input a letter
               continue

    def replay():

      # Lets the player choose if they want to play the game again, once the current round is done

      # Returns either Y/N

      letter = ''

      while not (letter == 'Y' or letter == 'N'):   #runs as long neither letter is Y or N

          print('Do you wish to replay?\nType Y/N')

          letter = input().upper()   #changes input to uppercase
          try:
                if letter == "Y" or letter == "N":
                    return letter
                else:
                    print("\nInput either Y or N\n")   #when you input a wrong letter
                    continue
          except ValueError:
               print("\nThat's not a letter. Try again\n")    #when you don't input a letter
               continue


    #prints the board
    def draw():
        print("\n")
        print("\t     |     |")
        print("\t ",board[0]," | ",board[1]," | ",board[2]," ")
        print('\t_____|_____|_____')
     
        print("\t     |     |")
        print("\t ",board[3]," | ",board[4]," | ",board[5]," ")
        print('\t_____|_____|_____')
     
        print("\t     |     |")
        print("\t ",board[6]," | ",board[7]," | ",board[8]," ")
        print("\t     |     |")
        print("\n")
        print()


    #in p1, the player makes the move
    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":   #if that cell is already filled
            print("\nYou can't go there. Try again")
            p1()
        else:     #set the board to that particular value (X/O)
            if one == "Player":
                board[n] = onee    
            else:
                board[n] = twoo
             
           

    #in p2, the computer makes the move
    def p2():
        p = ''   #stores X/O of the computer
        q = ''   #stores X/O of the player
        if one == "Computer":    
            p = onee
            q = twoo
        else:
            p = twoo
            q = onee

        for a in win_commbinations:     #this for loop checks if there is a possibility for the computer to win
            if board[a[0]] == board[a[1]]== p and board[a[2]] != q:
                board[a[2]] = p
                return
            if board[a[1]] == board[a[2]]== p and board[a[0]] != q:
                board[a[0]] = p
                return
            if board[a[0]] == board[a[2]]== p and board[a[1]] != q:
                board[a[1]] = p
                return

        for a in win_commbinations:     #this for loop checks if there is a possibility to block any place incase the player has a chance to win
            if board[a[0]] == board[a[1]]== q and board[a[2]] != p:
                board[a[2]] = p
                return
            if board[a[1]] == board[a[2]]== q and board[a[0]] != p:
                board[a[0]] = p
                return
            if board[a[0]] == board[a[2]]== q and board[a[1]] != p:
                board[a[1]] = p
                return

        #from here it checks if any of the corners are empty
        if board[0] == 1:   
            board[0] = p
            return;
        if board[2] == 3:
            board[2] = p
            return;
        if board[6] == 7:
            board[6] = p
            return;
        if board[8] == 9:
            board[8] = p
            return;

        #from here it checks if the center is empty
        if board[4] == 5:
            board[4] = p
            return;
        
        #if none of the above hold true
        if board[1] == 2:
            board[1] = p
            return;
        if board[3] == 4:
            board[3] = p
            return;
        if board[5] == 6:
            board[5] = p
            return;
        if board[7] == 8:
            board[7] = p
            return;


    # the player chosed a number in this function
    def choose_number():
        while True:
            a = input()
            try:
                a  = int(a)
                a -= 1
                if a in range(0, 9):   
                    return a
                else:
                    print("\nThat's not on the board. Choose again")   #if a can't be used to fill the board
                    continue
            except ValueError:   #if a is not an integer
               print("\nThat's not a number. Choose again")
               continue


    #checks if there is a possibility of winning or a tie
    def check_board():
        count = 0
        for a in win_commbinations:    
            if board[a[0]] == board[a[1]] == board[a[2]] == univ:   #if univ, then player wins
                print("Player Wins!\nCongratulations!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == notuniv:   #if notuniv, then computer wins
                print("Computer Wins!\nCongratulations!\n")
                return True
        for a in range(9):  #if all 9 numbers in the board are filled, and no one wins, then tie
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True

    #sets the value of one, two, onee, twoo, univ, notuniv
    univ = inputPlayerLetter()   
     
    if univ == "X":  
        notuniv = "O"
    else:
        notuniv = "X"
     
    if choice() == "Y":
        one = "Player"
        two = "Computer"
        onee = univ
        if univ == "X":
            twoo = "O"
        else:
            twoo = "X"
        
    else:
        two = "Player"
        one = "Computer"
        twoo = univ
        if univ == "X":
            onee = "O"
        else:
            onee = "X"

    
        
    while not end:
        draw()  
        end = check_board()
        if end == True:  #if end is true, either someone won, or it's a tie
            break
        print(one,"choose where to place a",onee)
        if one == "Player":  #if the first one is player
            p1()
        else:               #if the first one is computer
            p2()
        
        print()
        draw()
        end = check_board()
        if end == True:   #if end is true, either someone won, or it's a tie
            break
        print(two,"choose where to place a",twoo)
        if two == "Player":   #if the second one is player
            p1()
        else:                 #if the second one is computer
            p2() 
        print()
  
    
    if replay() == "Y":  #if the player wants to start another round
        print()
        tic_tac_toe() #calling the tic_tac_toe() function again

tic_tac_toe()
