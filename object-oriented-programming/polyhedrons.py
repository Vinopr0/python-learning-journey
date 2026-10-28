class Cylinder():
    # class object attribute
    pi = 3.14

    # instance
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_volume(self):
        return self.pi * self.radius ** 2 * self.height

    def get_area_circle(self):
        return self.pi * self.radius ** 2
     
    def get_perimeter_of_circle(self):
        return round(2 * self.pi * self.radius, 2)

    def get_surface_area(self):
        side_area = 2 * self.pi * self.radius * self.height
        top_bottom_area = 2 * self.pi * self.radius ** 2
        return round(side_area + top_bottom_area, 2)
    
    def percentage_of_volume_from_height(self, partial_height):
        total_volume = self.get_volume() # no need to pass self again inside this!
        partial_volume = total_volume / self.height * partial_height
        # I know this is stupid, but I want it to be clearer at least for myself . . . 
        return round(partial_volume / total_volume, 2)

cyl_1 = Cylinder(radius=5.0, height=3.0)

print(cyl_1.get_perimeter_of_circle())
print(cyl_1.get_volume())
print(cyl_1.get_area_circle())
print(cyl_1.percentage_of_volume_from_height(2.0))
print(cyl_1.get_surface_area())