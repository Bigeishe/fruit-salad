init python:
    class Event:
        def __init__(self, buffr):
            self.speaker = buffr.select_character()
            self.stalkers = buffr.select_stalkers(excluded=[self.speaker])
            self.selected = None
            
        def adjust_attr(self, attr, amount):
            self.speaker.adjust_attr(attr, amount)
            renpy.say(None, f"-SPEAKER- {self.speaker.name}: added {amount} to {attr}")
            self.update_stalkers_attr(attr, -amount)
            
        def adjust_jalousy(self, character, amount):
            self.speaker.adjust_jalousy(character.name, amount) 
            renpy.say(None, f"-SPEAKER- {self.speaker.name} is {amount} more jalous of {character.name}")
            self.update_stalkers_jalousy(-amount)
            
        def update_stalkers_attr(self, attr, amount):
            for gal in self.stalkers:     
                gal.adjust_attr(attr, amount)
                renpy.say(None, f"-STALKER- Added {amount} to {attr} for {gal.name}")
            
        def update_stalkers_jalousy(self, amount):
            for gal in self.stalkers:     
                gal.adjust_jalousy(self.speaker.name, amount)
                renpy.say(None, f"-STALKER- {gal.name} is {amount} more jalous of {self.speaker.name}")    
        
        def get_speaker_sayer(self):
            return self.speaker.sayer()

        def select_character(self):
            selected = renpy.call_screen("character_select", excluded=[self.speaker])
            renpy.say(None, f"{selected} selected") 
            return selected

        def trigger(self):
            if self.speaker.madness() >= 100:
                renpy.call("death", event=self, sayer=self.get_speaker_sayer())
            else:
                renpy.call("dialogue", event=self, sayer=self.get_speaker_sayer())
            
        