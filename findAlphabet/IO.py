'''
欠落しているアルファベットを検出するCUIゲーム
書籍「Pythonでつくるゲーム開発」に掲載されていたものをアレンジしています。
'''

class IO:
	def output(self,str):
		print(str)
		
	def input(self):
		word = input()
		return word
