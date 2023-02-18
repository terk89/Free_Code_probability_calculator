"""
For this project, you will write a program to determine
the approximate probability of drawing certain balls randomly from a hat.
"""
import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for key, value in balls.items():
            for i in range(value):
                self.contents.append(key)
"""
The Hat class should have a draw method that accepts an argument 
indicating the number of balls to draw from the hat. This method 
should remove balls at random from contents and return those balls 
as a list of strings. The balls should not go back into the hat 
during the draw, similar to an urn experiment without replacement. 
If the number of balls to draw exceeds the available quantity, return all the balls.
"""
    def draw(self, nr_balls):
        draw_balls = []
        if nr_balls >= len(self.contents):
            return self.contents
        else:
            counter = 0
            while counter < nr_balls:
                index = random.randint(0, len(self.contents)-1)
                draw_balls.append(self.contents[index])
                del self.contents[index]
                counter += 1
        return draw_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_draws = 0
    counter = 0
    while num_experiments > counter:
        temp_hat = copy.deepcopy(hat)
        success = True
        drawn_balls = temp_hat.draw(num_balls_drawn)
        for key, value in expected_balls.items():
            if key in drawn_balls:
                if value <= drawn_balls.count(key):
                    continue
                else:
                    success = False
            else:
                success = False
        if success:
            successful_draws += 1
            counter += 1
        else:
            counter += 1
    return successful_draws/num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)