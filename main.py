def on_button_pressed_a():
    global GUN
    GUN = 4
input.on_button_pressed(Button.A, on_button_pressed_a)

BAL = 0
GUN = 0
points = 0
GUN = 5
if points == 10:
    music._play_default_background(music.built_in_playable_melody(Melodies.PRELUDE),
        music.PlaybackMode.IN_BACKGROUND)
    radio.send_number(0)
    points = 0

def on_every_interval():
    global BAL
    led.plot(BAL, 0)
    led.unplot(BAL - 1, 0)
    if BAL == 5:
        BAL = 0
    else:
        BAL += 1
loops.every_interval(500, on_every_interval)

def on_forever():
    global points
    if GUN == 0 and BAL == 3:
        music._play_default_background(music.built_in_playable_melody(Melodies.BA_DING),
            music.PlaybackMode.UNTIL_DONE)
        points += 1
basic.forever(on_forever)

def on_every_interval2():
    global GUN
    led.plot(2, GUN)
    led.unplot(2, GUN + 1)
    if GUN < 5:
        GUN += -1
loops.every_interval(200, on_every_interval2)
