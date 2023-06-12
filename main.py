def on_button_pressed_a():
    global branco
    branco = pins.analog_read_pin(AnalogPin.P1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global média
    média = (branco + preto) / 2
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global preto
    preto = pins.analog_read_pin(AnalogPin.P1)
input.on_button_pressed(Button.B, on_button_pressed_b)

preto = 0
média = 0
branco = 0
for index in range(4):
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_icon(IconNames.SMALL_SQUARE)
    basic.show_icon(IconNames.SQUARE)

def on_forever():
    if pins.analog_read_pin(AnalogPin.P2) > 800:
        robotbit.motor_stop_all()
        basic.show_icon(IconNames.NO)
        basic.pause(100)
        basic.clear_screen()
    else:
        if pins.analog_read_pin(AnalogPin.P1) > média:
            robotbit.motor_run_dual(robotbit.Motors.M1B, 0, robotbit.Motors.M2A, 150)
        else:
            robotbit.motor_run_dual(robotbit.Motors.M1B, 150, robotbit.Motors.M2A, 0)
basic.forever(on_forever)

def on_forever2():
    serial.write_value("x", pins.analog_read_pin(AnalogPin.P1))
    serial.write_value("y", pins.analog_read_pin(AnalogPin.P2))
    basic.pause(500)
basic.forever(on_forever2)
