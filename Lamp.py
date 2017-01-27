import pigpio

pi1 = pigpio.pi()
brightness = 255
pi1.set_PWM_dutycycle(13, brightness)
pi1.set_PWM_dutycycle(26, brightness)
pi1.set_PWM_dutycycle(19, brightness)


