class Game:
    stats = {
        "wins": 0,
        "loses": 0,
        "ties": 0
    }
    moves = ['r', 'p', 's', 'q', '']
    move = ''

    def getMove(self):
        self.move = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ')

    def addWin(self):
        self.stats['wins'] += 1

    def addLose(self):
        self.stats['loses'] += 1

    def addTie(self):
        self.stats['ties'] += 1

    def getStats(self):
        print("Wins: {} Loses: {} Ties: {}".format(
                str(self.stats['wins']),
                str(self.stats['loses']),
                str(self.stats['ties'])
            )
        )
