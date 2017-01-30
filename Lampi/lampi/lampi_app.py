from kivy.app import App
from kivy.properties import NumericProperty, StringProperty, ListProperty
from lamp_driver import LampDriver
import colorsys

class LampiApp(App):
  lamp_driver = LampDriver()
  hsb = [0,1,0]

  current = ListProperty([1,0,0])
  current_sat = ListProperty([1,0,0])

  def on_start(self):
    self.update_color()

  def _hue_slider(self,instance,value):
    self.hsb[0] = value
    self.update_color()

  def _sat_slider(self, instance,value):
    self.hsb[1] = value
    self.update_color()

  def _bright_slider(self, instance, value):
    self.hsb[2] = value
    self.update_color()

  def update_color(self):
    self.current = colorsys.hsv_to_rgb(self.hsb[0],self.hsb[1],1.0)
    self.current_sat = colorsys.hsv_to_rgb(self.hsb[0],1.0,1.0)
    self.lamp_driver.set_led_color(self.current, self.hsb[2])
