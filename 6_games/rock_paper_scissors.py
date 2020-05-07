#!/usr/bin/env python

import random, os, sys

wins = 0
loses = 0
ties = 0
moves = ['r', 'p', 's', 'q', '']
move = ''

while True:
    print('*** ROCK, PAPER, SCISSORS ***')
    if move not in moves:
        print('{} is not an option'.format(str(move)))
    elif move == moves[3]:
        os.system('clear')
        print('Thanks for playing!')
        print('FINAL RESULTS: Wins: {} Loses: {} Ties: {}'.format(str(wins), str(loses), str(ties)))
        sys.exit()
    else:
        randomMove = moves[random.randint(0, 2)]
        if move == moves[0]:
            if randomMove == move:
                print('I choose...ROCK!!!')
                print("It's a tie!")
                ties += 1
            elif randomMove == moves[1]:
                print('I choose...PAPER!!!')
                print('PAPER BEATS ROCK!!!')
                print('You lose')
                loses += 1
            else:
                print('I choose...SCISSORS!!!')
                print('Ooof! Rock beats scissors.')
                print('You win')
                wins += 1

        if move == moves[1]:
            if randomMove == move:
                print('I choose...PAPER!!!')
                print("It's a tie!")
                ties += 1
            elif randomMove == moves[2]:
                print('I choose...SCISSORS!!!')
                print('SCISSORS BEATS PAPER!!!')
                print('You lose')
                loses += 1
            else:
                print('I choose...ROCK!!!')
                print('Ooof! Paper beats rock.')
                print('You win')
                wins += 1

        if move == moves[2]:
            if randomMove == move:
                print('I choose...SCISSORS!!!')
                print("It's a tie!")
                ties += 1
            elif randomMove == moves[0]:
                print('I choose...ROCK!!!')
                print('ROCK BEATS SCISSORS!!!')
                print('You lose')
                loses += 1
            else:
                print('I choose...PAPER!!!')
                print('Ooof! Scissors beats paper.')
                print('You win')
                wins += 1

    print("Wins: {} Loses: {} Ties: {}".format(str(wins), str(loses), str(ties)))
    move = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ')
    os.system('clear')
