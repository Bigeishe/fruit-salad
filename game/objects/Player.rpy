init python:
    class Player:
        def __init__(self, name):
            self.name = name
                      
        def __repr__(self):
            return self.name
    
        def sayer(self):
            return renpy.character.Character(self.name)