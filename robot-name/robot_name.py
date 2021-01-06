import random, string

class Robot:
    def __init__(self):
        self.getRandomName()

    def reset(self):
        random.seed(random.randrange(10))
        self.getRandomName()

    def getUppercase(self):
        return random.choice(string.ascii_uppercase)

    def getDigit(self):
        return str(random.randrange(0, 10))

    def getRandomName(self):
        self.name = ''.join(
            self.getUppercase() for _ in range(2)
            ) + ''.join(self.getDigit() for _ in range(3))