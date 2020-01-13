'''
じゃんけんゲーム
日経ソフトウエア２０１９年１１月号に掲載されていたもの
クラスメソッドを使った例
'''
import random

class Janken:
    HANDS = ['グー', 'チョキ', 'パー']

    @classmethod
    def description(cls):
        print('グー:0 チョキ:1 パー:2')

    @classmethod
    def your_hand_and_enemy_hand(cls, you, enemy):
        print('あなた： {0},相手：{1}'.format(cls.HANDS[you],cls.HANDS[enemy]))

    @classmethod
    def enemy_hand(cls):
        return random.randint(0, len(cls.HANDS)-1)

    @classmethod
    def judge(cls, you, enemy):
        result = (you - enemy) % 3
        if result == 0:
            print('DRAW')
        elif result == 1:
            print('LOSE')
        else:
            print('WIN')

class GameFlow:
    @classmethod
    def play(cls):
        Janken.description()
        you = int(input())
        enemy = Janken.enemy_hand()
        Janken.your_hand_and_enemy_hand(you, enemy)
        Janken.judge(you, enemy)

GameFlow.play()