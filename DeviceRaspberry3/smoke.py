import time, sys
import RPi.GPIO as GPIO

class smoke:
       
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

                def smokedetect(pin):
                        print('Smoke detected')
                        return 

                GPIO.add_event_detect(35, GPIO.RISING)
                GPIO.add_event_callback(35, smokedetect)


                        
                try:
                    while True:
                        print('No Smoke')
                        time.sleep(0.5)
                except KeyboardInterrupt:
                    GPIO.cleanup()
                    sys.exit()



        
