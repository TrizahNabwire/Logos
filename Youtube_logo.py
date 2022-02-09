from turtle import *
fillcolor('red')
begin_fill()
for i in  [300, 200, 300, 200]:
    forward(i)
    circle(10,90)
# forward(300)#draws a horizontal line 
# circle(10, 90)#makes a small turn like a border radius
# forward(200)#straight line upwards
# circle(10, 90) #makes a u turn towards your left
end_fill()

up()
goto(120, 65)
down()
fillcolor('white')
begin_fill()
for i in [30, 120, 120]:
    left(i)
    forward(100)
end_fill()