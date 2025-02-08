class StringManipulator: 
    def __init__(self):
        self.s = "" 

    def getString(self):
        self.s = input("Мәтінді енгізіңіз: ")  

    def printString(self):
        print(self.s.upper())  

name = StringManipulator()
name.getString()   # getString() әдісін шақыру
name.printString() # printString() әдісін шақыру