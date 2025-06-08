label start:
    $ quick_menu = False
    $ char_buffer.fill(3)
    jump map_label

label time_label:
    hide screen hud
    scene black with dissolve
    $ global_time.next_slot()
    centered "[global_time.get_slot()]"
    return

label map_label:
    call screen map with dissolve
    return

label location:
    $ place = world_map.current_place
    show screen hud
    scene expression place.image with dissolve

    #if renpy.random.random() > 0.5:
    $ event = Event(char_buffer)
    $ event.trigger()
    if game_over:
        jump game_over

    call screen return_screen with dissolve
    if global_time.end_of_day():
        jump end_of_day
    if place.time_skip:
        call time_label
    jump map_label

label end_of_day:
    hide screen hud with dissolve
    scene black with dissolve

    "Another day is about to start..."
    $ char_buffer.add_character()

    call time_label
    $ world_map.set("Appartment")
    show screen hud with dissolve
    jump location
    
label game_over:
    "Game over"
    return

