class Move:
    name = ''
    weakness = ''
    beats = ''
    moves = {
        'r': 'Rock',
        'p': 'Paper',
        's': 'Scissors'
    }

    def __init__(self, name, weakness, beats):
        self.name = name
        self.weakness = weakness
        self.beats = beats

    def check(self, move, game):
        if move == self.name:
            print('I choose...{}!!!'.format(self.moves[self.name]))
            print("It's a tie!")
            game.addTie()
        elif move == self.weakness:
            print('I choose...{}!!!'.format(self.moves[self.weakness]))
            print('You lose')
            game.addLose()
        else:
            print('I choose...{}!!!'.format(self.moves[self.beats]))
            print('You win')
            game.addWin()
        return game
