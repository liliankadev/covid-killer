import utime
import machine

# Gpio setup
pum = machine.Pin(16, machine.Pin.OUT)
button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
pot = machine.ADC(0)

MAX_CM = 10


def sensor_read():
    while True:
        cm = get_distance()
        if cm < MAX_CM:
            pum.on()
            utime.sleep_ms(get_flow_time())
        while not button.value():
             pum.on()
        pum.off()
        wait_to_hand_remove()


def get_distance():
    emit_wave()
    return get_wave()


def get_flow_time():
    pot_value = pot.read()
    pot_ms = pot_value * 2 + 400
    return pot_ms


def wait_to_hand_remove():
    while True:
        cm = get_distance()
        utime.sleep_ms(500)
        if cm >= MAX_CM:
            break


def emit_wave():
    trig = machine.Pin(12, machine.Pin.OUT)
    trig.off()
    utime.sleep_us(5)
    trig.on()
    utime.sleep_us(10)
    trig.off()


def get_wave():
    echo = machine.Pin(14, machine.Pin.IN)
    while echo.value() == 0:
        pass
    t1 = utime.ticks_us()
    while echo.value() == 1:
        pass
    t2 = utime.ticks_us()
    cm = (t2 - t1) / 58.0
    return cm


if __name__ == '__main__':
    print('Program started...')
    sensor_read()