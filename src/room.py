# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self,name,description):
        self.name=name
        self.description=description
    def __str__(self):
        print(f"You Enter a Room! It is called... \n ---------------------------------------------\n  {self.name} \n ================= \n Room Description \n _________________________\n {self.description} \n")



# test = Room("Iowa State","Full of Silly Lads tbh get out of there and go to lambda")

# print(test)