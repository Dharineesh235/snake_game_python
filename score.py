from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 255)
        self.score = 0
        self.color('white')
        self.write(f'Score : {self.score}', False, 'center', ('Arial', 20, 'normal'))
        self.hideturtle()

    # game over method that runs when snake hits the wall or its body
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, 'center', ('Arial', 26, 'normal'))

    # method to continuously updates our scor̥e board
    def score_board(self):
        self.score += 1
        self.clear()
        self.write(f'Score : {self.score}', False, 'center', ('Arial', 20, 'normal'))
        # self.update_score_board()
