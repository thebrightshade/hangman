#!/Users/skb/anaconda3/bin/python
'''Hangman - You will have to guess the letters of a random word.
 You will be shown the number of letters the word has,
 each correct guess will populate the appropriate position 
 for that letter in the word.
 You will be allowed seven(7) wrong guesses, 
 once you exhaust the 7th wrong guess, you lose the game'''

import random


alreadySaid = ""


def main():
    gw, dw = set_guess_word()
    print("Word: {}\n".format(gw))
    playing(gw, dw, alreadySaid)


def set_guess_word():
    '''This function creates a list of words, 
    from the words in the text file and selects a 
    random word from that list as the guess word.
    Also sets the display word of the same length using "_".'''

    with open("words.txt", "r") as myWordFile:
        myWordList = []
        for word in myWordFile:
            myWordList.append(word.strip().lower())

    guessWord = random.choice(myWordList)
    dispWord = ["-" for char in guessWord]
    return guessWord, dispWord


def playing(guessWord, dispWord, alreadySaid):
    try:
        while dispWord != guessWord:
            playerSaid = input("Guess a letter: ")

            if playerSaid.lower() not in alreadySaid:
                alreadySaid = alreadySaid + playerSaid
            else:
                print("You already used that letter")

            if playerSaid.lower() in guessWord:
                dispWord = [
                    char if char == playerSaid or
                    char in alreadySaid else "-" for char in guessWord]
                dispWord = "".join(dispWord)
            else:
                print("Not in word.")

            print(dispWord)
            print("Letters Used: {}".format(alreadySaid))
            playing(guessWord, dispWord, alreadySaid)
            print(dispWord == guessWord)
        else:
            print("You win!")
            return dispWord
    except KeyboardInterrupt:
        raise


if __name__ == '__main__':
    main()
