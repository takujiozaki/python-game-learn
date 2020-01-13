'''
欠落しているアルファベットを検出するCUIゲーム
書籍「Pythonでつくるゲーム開発」に掲載されていたものをアレンジしています。
'''

import random
import datetime

from findAlphabet import IO

# 出題


# 解答


# 判定


QUESTION = [
	'A','B','C','D','E','F','G',
	'H','I','J','L','M','N','O',
	'P','Q','R','S','T','V','W',
	'X','Y','Z'
	]
random.shuffle(QUESTION)
q_str = ''
r = random.choice(QUESTION)
for i in QUESTION:
	if i != r:
		q_str = q_str + i
		
io = IO.IO()

io.output(q_str)
io.output('欠けている文字はなんでしょう？')
start = datetime.datetime.now()

answer=io.input()

if answer == r:
	end = datetime.datetime.now()
	diff = (end - start).seconds
	io.output('正解')
	io.output('回答にかかった時間は{}秒でした'.format(str(diff)))
else:
	io.output('残念！')
	io.output('正解は{}です'.format(r))
