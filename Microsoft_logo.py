from turtle import *
colors = ['#f5480f', '#2aad21', '#288cf7','#ffcc00']
for col,pos in zip(colors, [(0,0),(1,0),(0,-1),(1,-1)]):
    up()
    goto(pos[0]*100,pos[1]*100)
    down()
    fillcolor(col)
    begin_fill()
    for k in range(4):
        forward(90)
        right(90)
    end_fill()
end()