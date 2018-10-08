def hangman(word):
    wrong = 0
    stage = ["",
    "___________",
    "|     |    ",
    "|     0    ",
    "|    /|\   ",
    "|    / \   ",
    "|          "
    ]
    reletters = list(word)
    board = ["_"] * len(word)
    win = False

    print("welcome to hangman!")
    while wrong < len(stage) - 1:
        print("\n")
        msg = "type a chara"
        char = input(msg)
        if char in reletters:
            cind = reletters.index(char)
            board[cind] = char
            reletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stage[0:e]))
        if "_" not in board:
            print("You win")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stage[0:wrong+1]))
        print("You lose!Answer is {}.".format(word))

hangman("cat")
