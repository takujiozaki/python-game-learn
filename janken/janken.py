'''
じゃんけんゲーム
日経ソフトウエア２０１９年１１月号に掲載されていたもの
'''
import random

class Janken(object):
    HANDS = ['グー', 'チョキ', 'パー']

    def description(self):
        return "グー: 0 チョキ: 1 パー: 2"

    def your_and_enemy_hand(self, you, enemy):
        return "あなた：{} 相手：{}".format(self.HANDS[you], self.HANDS[enemy])

    def enemy_hand(self):
        return random.randint(0, len(self.HANDS) -1)

    def judge(self, you, enemy):
        result = (you - enemy) % len(self.HANDS)
        if result == 0:
            return "DRAW"
        elif result == 1:
            return "LOSE"
        else:
            return "WIN"


class SystemIO(object):

    def print(self, message):
        print(message)

    def input(self):
        return input()


class GameFlow(object):

    def __init__(self, game, flow_io):
        self.game = game
        self.flow_io = flow_io

    def play(self):
        self.flow_io.print(self.game.description())
        you = int(self.flow_io.input())
        enemy = int(self.game.enemy_hand())
        self.flow_io.print(self.game.your_and_enemy_hand(you, enemy))
        result = self.game.judge(you, enemy)
        self.flow_io.print(result)


# GAME START
game = Janken()
flow_io = SystemIO()
flow = GameFlow(game, flow_io)
flow.play()

