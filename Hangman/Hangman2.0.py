import random

def replace(character):
    global new_word
    global temp
    cycles = word.count(character)
    for x in range(cycles):
        position = temp.find(character)
        new_word = new_word[:position] + character + new_word[position + 1:]
        temp = temp[:position] + " " + temp[position + 1:]
        print(position)
    return new_word

play = "Y"

while play == "Y":

    play = "Y"

    while play == "Y":
        words = ["Water", "Fire", "Earth", "Air", "Eyes", "Wizard", "Hut","Peel","Boom"]
        word = random.choice(words)
        word = word.upper()
        list_o_letters = []
        letter_count = len(word)
        new_word = letter_count * "_ "
        lives = 5
        long_word = ""

        for i in word:
            long_word += i
            long_word += " "

        temp = long_word

        while new_word != long_word and lives != 0:
            flag = False
            temp = long_word
            while not flag:
                print(new_word)
                guess = input("What letter do you want to guess?: ").upper()
                if guess.isalpha() and len(guess) == 1:
                    flag = True
                else:
                    print(f"{guess} is not a valid input!")
            tries = letter_count
            for i in range(len(word)):
                if guess == word[i]:
                    new_word = replace(guess)
                    print(new_word)
                    break
                else:
                    tries -= 1
                    if tries == 0:
                        lives -= 1
                        print(f"You have {lives} more attempts!")
                        list_o_letters.append(guess)
                        print(new_word)
            print(f"Letters used '{list_o_letters}'")

        if lives == 0:
            print("Nice try better luck next time!"
                  f"The word was: {word}")
        else:
            print(f"Congratulations you won with {lives} lives reamining!")
        replay = ""
        replay = input('If you would like to play again type "Y"\nType anything else to quit.').upper()
        if replay == "Y":
            continue
        else:
            play = "333"