def on_button_pressed_a():
    music._play_default_background(music.built_in_playable_melody(Melodies.WAWAWAWAA),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    basic.show_string("\"Nathan\"")
    basic.show_icon(IconNames.CONFUSED)
input.on_button_pressed(Button.A, on_button_pressed_a)
