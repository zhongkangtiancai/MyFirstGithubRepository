class Cat:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name} sit")

    def roll_over(self):
        print(f"{self.name} rolling")

    def happy(self,food):
        print(f"give {food},i am happy!")
