# Set up PiTFT Screen


### Install the PiTFT kernel
Instructions based on [this guide on Adafruit](https://learn.adafruit.com/running-opengl-based-games-and-emulators-on-adafruit-pitft-displays/pitft-setup).

First, install Adafruit's PiTFT kernel and configuration tools. 

```
cd ~
curl -SLs https://apt.adafruit.com/add | sudo bash
sudo apt-get update
```

> **COMPATIBILITY:** as of the time of this writing (12/28/16), adafruit's kernel version is behind the main Raspbian kernel version; if the Rasbpian kernel is installed, the PiTFT screen will not function correctly, so **we need to specify the kernel version we want, __and__ mark the package as "hold" so it is not automatically updated in the future.**

```
sudo apt-get install raspberrypi-kernel=1.20161101-1
sudo apt-mark hold raspberrypi-kernel
```

(You can use ```sudo apt-mark showhold``` to see what packages are currently under hold, and ```sudo apt-mark unhold <packagename>``` if you make  a mistake.)

Then upgrade and install the other needed packages. 
```
sudo apt-get upgrade
sudo apt-get install -y libraspberrypi0 libraspberrypi-dev raspberrypi-bootloader
sudo apt-get install -y adafruit-pitft-helper
```

Next we'll tell the configuration tool about our screen. Run the following.
**Important**: Answer **n** to both questions (if you messed up and said **y**, just re-run the command).
```
sudo adafruit-pitft-helper -t 28c
```
("28c" configures for the 2.8" Capacitive touch display)

Kivy uses GLES, which will only be hardware accelerated on the primary framebuffer (/dev/fb0). The PiTFT uses /dev/fb1. As such, we'll use a tool called `fbcp` to blit the primary framebuffer to the PiTFT's framebuffer.

```
sudo apt-get install -y cmake
git clone https://github.com/tasanakorn/rpi-fbcp
cd rpi-fbcp/
mkdir build
cd build/
cmake ..
make
sudo install fbcp /usr/local/bin/fbcp
```

Now that it's installed, we need to run fbcp on startup.

```
sudo bash -c 'echo -e "@reboot root /usr/local/bin/fbcp &\n" > /etc/cron.d/0_fbcp'
```

Now we'll chose a console font that reads better on the tiny screen. Run:
```
sudo dpkg-reconfigure console-setup
```
Select **UTF-8**, **Guess optimal character set**, **Terminus** and **6x12 (framebuffer only)**.

Finally, we'll configure the device tree for the PiTFT. Open **/boot/config.txt** in a text editor with sudo, i.e. `sudo nano /boot/config.txt`.

Find the **last line of the file** that starts with **dtoverlay** (it is possible that your config.txt will accumulate more than one; only the last one matters). It should look like this:
```
dtoverlay=pitft28c,rotate=90,speed=32000000,fps=20
```

...and change it to the following:
```
dtoverlay=pitft28c,rotate=180,speed=62500000,fps=30
```

The above ```rotate=180``` rotates the screen into "portrait" mode, the ```speed=64000000``` increases the SPI bus speed for higher performance, and the ```fps=30``` sets the frames per second rate.  See [here](https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/faq#faq-11) for more info.

Finally, add the following lines to the bottom of **/boot/config.txt** with sudo. This will configure the primary framebuffer / HDMI output to 320x240. **This will most likely break your HDMI output on TVs until you remove these lines.**
```
hdmi_force_hotplug=1
hdmi_cvt=240 320 60 1 0 0 0
hdmi_group=2
hdmi_mode=87
```

Save and quit. Run `sudo reboot`.

Next up: go to [Hello, Kivy](../02.3_Hello_Kivy/README.md)

&copy; 2015-17 LeanDog, Inc. and Nick Barendt
