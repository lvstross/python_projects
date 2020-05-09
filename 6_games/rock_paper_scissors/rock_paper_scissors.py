#!/usr/bin/env python

import random, os, sys
from move import Move
from game import Game

nG = Game()

while True:
    print('*** ROCK, PAPER, SCISSORS ***')
    if nG.move not in nG.moves:
        print('{} is not an option'.format(str(nG.move)))
    elif nG.move == nG.moves[3]:
        os.system('clear')
        print('Thanks for playing!')
        print('FINAL RESULTS:')
        nG.getStats()
        sys.exit()
    else:
        randomMove = nG.moves[random.randint(0, 2)]
        if nG.move == nG.moves[0]:
            rock = Move(nG.moves[0], nG.moves[1], nG.moves[2]);
            rock.check(randomMove, nG)
        if nG.move == nG.moves[1]:
            paper = Move(nG.moves[1], nG.moves[2], nG.moves[0]);
            paper.check(randomMove, nG)
        if nG.move == nG.moves[2]:
            scissors = Move(nG.moves[2], nG.moves[0], nG.moves[1]);
            scissors.check(randomMove, nG)


    nG.getStats()
    nG.getMove()
    os.system('clear')
