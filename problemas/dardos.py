class Target():
    shot: str = ""
    split_values = []
    x = y = None

    def __init__(self, shot: str):
        self.shot = shot.strip()
        self.get_axis()

    def get_axis(self):
        self.split_values = self.shot.split()
        self.x = int(self.split_values[0])
        self.y = int(self.split_values[1])
    
    def result(self):
        if self.x == 0 or self.y == 0:
            print("NO ALVO!", end='')
        elif self.x > 0 and self.y > 0:
            print("R1", end='')
        elif self.x < 0 and self.y > 0:
            print("R2", end='')
        elif self.x < 0 and self.y < 0:
            print("R3", end='')
        elif self.x > 0 and self.y < 0:
            print("R4", end='')

test = Target(input())
test.result()