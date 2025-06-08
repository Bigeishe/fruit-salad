init python:
    class Place:
        def __init__(self, name, alignment, time_skip=True):
            self.name = name
            self.image = name.lower().replace(" ", "_")
            self.alignment = alignment
            self.time_skip = time_skip

        def __repr__(self):
            return self.name
