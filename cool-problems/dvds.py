
class Library: # library class
    def __init__(self, members, dvds):
        self.dvds = dvds # stores the dvds 
        self.members = members # stores members
        self.is_borrowed = {dvd: False for dvd in dvds} # makes a list that says if the dvd is borrowed or not
        self.borrowed_dvds = {member: [] for member in members} # makes a list for every member that includes the dvds that they have borrowed.

    def borrow(self, member, dvd): 
        if member in self.members and dvd in self.dvds and not self.is_borrowed[dvd]: # blocks if the variables are not on the list, or if the dvd is borrowed.
            self.borrowed_dvds[member].append(dvd) # adds the dvd being borrowed to the borrowed_dvds dict, associated with the member
            self.is_borrowed[dvd] = True # changes the value that asks if the dvd is being borrowed to True.
        pass

    def return_dvd(self, member, dvd): # the same as above, but asks if the dvd is currently being borrowed at all.
        if member in self.members and dvd in self.dvds and dvd in self.borrowed_dvds[member]:
            self.borrowed_dvds[member].remove(dvd)
            self.is_borrowed[dvd] = False
        pass

    def return_all(self, member):
        if member in self.members:
            for dvd in self.borrowed_dvds[member]:
                self.is_borrowed[dvd] = False
            self.borrowed_dvds[member] = []
        pass

    def add_member(self, *new_members):
        for new_member in new_members:
            if isinstance(new_member, str) == True:
                self.members.append(new_member)
                self.borrowed_dvds[new_member] = []        
        pass

    def add_dvd(self, *new_dvds):
        for new_dvd in new_dvds:
            if isinstance(new_dvd, str) == True:
                self.dvds.append(new_dvd)
                self.is_borrowed[new_dvd] = False
        pass
    

    
        



dvds = [
    "Forrest Gump", "The Shawshank Redemption", "Get Out", 
    "Rio", "Toy Story", "Finding Nemo", "The Smurfs",
    "Spider-Man: Brand New Day", "The Godfather", "Fight Club"
]

members = [
    "Mary", "Winston", "Brad", "Jonathan", 
    "Ella", "Edward", "Jules", "Peter"
]

lib = Library(members, dvds)

lib.add_dvd("Scream", "Percy Jackson", "The Wizard of Oz")

lib.borrow("Mary", lib.dvds[-1])

print("\n" + str(lib.borrowed_dvds) + f"\n \n" + str(lib.dvds))