
class Points():

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def get_deltas(self):
        delta_x = self.p1[0] - self.p2[0]
        delta_y = self.p1[1] - self.p2[1]
        return [delta_x, delta_y]
    
    def distance(self):
        deltas = self.get_deltas()
        delta_x, delta_y = deltas[0], deltas[1]
        return round((delta_x**2 + delta_y**2) ** (1/2), 2) # pythagoras
    
    def slope(self):
        deltas = self.get_deltas()
        delta_x, delta_y = deltas[0], deltas[1]
        return round(delta_y / delta_x, 2)


points = Points((3, 2), (-2, 3))

print(points.distance())
print(points.slope())