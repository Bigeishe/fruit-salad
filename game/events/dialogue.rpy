label dialogue(event, sayer):
    show screen debug(event.stalkers)
    sayer "Hello!"
    menu:
        "+ Affection":
            $ event.adjust_attr("affection", 20)
        "- Affection":
            $ event.adjust_attr("affection", -20)

        "Select other character":
            $ selected =  event.select_character()
            menu:
                "Talk trash about [selected] (-20 Jalousy)":
                    $ event.adjust_jalousy(selected, -20)
                "Talk nicely about [selected] (+20 Jalousy)":
                    $ event.adjust_jalousy(selected, 20)
        "No thanks":
            pass
    sayer "Bye!"
    hide screen debug
    return