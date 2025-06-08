init python:
    import random

    class CharacterFactory:
        def __init__(self):
            self.girl_names = self.read_girl_names()

        def read_girl_names(self):
            with open(renpy.loader.transfn("girl_names.txt"), 'r', encoding='utf-8') as file:
                names = file.read().splitlines()
            return names

        def make_girl_name(self):
            name_index = random.randint(0, len(self.girl_names))
            return self.girl_names[name_index]

        def make_girl(self):
            return FemaleChar(self.make_girl_name())