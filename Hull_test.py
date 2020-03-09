import random as rd

Three_board = [0, 0, 1]

class Audience():
    def __init__(self,name):
        self.name = name
        self.score_A = 0
        self.score_B = 0
        self.index = 0
    def get_board(self):
        self.index = rd.sample(range(0,3),1)[0]
    def select_A(self):
        self.score_A += Three_board[self.index]
    def select_B(self,sheep_index):
        self.score_B += Three_board[3-self.index-sheep_index]

class Host():
    def __init__(self,name):
        self.name = name
        self.sheep_index = 0

    def Shuffle(self):
        rd.shuffle(Three_board)
        
    def get_sheep_index(self, Audience_index):
        if Three_board.index(1) == 0:
            if Audience_index == 0:
                self.sheep_index = rd.sample(range(1,3),1)[0]
            else:
                self.sheep_index = 3-Audience_index
        elif Three_board.index(1) == 1:
            if Audience_index == 1:
                self.sheep_index = rd.sample(range(0,2),1)[0]*2
            else:
                self.sheep_index = 2-Audience_index
        else:
            if Audience_index == 2:
                self.sheep_index = rd.sample(range(0,2),1)[0]
            else:
                self.sheep_index = 1-Audience_index

host = Host('Bob')
audience = Audience('Jack')

for i in range(0,90000):
    host.Shuffle()
    audience.get_board()
    host.get_sheep_index(audience.index)
    audience.select_A()
    audience.select_B(host.sheep_index)

print('score_A =',audience.score_A/90000)
print('score_B =',audience.score_B/90000)

'''
A = 0
B = 0
C = 0
for i in range(0,900000):
    index = rd.sample(range(0,3),1)
    if index[0] == 0:
        A +=1
    elif index[0] == 1:
        B +=1
    else:
        C +=1
print('A:', A)
print('B:', B)
print('C:', C)
'''