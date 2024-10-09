import random



def wordle():

    # choose a random number between 1 and 3103 (inclusive)
    rand = random.randrange(1, 3104)

    # read through the csv file and stop at that number
    with open('WORDS.csv')as file:
        i = 1

        while i != rand:
            file.readline()
            i += 1

        word = file.readline().lower()

    # tell user the word has been picked and to start guessing
    print("a word has been picked!\n")

    # check if each letter in the guess is correct
    correct = False
    rounds = 1
    letters_used = set([])

    while (not correct) and (rounds <=5):
        guess = input("what's your guess?\n").lower()
        if word == guess:
            print("YOU GOT IT!!!! THE WORD IS {}".format(word))
            correct = True
        else:
            output = checker(word, guess, letters_used)
            result, letters_used = output[0], output[1]
            print("close, here's a hint:\n")
            print("letters used: {}\n".format(letters_used))
            print(result)

        rounds += 1

    if not correct:
        print("better luck next time, the word was: {}".format(word))


def checker(word, guess, letters_used):
    final = ['_', '_', '_', '_', '_']
    for i in range(len(word)-1):
        if guess[i] == word[i]:
            final[i] = word[i].upper()
        elif guess[i] in word:
            final[i] = guess[i]
        else:
            letters_used.add(guess[i])
    final_word = ''.join(final)
    return [final_word, letters_used]


wordle()

