import random

def hangman():
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    wrong = 0
    word_list = ["soccer","baseball","handball","swimming"]
    random_number = random.randint(0,4)
    word = word_list[random_number]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to hangman game!")

    while wrong < len(stages) -1:
        print("\n")
        message = "Type a character!"
        character = input(message)
        if character in rletters:
            number = rletters.index(character)
            board[number] = character
            rletters[number] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        #When wrong == 3,alart!
        if wrong == 3 and word == "soccer":
            print("The answer is team sports! And the sports uses ball!")
        if wrong == 3 and word == "baseball":
            print("The answer is team sports and the sparts uses ball and iron stick!")
        if wrong == 3 and word == "handball":
            print("The answer is team sports and you use small ball to play it")
        if wrong == 3 and word == "swimming":
            print("The sport is competition.")
        
        if "_" not in board:
            print("You are winner!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You are loser!The answer is {}.".format(word))

hangman()
        
    
