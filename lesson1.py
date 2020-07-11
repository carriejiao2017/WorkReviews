# import turtle
# fred = turtle.Turtle()
# fred.color("green")
# fred.forward(135)
# fred.right(135)
# fred.forward(140)
# fred.right(135)
# fred.forward(100)

import turtle
turtle.bgcolor('black') # 改变画布背景颜色为黑色
george = turtle.Turtle()
george.color("yellow")
for side in [1, 2, 3, 4]:
    george.forward(100)
    george.right(90)