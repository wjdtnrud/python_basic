# import turtle
from turtle import *
#import turtle as t

def draw_circle(x,y,col,r):
    penup()
    goto(x,y)
    pendown()
    color(col)
    begin_fill()
    circle(r)
    end_fill()
    

setup(500,500)
title('크리스마스카드')
bgcolor("pink")

speed(0) #최고속도 0, 느림1~, 빠름10
st()
shape("turtle")
color("black")
penup()
goto(-200,200)
pendown()

#테두리그리기
forward(400)
right(90) #외각
forward(400)
right(90)
forward(400)
right(90)
forward(400)
right(90) 


#얼굴그리기
penup()
goto(0,-70)
pendown()
begin_fill()
color("ivory")
circle(50)
end_fill()

#모자그리기
penup()
goto(50,0)
pendown()
color("blue")
begin_fill()
left(360/3)
forward(100)
left(360/3)
forward(100)
left(360/3)
forward(100)
end_fill()

#모자꼭지그리기
draw_circle(-50,-5,"red",7)
draw_circle(-30,-5,"gray",7)
draw_circle(-10,-5,"red",7)
draw_circle(10,-5,"gray",7)
draw_circle(30,-5,"red",7)
draw_circle(50,-5,"gray",7)


#글자쓰기
penup()
goto(0,-150)
color("black")
write("메리추석")
ht() #hideturtle()
      
done() #mainloop()
