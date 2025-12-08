# Jaiden Blanchard
# CS 499 Capstone with Professor Sherri Maciosek
# started 11 / 10 / 2025, first submission 11 / 15 / 2025, polished 12 / 8 / 2025

class PaintNeeded:

    # it takes approximately 1 gallon of paint to cover around 350 square feet
    square_ft_per_gallon = 350

    def __init__(self, wall_height, wall_width, coat_count):
        self.wall_height = wall_height
        self.wall_width = wall_width
        self.coat_count = coat_count

    # calculation for wall area
    def wall_area(self):
        return self.wall_height * self.wall_width

    # calculation for ceiling area
    @classmethod
    def ceiling(cls, ceiling_length, ceiling_width, coat_count):
        ceiling_area = ceiling_length * ceiling_width
        return cls(1, ceiling_area, coat_count)

    # calculation for window area
    @classmethod
    def window(cls, window_height, window_width):
        window_area = window_height * window_width
        return cls(1, window_area, 0)

    # calculation for door area
    @classmethod
    def door(cls, door_height, door_width):
        door_area = door_height * door_width
        return cls(1, door_area, 0)

    # final calculation for gallons needed to paint the wall
    def gallons_paint(self):
        return (self.wall_area() * self.coat_count) / PaintNeeded.square_ft_per_gallon