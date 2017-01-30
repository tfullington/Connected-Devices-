import pigpio
import time
 
pwm_max = 255 

class LampDriver():
  pi1 = pigpio.pi()    

  def set_led_color(self, rgb, brightness):

    for (19,  strength):
      self.pi1.write(19, 0 if strength == 0 else 1)
      brightness = brightness if brightness > 0 else 0.01
      self.pi1.set_PWM_dutycycle(19, brightness + pwm_max * strength + 1)
    for (26, strength):
      self.pi1.write(26,0 if strength == 0 else 1)
      brightness = brightness if brightness > 0 else 0.01
      self.pi1.set_PWM_dutycycle(26, brightness + pwm_max * strength + 1)



   # for (pin, strength) in { red_pin: rgb[0], green_pin: rgb[1], blue_pin: rgb[2] }.iteritems():
     # self.pi1.write(pin, 0 if strength == 0 else 1)
     # bright = bright if bright > 0 else 0.01 
     # self.pi1.set_PWM_dutycycle(pin, brightness * pwm_max  * strength + 1)
