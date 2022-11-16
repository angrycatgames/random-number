def on_button_pressed_a():
    basic.show_number(randint(0, 100))
input.on_button_pressed(Button.A, on_button_pressed_a)
