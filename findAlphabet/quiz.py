'''
欠落しているアルファベットを検出するCUIゲーム
書籍「Pythonでつくるゲーム開発」に掲載されていたものをアレンジしています。
'''

import random
import datetime

#入出力
class SystemIO:
	def print(self, word):
		print(word)

	def input(self):
		return(input())

#game flow
class FindLetter:
	#プロパティ
	QUESTION = ''
	r = ''
	answer = ''
	playtime = []

	def __init__(self):
		#問題文
		self.QUESTION = [
			'A','B','C','D','E','F','G',
			'H','I','J','L','M','N','O',
			'P','Q','R','S','T','V','W',
			'X','Y','Z'
		]
		#正解
		self.r = random.choice(self.QUESTION)

	def description(self):
		#説明
		q_str = 'アルファベットがランダムに並んでいますが、一文字欠けています。\n欠けている文字はなんでしょうか？\n'
		#問題文生成
		random.shuffle(self.QUESTION)

		for i in self.QUESTION:
			if i != self.r:
				q_str = q_str + i

		return q_str

	def your_answer(self, answer):
		self.answer = answer

	def judge(self):
		judgement = ''
		if self.answer == self.r:
			judgement = '正解！ 解答にかかった時間は{}秒でした'.format(self.get_diff_time())
		else:
			judgement = '残念! 正解は{}でした'.format(self.r)
		return judgement
	
	def set_play_time(self):
		self.playtime.append(datetime.datetime.now())

	def get_diff_time(self):
		playtime = (self.playtime[1] - self.playtime[0]).seconds
		return playtime 


game = FindLetter()
io = SystemIO()
#問題出力
io.print(game.description())
#開始時間計測
game.set_play_time()
#解答入力
game.your_answer(io.input())
#終了時間計測
game.set_play_time()
#判定
io.print(game.judge())