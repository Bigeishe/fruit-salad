init python:
    class Time:
        def __init__(self):
            self.day = 1
            self.slot = 0
            self.slots = ["Noon", "Morning", "Afternoon", "Evening", "Night"]
            
        def next_slot(self):
            if self.end_of_day():
                self.day += 1
            self.slot = (self.slot + 1) % 5

        def get_slot(self):
            return self.slots[self.slot]
            #return str(self.slot)

        def get_day(self):
            return str(self.day)

        def __repr__(self):
            return self.get_slot() + "of day " + self.get_day()

        def end_of_day(self):
            return self.slot == 4
