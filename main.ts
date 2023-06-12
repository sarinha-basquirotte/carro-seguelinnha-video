input.onButtonPressed(Button.A, function () {
    branco = pins.analogReadPin(AnalogPin.P1)
})
input.onButtonPressed(Button.AB, function () {
    média = (branco + preto) / 2
})
input.onButtonPressed(Button.B, function () {
    preto = pins.analogReadPin(AnalogPin.P1)
})
let preto = 0
let média = 0
let branco = 0
for (let index = 0; index < 4; index++) {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.showIcon(IconNames.SmallSquare)
    basic.showIcon(IconNames.Square)
}
basic.forever(function () {
    if (pins.analogReadPin(AnalogPin.P2) > 800) {
        robotbit.MotorStopAll()
        basic.showIcon(IconNames.No)
        basic.pause(100)
        basic.clearScreen()
    } else {
        if (pins.analogReadPin(AnalogPin.P1) > média) {
            robotbit.MotorRunDual(
            robotbit.Motors.M1B,
            0,
            robotbit.Motors.M2A,
            150
            )
        } else {
            robotbit.MotorRunDual(
            robotbit.Motors.M1B,
            150,
            robotbit.Motors.M2A,
            0
            )
        }
    }
})
basic.forever(function () {
    serial.writeValue("x", pins.analogReadPin(AnalogPin.P1))
    serial.writeValue("y", pins.analogReadPin(AnalogPin.P2))
    basic.pause(500)
})
