nogpio = False
try:
    import RPi.GPIO as GPIO
except:
    print("no GPIOs found")
    nogpio = True
    
import time
import numpy as np
import random


class player:
    def __init__(my, name, pin, simulate=False, is_kid=True):
        global nogpio
        my.nogpio = nogpio
        
        my.name = name
        my.pin = pin
        my.hits = []
        my.time_dots = [] 
        
        if not nogpio:
            my.setup_gpio()
            
        if simulate or nogpio:
            my.simulate_game(is_kid)

    def __del__(my):
        if not my.nogpio:
            GPIO.cleanup()
    
    # helferfunktion, gib alle zeitpunkte als string zurück
    def timing_str(my):
        return f'{my.name}\t' + str([f'{td:.2f}' for td in my.time_dots]).replace("'","")

    # helferfunktion, gib alle treffer als string zurück 
    def hits_str(my):
        return f'{my.name}\t' + str([f'{h}' for h in my.hits]).replace("'","")

    # helferfunktion, simuliierteachert die Eingabe
    def simulate_game(my, is_kid):
        print("Simulate Game -> generate Inputs")
        my.time_dots = np.arange(0.5, 10.5, 1.0).tolist()
        if is_kid:
            my.time_dots[:] = [td + random.uniform(-0.5, 0.5) for td in my.time_dots]
    
    # Button Press Event handler
    def pin_callback(my, ch):
        #print(f'{my.name}: Button pressed! gpio_ch:{ch}')
        my.time_dots.append(time.monotonic())
    
    def enable_input(my):
        if my.nogpio:
            return
        
        GPIO.add_event_detect(
            my.pin, 
            GPIO.FALLING, 
            callback=my.pin_callback, 
            bouncetime=250)
        
    def disable_input(my):
        if my.nogpio:
            return
        
        GPIO.remove_event_detect(my.pin)
        
    # Setup GPIO Pin with Event handl
    def setup_gpio(my):
        if my.nogpio:
            return
        
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(     my.pin, 
                        GPIO.IN, 
                        pull_up_down=GPIO.PUD_UP)

        my.enable_input()

        