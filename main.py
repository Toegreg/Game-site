import os
from re import X
import random
import time


class game:
    # variables
    def __init__(self):
        self.moves = 0
        self.omoves = 0
        self.xplaces = []
        self.oplaces = []
        self.win = 'no'
        self._11 = ' '
        self._12 = '| |'
        self._13 = ' '
        self._21 = '_'
        self._22 = '|_|'
        self._23 = '_'
        self._31 = '_'
        self._32 = '|_|'
        self._33 = '_'
        self.numbers = [1, 2, 3]
        self.players = 0

    # checks if you win

    def winning_conditions(self):
        if self._11 == 'X' and self._21 == 'X' and self._31 == 'X':
            print('You win!')
            self.win = 'yes'
        if self._12 == '|X|' and self._22 == '|X|' and self._32 == 'X':
            print('You win!')
            self.win = 'yes'
        if self._13 == 'X' and self._23 == 'X' and self._33 == 'X':
            print('You win!')
            self.win = 'yes'
        if self._11 == 'X' and self._12 == '|X|' and self._13 == 'X':
            print('You win!')
            self.win = 'yes'
        if self._21 == 'X' and self._22 == '|X|' and self._23 == 'X':
            print('You win!')
            self.win = 'yes'
        if self._31 == 'X' and self._32 == '|X|' and self._33 == 'X':
            print('You win!')
            self.win = 'yes'
        if self._11 == 'X' and self._22 == '|X|' and self._33 == 'X':
            print('You win!')
            self.win = 'yes'
        if self._31 == 'X' and self._22 == '|X|' and self._13 == 'X':
            print('You win!')
            self.win = 'yes'

        if self._11 == 'O' and self._21 == 'O' and self._31 == 'O':
            print('AI wins!')
            self.win = 'yes'
        if self._12 == '|O|' and self._22 == '|O|' and self._32 == 'O':
            print('AI wins!')
            self.win = 'yes'
        if self._13 == 'O' and self._23 == 'O' and self._33 == 'O':
            print('AI wins!')
            self.win = 'yes'
        if self._11 == 'O' and self._12 == '|O|' and self._13 == 'O':
            print('AI wins!')
            self.win = 'yes'
        if self._21 == 'O' and self._22 == '|O|' and self._23 == 'O':
            print('AI wins!')
            self.win = 'yes'
        if self._31 == 'O' and self._32 == '|O|' and self._33 == 'O':
            print('AI wins!')
            self.win = 'yes'
        if self._11 == 'O' and self._22 == '|O|' and self._33 == 'O':
            print('AI wins!')
            self.win = 'yes'
        if self._31 == 'O' and self._22 == '|O|' and self._13 == 'O':
            print('AI wins!')
            self.win = 'yes'

    # updates the board

    def updategameboard(self):
        if '1,1' in self.xplaces:
            self._11 = 'X'
        if '1,2' in self.xplaces:
            self._12 = '|X|'
        if '1,3' in self.xplaces:
            self._13 = 'X'
        if '2,1' in self.xplaces:
            self._21 = 'X'
        if '2,2' in self.xplaces:
            self._22 = '|X|'
        if '2,3' in self.xplaces:
            self._23 = 'X'
        if '3,1' in self.xplaces:
            self._31 = 'X'
        if '3,2' in self.xplaces:
            self._32 = '|X|'
        if '3,3' in self.xplaces:
            self._33 = 'X'
        if '1,1' in self.oplaces:

            self._11 = 'O'
        if '1,2' in self.oplaces:
            self._12 = '|O|'
        if '1,3' in self.oplaces:
            self._13 = 'O'
        if '2,1' in self.oplaces:
            self._21 = 'O'
        if '2,2' in self.oplaces:
            self._22 = '|O|'
        if '2,3' in self.oplaces:
            self._23 = 'O'
        if '3,1' in self.oplaces:
            self._31 = 'O'
        if '3,2' in self.oplaces:
            self._32 = '|O|'
        if '3,3' in self.oplaces:
            self._33 = 'O'

    # generates the board

    def createboard(self):
        os.system('clear')
        print(self._31, self._32, self._33)
        print(self._21, self._22, self._23)
        print(self._11, self._12, self._13)

    # 0's move if there are two players

    def player2move(self):
        print('Player 2, what is your move?')
        print('What Y position do you want to place your X?')
        playermovex = input()
        while int(playermovex) > 3:
            print('error')
            playermovex = input()
        print('What X position do you want to place your X?')
        playermovey = input()
        while int(playermovey) > 3:
            print('error')
            playermovey = input()
        var = playermovex + "," + playermovey
        if self.moves + self.omoves == 9 and not self.win == 'yes':
            print('Its a tie!')
        elif var in self.xplaces or var in self.oplaces:
            os.system('clr')
            self.createboard()
            print('Spot alredy taken, try again')
            self.player2move()
        else:
            self.oplaces.insert(self.omoves, var)
            self.omoves += 1
            self.updategameboard()
            self.createboard()
            self.winning_conditions()
            if self.win != 'yes':
                self.playermove()

    # x's move

    def playermove(self):
        if self.players == 2:
            print('Player 1, what is your move?')
        print('What Y position do you want to place your X?')
        playermovex = input()
        while int(playermovex) > 3:
            print('error')
            playermovex = input()
        print('What X position do you want to place your X?')
        playermovey = input()
        while int(playermovey) > 3:
            print('error')
            playermovey = input()
        var = playermovex + "," + playermovey
        if self.moves + self.omoves == 9 and not self.win == 'yes':
            print('Its a tie!')
        elif var in self.xplaces or var in self.oplaces:
            os.system('clr')
            self.createboard()
            print('Spot alredy taken, try again')
            self.playermove()
        else:
            self.xplaces.insert(self.moves, var)
            self.moves += 1
            self.updategameboard()
            self.createboard()
            self.winning_conditions()
            if self.win == 'no':
                if self.players == 2:
                    self.player2move()
                else:
                    self.aimove()
            else:
                pass

    # aimove

    def aimove(self):
        omoveX = random.choice(self.numbers)
        omoveY = random.choice(self.numbers)
        while str(omoveX) + "," + str(omoveY) in self.xplaces or str(omoveX) + "," + str(omoveY) in self.oplaces:
            omoveX = random.choice(self.numbers)
            omoveY = random.choice(self.numbers)
        if self.moves + self.omoves == 9:
            print('Its a tie!')
        else:
            self.oplaces.insert(self.omoves, str(omoveX) + "," + str(omoveY))

        self.omoves += 1
        self.updategameboard()
        self.createboard()
        self.playermove()

    # begining of the game

    def game_initialize(self):
        print('Welcome to TickTackToe!')
        print('Say "begin" to start the game')
        while not input() == "begin":
            pass
        print('How many players? one or two?')
        self.players = int(input())
        if self.players != 1 and self.players != 2:
            print("Sorry please input '1' or '2'. ")
        os.system('clear')
        self.createboard()
        self.playermove()


game().game_initialize()
