from turtle import Turtle


class score_board(Turtle):

    def __init__(self):

        super().__init__()

        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.write(f"Score:  {self.score}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()


    def game_over(self):
        self.hideturtle()
        self.goto(0,0)
        self.color("white")
        self.penup()
        self.write("Game Over.",align="center",font=("Arial",16,"normal"))


    def increase(self):

        self.score+=1
        self.clear()

        self.write(f"Score:  {self.score}",align="center",font=("Arial",24,"normal"))

