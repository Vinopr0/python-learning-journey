class Square():
    
    def __init__(self, side_length):
        self.side_length = side_length
    
    def get_area(self):
        return self.side_length ** 2
    
    def get_largest_diagonal(self):
        return round(self.side_length * 2**(1/2), 2)

    def get_perimeter(self):
        return self.side_length * 4

class RegularHexagon():

    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return round(self.side_length ** 2 * 3/2 * 3 ** (1/2), 2)
    
    def get_largest_diagonal(self):
        return self.side_length * 2

    def get_perimeter(self):
        return self.side_length * 6

# two different types of polygons, 
# but have methods that do the same thing 
# (but are not necessarily the same)

sqr_1 = Square(3)

hex_1 = RegularHexagon(2)

for polygon in [sqr_1, hex_1]:
    print(f"Area of {str(type(polygon))[17:-2]}: {polygon.get_area()}") # strips the string of the type, excuse the magic numbers
    print(f"Perimeter of {str(type(polygon))[17:-2]}: {polygon.get_perimeter()}") 
    print(f"Largest Diagonal of {str(type(polygon))[17:-2]}: {polygon.get_largest_diagonal()}") 
    print()