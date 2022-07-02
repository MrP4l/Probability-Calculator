import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items(): # input ex key -> Red, value -> 2
            self.contents += v * [k] # write n times keys
        print(self.contents)

    def draw(self, num):
        if num >= len(self.contents):
            return self.contents
        selection = []
        for n in range(num):
            choice = random.choice(self.contents)
            selection.append(choice)
            self.contents.remove(choice)
        return selection

def contains_balls(expected_balls, actual_balls):
        for b in expected_balls:
            if b in actual_balls:
                actual_balls.remove(b)
            else:
                return False
        return True
  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)

        eb_list = []
        for k, v in expected_balls.items():
            eb_list += v * [k]

        if contains_balls(eb_list, balls):
            M += 1

    probability = M / num_experiments
    return probability



