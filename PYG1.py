#part 1
'''
def greet():
    print("Hello to you")
    print("My Name is JARVIS")
    print("May I know your name: ")
    userName = input()


#How to call the function
greet()
'''

#How to make a class

class Student():
    #properties/ attributes
    name = ""
    age = 12
    schoolclass = "6th A"
    house = "Sapphire"
    classteacher = "Poonam Ma'am"

    #constructor
    def __init__(self):
        print("Making a new student")

    #Another Function
    def change_details(self):
        print("Please enter your age: ")
        self.age = int(input())
        print ("Please enter the name of the student")
        self.name = input()

    #Another Function
    def show_Details(self):
        print("The details of student are:")
        print(self.name)
        print(self.age)
        print(self.schoolclass)
        print(self.house)
        print(self.classteacher)
    
#Student class definition  is over
#Making 2 objects/ instances of Student class
Varnika = Student()
Surabhi = Student()


#part 2
#import and initialize pygame 
import pygame
pygame.init()

#set dimensions of the screen
screen= pygame.display.set_mode((600,600))

#Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
#screen fil
screen.fill(white)
pygame.display.update()

#creating a Rectangle class
class Rect():
    def __init__(self,color,dimensions):
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dimensions=dimensions

    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)

#creating Instances    

greenRect=Rect(green,(50,20,100,100))
redRect=Rect(red,(150,200,150,150))
blueRect=Rect(blue,(300,400,200,200))
#accessing methods 
greenRect.draw()
blueRect.draw()
redRect.draw()
#Display update to reflect the things on screeen
pygame.display.update()


