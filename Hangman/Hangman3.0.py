import random
def check4repeats(guess):
    global flag
    for i in list_o_letters:
        if guess == i:
            pass
            return False
def health():
    global lives
    lives = 5 - len(list_o_letters)
def replace(character):
    global new_word
    global temp
    cycles = word.count(character)
    for x in range(cycles):
        position = temp.find(character)
        new_word = new_word[:position] + character + new_word[position + 1:]
        temp = temp[:position] + " " + temp[position + 1:]
    if cycles == 0:
        for value in character:
            if value in list_o_letters:
                continue
            else:
                list_o_letters.append(character)
    return new_word
play = "Y"
while play == "Y":
    play = "Y"
    while play == "Y":
        words = ["Water", "Fire", "Earth", "Air", "Eyeball", "Wizard", "Hut"]
        word = random.choice(words)
        word = word.upper()
        list_o_letters = []
        letter_count = len(word)
        new_word = letter_count * "_ "
        long_word = ""
        lives = 5
        for i in word:
            long_word += i
            long_word += " "
        temp = long_word
        while new_word != long_word and lives != 0:
            flag = False
            temp = long_word
            print(new_word)
            while not flag:
                guess = input("What letter would you like to guess?: ").upper()
                if guess.isalpha() and len(guess) == 1:
                    check4repeats(guess)
                    break
                else:
                    print(f'"{guess}" is not a valid input!')
                    pass
            new_word = replace(guess)
            health()
            print(f"You have {lives} more lives!")
            print(f"Incorrect letters: {list_o_letters}.")
        if lives == 0:
            print(f" \nNice try better luck next time!\nThe word was: {word}\n ")
        else:
            if lives == 1:
                print(f" \nCongratulations you won with 1 life remaining!\n ")
            else:
                print(f" \nCongratulations you won with {lives} lives remaining!\n ")
        replay = input('If you would like to play again type "Y"\nType anything else to quit.').upper()
        if replay == "Y":
            continue
        else:
            play = "333"