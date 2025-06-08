init python:
    class FemaleChar:
        def __init__(self, name):
            self.name = name
            self.together = False
            self.seen = False
            
            self.affection = 0
            self.aggro = 0

            # Dictionnaire: nom_du_perso:chiffre_de_0_a_100
            self.jalousy = {}

        def madness(self):
            jalousy_sum = 0
            for gal in self.jalousy:
                jalousy_sum += self.jalousy[gal]
            return self.aggro + jalousy_sum

        def init_jalousy(self, name):
            self.jalousy[name] = 0

        def get_jalousy(self, name):
            return self.jalousy[name]

        def adjust_jalousy(self, name, value):
            if name not in self.jalousy:
                self.init_jalousy(name)
            self.jalousy[name] += value
            
        def adjust_attr(self, var, amount):
            if not hasattr(self, var):
                raise Exception("This is not a valid attribute for a female character, Honey~")
            setattr(self, var, getattr(self, var) + amount)
            
        def __repr__(self):
            return self.name
    
        def sayer(self):
            return renpy.character.Character(self.name)

