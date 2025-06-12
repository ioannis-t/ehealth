from microbit import *
import neopixel

# Initialize components
np = neopixel.NeoPixel(pin0, 4)
servo_pin = pin8

def move_forward():
    # move forward
    display.show(Image.ARROW_N)

def move_backward():
    # move backward
    display.show(Image.ARROW_S)

def turn_left():
    # turn left
    display.show(Image.ARROW_W)

def turn_right():
    # turn right
    display.show(Image.ARROW_E)

def stop():
    # stop movement
    display.clear()

def take_temperature():
    # Simulate temperature reading
    temp = temperature()  # dummy
    display.scroll("T:{}".format(temp))
    return temp

def measure_heart_rate():
    # Dummy function for pulse
    hr = 72  # placeholder
    display.scroll("HR:{}".format(hr))
    return hr

def give_pill():
    servo_pin.write_analog(95)  # simulate servo giving pill
    sleep(2000)
    servo_pin.write_analog(180)

def disinfect():
    pin13.write_digital(1)
    pin15.write_digital(1)
    sleep(2000)
    pin13.write_digital(0)
    pin15.write_digital(0)
    sleep(1000)

def sos_alert():
    sleep(200)
    display.scroll("SOS")

# Main routine
def main():
    servo_pin.write_analog(180)
    stop()
    display.scroll("Init comm on ch 7")

    sleep(5000)
    display.scroll("Go to patient")
    sleep(3000)

    temp = take_temperature()
    sleep(6000)

    hr = measure_heart_rate()
    sleep(3000)

    give_pill()
    sleep(1000)

    disinfect()

    display.scroll("Go to next")
    sleep(2000)
    take_temperature()

    sleep(5000)
    sos_alert()

main()