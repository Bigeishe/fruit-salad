init python:
    import random

    class CharacterBuffer():
        def __init__(self):
            self.factory = CharacterFactory() 
            self.buffer = []

        def select_character(self):
            index = renpy.random.randint(0, len(self.buffer) - 1)
            return self.buffer[index]

        def add_character(self, character):
            self.buffer.append(character)
            renpy.say(None, f"Added {character.name} to buffer")

        def select_stalkers(self, excluded):
            stalkers = []
            charas = list(set(self.buffer) - set(excluded))
            for chara in charas:
                if random.random() > 0.5:
                    stalkers.append(chara)
            return stalkers  
    
        def fill(self, number_of_chars):
            for i in range(number_of_chars):
                char = self.factory.make_girl()
                self.add_character(char)