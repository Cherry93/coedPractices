import turtle

turtle.showturtle()
turtle.pensize(5)

turtle.color("red")
turtle.penup()
turtle.goto(-110,0)
turtle.pendown()
turtle.circle(45)

turtle.color("green")
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.circle(45)

turtle.color("blue")
turtle.penup()
turtle.goto(110,0)
turtle.pendown()
turtle.circle(45)

turtle.color("yellow")
turtle.penup()
turtle.goto(-55,-45)
turtle.pendown()
turtle.circle(45)

turtle.color("black")
turtle.penup()
turtle.goto(55,-45)
turtle.pendown()
turtle.circle(45)

turtle.penup()
turtle.goto(0,-100)
turtle.write("乌龟：健身操已完成！",align="center",font=("楷体", 20, "italic"))

turtle.done()
turtle.config_dict()