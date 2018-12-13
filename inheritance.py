class Parent ():
    def __init__(self, last_name, eye_color) :
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self) :
        print("Last Name "+self.last_name)
        print("Eye color "+self.eye_color)

class Child(Parent) :
    def __init__(self,last_name,eye_color,number_of_toys) :
        print("Child Constructor Called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys=number_of_toys
        
    def show_info(self) :
        print("Last Name "+self.last_name)
        print("Eye color "+self.eye_color)
        print("Number of Toys"+str(self.number_of_toys)
        
#suchitra_sundar = Parent("Sundar","black")
#suchitra_sundar.show_info()
#print(suchitra_sundar.last_name)

supriya_sundar = Child("Sundar","black",5)
supriya_sundar.show_info()
#print(supriya_sundar.eye_color)
#print(supriya_sundar.last_name)
#print(supriya_sundar.number_of_toys)
