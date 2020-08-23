import csv
import random
import sys
tmp = []
with open("sample.csv") as sample:
    reader = csv.DictReader(sample)
    for row in reader:
        quote = row.get("quote")
        pos = dict()
        for i in range(len(quote)):
            if quote[i] in pos:
                pos[quote[i]].append(i)
            else:
                pos[quote[i]] = [i]
        tmp.append((quote, pos))

game_incorrect_threshold = 6
while True:
    elem = random.choice(tmp)
    quote = elem[0]
    pos = elem[1]
    state = ['_' for c in quote]

    flag = False
    correct_guesses = []
    incorrect_guesses = []
    correct_chars = 0
    while not flag:
        print("guess a character")
        c = input()

        if c in pos:
            correct_guesses.append(c)
            indexes = pos[c]
            for index in indexes:
                correct_chars += 1
                state[index] = str(c)
            if correct_chars == len(state):
                print("congates you guessed the name correctly")
                flag = False
                continue
            print("good")
            for c in state:
                print(c, end="")
            print()
            print("correct_guesses", correct_guesses)
            print("incorrect_guesses", incorrect_guesses)
            print("chances {}/{}".format(incorrect_guesses, game_incorrect_threshold))
        else:
            incorrect_guesses.append(c)
            if len(incorrect_guesses) == game_incorrect_threshold:
                print("You loose")
                flag = False
            print("Nope")
            print()
            print("correct_guesses", correct_guesses)
            print("incorrect_guesses", incorrect_guesses)
            print("chances {}/{}".format(incorrect_guesses, game_incorrect_threshold))

    print("do you want to quit the game enter q for quit n for no:", end="")
    choice = input()
    if choice == 'q':
        flag = True
