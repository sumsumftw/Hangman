import random

words = ["Water", "Fire", "Earth", "Air","Eyes","Wizard","Hut"]
word = random.choice(words)
word = word.upper()
long_word = ""
new_position = 0
list_o_letters = []
letters = len(word)
new_word = letters * "_ "
new_position = 0
temp = word
count = letters
lives = 5
for i in word:
    long_word += i
    long_word += " "

def replace(character, position):
    global new_word
    cycles = word.count(guess)
    if cycles == 1: # I want the if statement to be >= 1 and get rid of the elif
        new_word = new_word[:position] + character + new_word[position + 1:]
    elif cycles >= 2:
        new_word = new_word[:position] + character + new_word[position + 1:]
        temp = word
        for x in range(cycles - 1):
            temp = temp[position + 1:]
            new_position = ((2 * x) + 2) + position
            new_word = new_word[:new_position] + character + new_word[new_position + 1:]
    return new_word

print(new_word)

while new_word != long_word and lives != 0:
    guess = input("What letter do you want to guess?: ").upper()
    tries = letters
    temp = ""
    for i in range(len(word)):
        if guess == word[i]:
            position = i * 2
            new_word = replace(guess, position)
            print(new_word)
            break
        else:
            tries -= 1
            if tries == 0:
                lives -= 1
                print(f"You have {lives} more attempts!")
                list_o_letters += guess
                print(new_word)
    print(f"Letters used '{list_o_letters}'")

if lives == 0:
    print("Nice try better luck next time!"
          f"The word was: {word}")
else:
    print(f"Congratulations you won with {lives} lives reamining!")