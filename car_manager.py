from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(f"{random.choice(COLORS)}")
            new_car.shapesize(1, 2)
            start_x = random.choice([300, -300])
            start_y = random.randrange(-250, 251, 50)

            # Assign direction as an attribute of the car itself
            if start_x == 300:
                new_car.direction = "backward"
            elif start_x == -300:
                new_car.direction = "forward"

            new_car.goto(start_x, start_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            # Check direction of each individual car
            #before this I used self.direction it makes the cars moving back and forward constantly,
            #The issue is that in your create_cars method, you're assigning self.direction to the CarManager object itself. This means that all cars share the same direction, which results in the problem where the direction is not updated per car instance.
            #To fix this, you need to assign the direction attribute to each individual
            # car (i.e., each Turtle object), not to the entire CarManager. Here's how you can fix the code:
            if car.direction == "backward":
                car.backward(self.car_speed)
            elif car.direction == "forward":
                car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT