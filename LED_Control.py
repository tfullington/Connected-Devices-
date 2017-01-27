import time
import pigpio
pi1 = pigpio.pi()

while True:
    #Initializes all LED's to off
    pi1.write(19,0)
    pi1.write(26,0)
    pi1.write(13,0)
    
    time.sleep(1)
    
    #Ramps brightness from 0 to 200 and back over 1 second + time to execute
    brightness = 0
    for n in range(100):
        brightness += 2.55 
        pi1.set_PWM_dutycycle(19, brightness)
        time.sleep(0.01)
    
    for n in range(100):
        brightness -= 2.55 
        print brightness
        pi1.set_PWM_dutycycle(19, brightness)
        time.sleep(0.01)
        
    for n in range(100):
        brightness += 2.55
        pi1.set_PWM_dutycycle(26, brightness)
        time.sleep(0.01)
    
    for n in range(100):
        brightness -= 2.55 
        pi1.set_PWM_dutycycle(26, brightness)
        time.sleep(0.01)
    
    for n in range(100):
        brightness += 2.55
        pi1.set_PWM_dutycycle(13, brightness)
        time.sleep(0.01)
    
    for n in range(100):
        brightness -= 2.55 
        pi1.set_PWM_dutycycle(13, brightness)
        time.sleep(0.01)
       
    for n in range(100):
        brightness += 2.55 
        pi1.set_PWM_dutycycle(13, brightness)
        pi1.set_PWM_dutycycle(26, brightness)
        pi1.set_PWM_dutycycle(19, brightness)
        time.sleep(0.01)
        
    for n in range(100):
        brightness -= 2.55 
        pi1.set_PWM_dutycycle(13, brightness)
        pi1.set_PWM_dutycycle(26, brightness)
        pi1.set_PWM_dutycycle(19, brightness)
        time.sleep(0.01)
