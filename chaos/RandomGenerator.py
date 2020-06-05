from random import randint

def randomGenerator():
    return( randint(0,10) for i in range(10)).__next__()

def yeilder():
    yield 123

print(randomGenerator())
print(yeilder().__next__())