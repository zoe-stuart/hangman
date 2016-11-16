#Hangman
#Zoe Stuart
#Oct. 19, 2016





import os
import random

def show_start_screen():
    print("██╗     ███████╗████████╗ █ ███████╗    ██████╗ ██╗       ███═╗ ██╗   ██╗")
    print("██║     ██╔════╝╚══██╔══╝   ██╔════╝    ██╔══██╗██║      ██╔██╚╗╚██╗ ██╔╝")      
    print("██║     █████╗     ██║      ███████╗    ██████╔╝██║     ██╔╝ ██║ ╚████╔╝ ")
    print("██║     ██╔══╝     ██║      ╚════██║    ██╔═══╝ ██║     ███████║  ╚██╔╝  ")
    print("███████╗███████╗   ██║      ███████║    ██║     ███████╗██║  ██║   ██║   ")
    print("╚══════╝╚══════╝   ╚═╝      ╚══════╝    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ")
    print()
    print("     ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗    ")
    print("     ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║    ")
    print("     ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║    ")
    print("     ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║    ")
    print("     ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║    ")
    print("     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝    ")


          
def show_credits():
    print(" ██████╗    ███═╗ ███╗     ███╗███████╗     ██████╗ ██╗     ██╗███████╗██████╗ ")
    print("██╔════╝   ██╔██╚╗████╗   ████║██╔════╝    ██╔═══██╗╚██╗   ██╔╝██╔════╝██╔══██╗")
    print("██║  ████╗██╔╝ ██║██╔██╗ ██╔██║█████╗      ██║   ██║ ╚██╗ ██╔╝ █████╗  ██████╔╝")
    print("██║    ██║███████║██║╚████╔╝██║██╔══╝      ██║   ██║  ╚████╔╝  ██╔══╝  ██╔══██╗")
    print("╚███████╔╝██║  ██║██║ ╚██╔╝ ██║███████╗    ╚██████╔╝   ╚██╔╝   ███████╗██║  ██║")
    print(" ╚══════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═╝╚══════╝     ╚═════╝     ╚═╝    ╚══════╝╚═╝  ╚═╝")

    print("by Zoe Stuart")

def game_display(solved, wrong, strikes, word):
    
    if strikes == 0:
        print("******************************************************")
        print("*  ______________________                        ")
        print("*  | .__________))______|      Your Word:        ")
        print("*  | | / /      ||               " + solved + "                ")
        print("*  | |/ /       ||                               ")
        print("*  | | /        ||             Wrong Letters:    ")
        print("*  | |/         ||               " + wrong[:-2] + "                ")
        print("*  | |          ||                               ")
        print("*  | |          ( \\                              ")
        print("*  | |           \\_)                             ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |*********************|                     ")
        print("*  | |*******************| |                     ")
        print("*  | |                   | |                     ")
        print("*  | |                   | |                     ")
        print("*  | |                   | |                     ")
        print("*****************************************************")
        print()
        print()
        
    elif strikes == 1:
        print()
        print()
        print()
        print()
        print("******************************************************")
        print("*  ______________________                        ")
        print("*  | .__________))______|      Your Word:        ")
        print("*  | | / /      ||               " + solved + "                ")
        print("*  | |/ /       ||                               ")
        print("*  | | /        ||.-''.        Wrong Letters:    ") 
        print("*  | |/         |/     \\         " + wrong[:-2] + "                ")
        print("*  | |          ||     |                         ")
        print("*  | |          ( \\ _.'                          ")
        print("*  | |           `--'                            ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |*********************|                     ")
        print("*  | |*******************| |                     ")
        print("*  | |                   | |                     ")
        print("*  | |                   | |                     ")
        print("*  | |                   | |                     ")
        print("*****************************************************")
        print()
        print()

    elif strikes == 2:
        print()
        print()
        print()
        print()
        print("******************************************************")
        print("*  ______________________                        ")
        print("*  | .__________))______|      Your Word:        ")
        print("*  | | / /      ||               " + solved + "                ")
        print("*  | |/ /       ||                               ")
        print("*  | | /        ||.-''.        Wrong Letters:    ") 
        print("*  | |/         |/     \\         " + wrong[:-2] + "                ")
        print("*  | |          ||     |                         ")
        print("*  | |          ( \\ _.'                          ")
        print("*  | |         .-`--'.                           ")
        print("*  | |         |     |                           ")
        print("*  | |          |   |                            ")
        print("*  | |          |   |                            ")
        print("*  | |          |   |                            ")
        print("*  | |          |___|                            ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |*********************|                     ")
        print("*  | |*******************| |                     ")
        print("*  | |                   | |                     ")
        print("*  | |                   | |                     ")
        print("*  | |                   | |                     ")
        print("*****************************************************")
        print()
        print()
    elif strikes == 3:
        print()
        print()
        print()
        print()
        print("******************************************************")
        print("*  ______________________                        ")
        print("*  | .__________))______|      Your Word:        ")
        print("*  | | / /      ||               " + solved + "                ")
        print("*  | |/ /       ||                               ")
        print("*  | | /        ||.-''.        Wrong Letters:    ") 
        print("*  | |/         |/     \\         " + wrong[:-2] + "                ")
        print("*  | |          ||     |                         ")
        print("*  | |          ( \\ _.'                          ")
        print("*  | |         .-`--'.                           ")
        print("*  | |         |      \\                          ")
        print("*  | |          |   | \\\\                         ")
        print("*  | |          |   |  \\\\                        ")
        print("*  | |          |   |   (`                       ")
        print("*  | |          |___|                            ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |*********************|                     ")
        print("*  | |*******************| |                     ")
        print("*  | |                   | |                     ")
        print("*  | |                   | |                     ")
        print("*  | |                   | |                     ")
        print("*****************************************************")
        print()
        print()
        
    elif strikes == 4:
        print()
        print()
        print()
        print()
        print("******************************************************")
        print("*  ______________________                        ")
        print("*  | .__________))______|      Your Word:        ")
        print("*  | | / /      ||               " + solved + "                ")
        print("*  | |/ /       ||                               ")
        print("*  | | /        ||.-''.        Wrong Letters:    ") 
        print("*  | |/         |/     \\         " + wrong[:-2] + "                ")
        print("*  | |          ||     |                         ")
        print("*  | |          ( \\ _.'                          ")
        print("*  | |         .-`--'.                           ")
        print("*  | |        /       \\                          ")
        print("*  | |       // |   | \\\\                         ")
        print("*  | |      //  |   |  \\\\                        ")
        print("*  | |     ')   |   |   (`                       ")
        print("*  | |          |___|                            ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |                                           ")
        print("*  | |*********************|                     ")
        print("*  | |*******************| |                     ")
        print("*  | |                   | |                     ")
        print("*  | |                   | |                     ")
        print("*  | |                   | |                     ")
        print("*****************************************************")
        print()
        print()
        
    elif strikes == 5:
        print()
        print()
        print()
        print()
        print("******************************************************")
        print("*  ______________________                        ")
        print("*  | .__________))______|      Your Word:        ")
        print("*  | | / /      ||               " + solved + "                ")
        print("*  | |/ /       ||                               ")
        print("*  | | /        ||.-''.        Wrong Letters:    ") 
        print("*  | |/         |/     \\         " + wrong[:-2] + "                ")
        print("*  | |          ||     |                         ")
        print("*  | |          ( \\ _.'                          ")
        print("*  | |         .-`--'.                           ")
        print("*  | |        /       \\                          ")
        print("*  | |       // |   | \\\\                         ")
        print("*  | |      //  |   |  \\\\                        ")
        print("*  | |     ')   |__ |   (`                       ")
        print("*  | |             ||                            ")
        print("*  | |             ||                            ")
        print("*  | |             ||                            ")
        print("*  | |             ||                            ")
        print("*  | |             |_\\                           ")
        print("*  | |*********************|                     ")
        print("*  | |*******************| |                     ")
        print("*  | |                   | |                     ")
        print("*  | |                   | |                     ")
        print("*  | |                   | |                     ")
        print("*****************************************************")
        print()
        print()
    elif strikes == 6:
        print()
        print()
        print()
        print()
        print("******************************************************")
        print("*  ______________________                        ")
        print("*  | .__________))______|  ________              ")
        print("*  | | / /      ||        / Oh NO! )             ")
        print("*  | |/ /       ||       / Hurry! /              ")
        print("*  | | /        ||.-''. (  ______/               ")
        print("*  | |/         |/     \\ \/                      ")
        print("*  | |          ||     |                         ")
        print("*  | |          ( \\ _.'           Your Word:     ")
        print("*  | |         .-`--'.              " + solved + "                ")
        print("*  | |        /       \\                          ")
        print("*  | |       // |   | \\\\          Wrong Letters: ")
        print("*  | |      //  |   |  \\\\           " + wrong[:-2] + "                ") 
        print("*  | |     ')   |   |   (`                       ")
        print("*  | |          || ||                            ")
        print("*  | |          || ||                            ")
        print("*  | |          || ||                            ")
        print("*  | |          || ||                            ")
        print("*  | |         /_| |_\\                           ")
        print("*  | |*********************|                     ")
        print("*  | |*******************| |                     ")
        print("*  | |                   | |                     ")
        print("*  | |                   | |                     ")
        print("*  | |                   | |                     ")
        print("*****************************************************")
        print()
        print()
    elif strikes == 7:
        print()
        print()
        print()
        print()
        print("******************************************************")
        print("*  ______________________                        ")
        print("*  | .__________))______|      Your Word Was:    ")
        print("*  | | / /      ||               " + word + "                ")
        print("*  | |/ /       ||                               ")
        print("*  | | /        ||.-''.        Wrong Letters:    ") 
        print("*  | |/         |/ x x \\         " + wrong[:-2] + "                ")
        print("*  | |          ||  *  |                         ")
        print("*  | |          ( \\ _.'                          ")
        print("*  | |         .-`--'.                           ")
        print("*  | |        /       \\                          ")
        print("*  | |       // |   | \\\\                         ")
        print("*  | |      //  |   |  \\\\                        ")
        print("*  | |     ')   |   |   (`                       ")
        print("*  | |          || ||                            ")
        print("*  | |          || ||                            ")
        print("*  | |          || ||                            ")
        print("*  | |          || ||                            ")
        print("*  | |         / | | \\                           ")
        print("*  | |******|_ `-' `-' |***|                     ")
        print("*  | |*******\\ \\       **|*|                     ")
        print("*  | |        \\ \\        | |                     ")
        print("*  | |         \\ \\       | |                     ")
        print("*  | |          `'       | |                     ")
        print("*****************************************************")
        print()
        print()

def win_screen():
    print("██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗")
    print("╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║")
    print(" ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║")
    print("  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║")
    print("   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║")
    print("   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝")
   
def lose_screen():
    print("██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗")
    print("╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝")
    print(" ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  ")
    print("  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  ")
    print("   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗")
    print("   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝")              

def get_category(path):
    files = os.listdir(path)

    print("Choose a category...")
    
    for i, f in enumerate(files):
        
        full_path = path + "/" + f
        
        with open(full_path, 'r') as file:
            print(str(i + 1) + ") " + file.readline().strip())

    choice = input("Enter selection: ")
    choice = int(choice)

    return path + "/" + files[choice - 1]

def get_puzzle(file):

    with open(file, 'r') as f:
        words = f.read().splitlines()

    return random.choice(words[1:])

def check(word, solved, guesses):
    
    for i in range(len(word)):
        if word[i].lower() in guesses or not word[i].isalpha():
            solved = solved[:i] + word[i] + solved[i+1:]


    return solved

def get_guess():
    while True:
        
        guess = input("Guess a letter: ")

        if len(str(guess)) == 1 and guess.isalpha():
            return guess.lower()
        else:
            print("I don't understand. Please type a single letter.")

    
def play_again():

    while True:
        print()
        answer = input("Would you like to play again?")

        if answer.lower() == 'no' or answer.lower() == 'n':
            return False   
        elif answer.lower() == 'yes' or answer.lower() == 'y':
            return True
        print("I don't understand. Please type yes or no.")



def play():

    puzzle_dir = 'puzzles'
    category_file = get_category(puzzle_dir)
    word = get_puzzle(category_file)
    solved = "-" * len(word)

    right = ""
    wrong = ""
    strikes = 0
    limit = 7
    
    solved = check(word, solved, right)
    game_display(solved, wrong, strikes, word) 

    while word != solved and strikes < limit:
        letter = get_guess()

        if letter.lower() not in word.lower():
            strikes += 1
            wrong += (letter + ", ")
            
        right += letter

        solved = check(word, solved, right)
        game_display(solved, wrong, strikes, word)


    if word == solved:
        win_screen()
    else:
        lose_screen()


def main():
    show_start_screen()

    playing = True

    while playing == True:       
        play()
        playing = play_again()
    
    show_credits()


# code execution begins here
if __name__ == "__main__":
    main()
