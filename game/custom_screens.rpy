screen map():
    add "map_img"
    use hud()

    for place in world_map.get_places():
        button:
            style "map_but"
            text place.name style "map_text"
            action [Hide("map", transition=dissolve), SetVariable("world_map.current_place", place), Call("location")]
            align place.alignment

screen hud():
    use clock()
    use phone()
    if world_map.is_somewhere():
        use location_name(world_map.current_place)

screen location_name(name):
    zorder 100
    frame:
        xfill False
        yfill False
        padding (10, 10, 10, 10) 
        background Solid("#424242")
        align (.2, .05)
        vbox:
            align (0.5, 0.5)
            text "[name]"

screen return_screen:
    button:
        text "Return" style "return_text"
        action [SetVariable("world_map.current_place", None), Return()]
        style "return_but"

screen debug(stalking):
    text "[stalking]":
        align (.5, .05)

screen character_select(info=False, excluded=[]):
    modal True
    zorder 200
    $ characters = list(set(char_buffer.buffer) - set(excluded))
    $ rows = (len(characters) // 4)
    if rows == 0:
        $ rows += 1

    if info:
        add Solid("#be0085")

    vbox:
        align (0.5, 0.5)
        if info:         
            textbutton "Return" action Hide("character_select", transition=dissolve)
        viewport:
            mousewheel True
            if rows != 1:
                scrollbars "vertical"
            align (0.5, 0.5)
            xysize(1000, 100)
            grid 4 rows:
                spacing 10
                align (0.0, 0.0)
                for chara in characters:
                    button:
                        background Solid("#000000")
                        hover_background Solid("#5e5e5e")
                        align (0.5, 0.5)
                        padding (10, 10, 10, 10)
                        xysize (200, 100)
                        if info == True:
                            action Show("character_sheet", chara=chara, transition=dissolve)
                        else:
                            action Return(chara)
                        text chara.name:
                            align (0.5, 0.5)

screen character_sheet(chara):
    modal True
    add Solid("#be0085")
    zorder 300
    frame:
        align (0.5, 0.5)
        background Solid("#505050")
        vbox:
            align (0.5, 0.5)
            text chara.name
            text "Affection: [chara.affection]"
            text "Aggro: [chara.aggro]"
            text "Together: [chara.together]"
            text "Seen: [chara.seen]"
            for name in chara.jalousy:
                $ value = chara.jalousy[name]
                text "[name] - Jalousy [value]"
            textbutton "Return" action Hide("character_sheet", transition=dissolve)
        
screen phone():
    textbutton _("Phone") action Show("character_select", info=True, transition=dissolve) align(.95, .05)

screen clock():
    zorder 100
    frame:
        xfill False
        yfill False
        padding (10, 10, 10, 10) 
        background Solid("#424242")
        align (.05, .05)
        vbox:
            align (0.5, 0.5)
            text "Day [global_time.get_day()]"
            text "[global_time.get_slot()]"
