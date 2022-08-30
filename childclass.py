class students:
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def fullname(self):
        return f'FirstName: {self.fname}\nLastName: {self.lname}\nAge: {self.age}\nRank: {self.rank}'
    
class teachers(students):
    def __init__(self, fname, lname, age, rank):
        super().__init__(fname, lname)
        self.age = age
        self.rank = rank
        
T1 = teachers('Sonny', 'John', 37, 12)

print(T1.fullname())