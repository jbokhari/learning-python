import turtle

def draw_the_thing():
	window = turtle.Screen()
	window.bgcolor("green")

	janal = turtle.Turtle()
	janal.shape("turtle")
	janal.color("orange")
	n=45
	while n > 0:
		n-=1
		q = 4
		while q > 0:
			q-=1
			janal.forward(100)
			janal.right(90)
		janal.right(8)

	window.exitonclick()


draw_the_thing()