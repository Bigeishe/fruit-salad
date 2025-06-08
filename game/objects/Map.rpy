init python:
    class Map:
        def __init__(self):
            places = [
                Place("Appartment", (.5, .8), time_skip=False),
                Place("Park", (.5, .2)),
                Place("Beach", (.5, .5))      
            ]

            self.places = {}
            for p in places:
                self.add_place(p)

            self.current_place = None

        def get_places(self):
            return self.places.values()

        def add_place(self, place):
            self.places[place.name] = place

        def set(self, name):
            self.current_place = self.places[name]
        
        def is_somewhere(self):
            return self.current_place != None
