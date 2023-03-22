import time, vlla, random

directions = ['L', 'R', 'U', 'D']
green = vlla.Color(g=0x7f)
red = vlla.Color(r=0x7f)

def randomCoord():
    x = random.randrange(0, vlla.WIDTH)
    y = random.randrange(0, vlla.HEIGHT)
    return (x, y)

class Board:
    def __init__(self):
        self.snake = [randomCoord()]
        self.direction = directions[random.randrange(0, 4)]
        self.food = self.genFood()

    def genFood(self):
        food = randomCoord()

        while food in self.snake:
            food = randomCoord()

        return food

    def advance(self):
        x, y = self.nextHead()
        ate = True

        if self.snake[0] != self.food:
            del self.snake[-1]
            ate = False

        if (x, y) in self.snake:
            return False

        if ate:
            self.food = self.genFood()

        self.snake = [(x, y)] + self.snake
        return True

    def nextHead(self, direction=None):
        direction = direction if direction else self.direction
        x, y = self.snake[0]

        if self.direction == 'L':
            x = (x - 1) % vlla.WIDTH
        elif self.direction == 'R':
            x = (x + 1) % vlla.WIDTH
        elif self.direction == 'U':
            y = (y - 1) % vlla.HEIGHT
        else:
            y = (y + 1) % vlla.HEIGHT

        return x, y

    def wouldDie(self, direction):
        return self.nextHead(direction) in self.snake

    def deathSequence(self, canvas):
        while self.snake:
            del self.snake[-1]
            canvas.clear()
            self.drawCanvas(canvas)
            time.sleep(0.1)

    def drawCanvas(self, canvas):
        for col, row in self.snake:
            canvas.set_pixel(row, col, green)

        col, row = self.food
        canvas.set_pixel(row, col, red)
        canvas.flush()

def run(canvas, until=None):
    board = Board()
    canvas.clear()
    board.drawCanvas(canvas)

    while board.advance():
        if until and time.time() > until:
            return

        hx, hy = board.snake[0]
        fx, fy = board.food
        orig = board.direction
        new = orig

        if hx == fx and board.direction in ['L', 'R']:
            board.direction = 'U' if fy < hy else 'D'
        elif hy == fy and board.direction in ['U', 'D']:
            board.direction = 'L' if fx < hx else 'R'

        if board.nextHead() in board.snake:
            if new != orig and not snake.wouldDie(orig):
                board.direction = orig
            elif orig == 'L' or orig == 'R':
                board.direction = 'U' if not board.wouldDie('U') else 'D'
            elif orig == 'U' or orig == 'D':
                board.direction = 'L' if not board.wouldDie('L') else 'R'

        time.sleep(0.1)
        canvas.clear()
        board.drawCanvas(canvas)

    board.deathSequence(canvas)
    time.sleep(0.5)

def loop(c, until=None):
    while True:
        if until and time.time() > until:
            return

        run(c, until)

if __name__ == '__main__':
    loop(vlla.Canvas())
