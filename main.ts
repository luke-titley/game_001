input.onButtonPressed(Button.A, function () {
    GUN = 4
})
let BAL = 0
let GUN = 0
let points = 0
GUN = 5
if (points == 10) {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Prelude), music.PlaybackMode.InBackground)
    radio.sendNumber(0)
    points = 0
}
loops.everyInterval(500, function () {
    led.plot(BAL, 0)
    led.unplot(BAL - 1, 0)
    if (BAL == 5) {
        BAL = 0
    } else {
        BAL += 1
    }
})
basic.forever(function () {
    if (GUN == 0 && BAL == 3) {
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.BaDing), music.PlaybackMode.UntilDone)
        points += 1
    }
})
loops.everyInterval(200, function () {
    led.plot(2, GUN)
    led.unplot(2, GUN + 1)
    if (GUN < 5) {
        GUN += -1
    }
})
