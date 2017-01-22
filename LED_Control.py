import time
pi1 = pigpio.pi()

while(1):
    #Initializes all LED's to off
    pi1.write(19,1)
    pi1.write(26,1)
    pi1.write(13,1)
    
    time.sleep(1)
    pi1.set_PWM_dutycycle(19, 128)
    pi1.set_PWM_dutycycle(26, 128)
    pi1.set_PWM_dutycycle(13, 128)
