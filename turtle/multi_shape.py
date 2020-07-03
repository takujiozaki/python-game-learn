from turtle import Turtle

def shape(n,turtle,color):
	#色を設定
	turtle.color(color)
	#位置調整
	turtle.penup()
	turtle.backward(50)
	turtle.pendown()
	#図形描写
	for i in range(n):
		turtle.forward(100)
		turtle.left(360/n)

#正三角形
t0 = Turtle()
shape(3, t0, 'pink')

#正方形
t1 = Turtle()
shape(4, t1, 'red')

#正五角形
t2 = Turtle()
shape(5, t2, 'blue')

#正六角形
t3 = Turtle()
shape(6, t3, 'green')

#正七角形
t4 = Turtle()
shape(7, t4, 'orange')

#正八角形
t5 = Turtle()
shape(8, t5, 'purple')
