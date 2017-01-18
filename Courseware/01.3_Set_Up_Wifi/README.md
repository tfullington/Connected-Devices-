## Now let's connect your Raspberry Pi to WiFi via the Command Line.
Some helpful instructions: [https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md)

**NOTE:** the Linux `sudo` command allows you to execute commands as another user.  By default, that other user is _root_, the superuser.  Executing commands as _root_ can be dangerous - you can, for example, delete every file on the system.  That would probably be bad.  We will require superuser privileges to access certain hardware devices, change system settings, and generally muck about with the Raspian system.

Use sudo carefully.  [Don't let the power go to your head.](https://xkcd.com/149/)

### Configure Your Wireless Network
1. In the terminal, scan for WiFi networks via `sudo iwlist wlan0 scan`. You'll see networks listed. You'll want to find the name of the network and password.
	* The name of the network is from either ssid or ESSID.
2. Add the network details to your Raspberry Pi.  A configuration for connecting to "CaseGuest" is shown below.
	* Using whatever terminal text editor you prefer ([https://www.raspberrypi.org/documentation/linux/usage/text-editors.md](https://www.raspberrypi.org/documentation/linux/usage/text-editors.md)), open the `wpa_supplicant` configuration file. The command will look something like: `sudo vi /etc/wpa_supplicant/wpa_supplicant.conf`.
	* The configuration file will open, add the information for your network below the existing content. ![Add Network](Images/Add_Network.png)
	* Save the updated wpa supplicant file.
3. At this stage, reboot your Raspberry Pi via `sudo reboot` (a reboot is not strictly necessary, but it is the easiest way to ensure all of the network configurations are updated).
4. After the pi reboots, login again via the serial console and test your network connection via `ping www.google.com` to verify that you are connected to the Internet.
5. Test that ssh is working.  Get the IP address of your Pi via `ifconfig` which will have output like

    ```
    nbarendt@nick-raspberrypi:~$ ifconfig
    eth0      Link encap:Ethernet  HWaddr b8:27:eb:2f:9f:38  
              UP BROADCAST MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
              UP LOOPBACK RUNNING  MTU:65536  Metric:1
              RX packets:72 errors:0 dropped:0 overruns:0 frame:0
              TX packets:72 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0
              RX bytes:6288 (6.1 KiB)  TX bytes:6288 (6.1 KiB)

    wlan0     Link encap:Ethernet  HWaddr 00:13:ef:30:02:72  
              inet addr:10.0.1.34  Bcast:10.0.1.255  Mask:255.255.255.0
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:40 errors:0 dropped:4 overruns:0 frame:0
              TX packets:45 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000
              RX bytes:6883 (6.7 KiB)  TX bytes:8131 (7.9 KiB)
    ```

    SSH is the "Secure Shell".  Linux and Mac's have an SSH client installed by default.  If you are on Windows, consider [PuTTy](http://www.putty.org/).  
    Fom ssh to your Raspberry Pi's IP address via 

    ```
    ssh -l pi PUT_YOUR_PIS_IP_ADDRESS_HERE
    ```

     or, alternatively, 

    ```
    ssh pi@PUT_YOUR_PIS_IP_ADDRESS_HERE
    ```

### Disable Wireless Power Management

Typically, you want your devices to reduce their energy usage.  For instance, a default configuration for Raspbian on the Raspberry Pi 3 is to put the WiFi interface to sleep if it is idle for a certain lenght of time.  This creates some problems for us, though, as LAMPI will disappear from the wireless network if there is no wireless traffic.  We therefore need to disable power management on the WiFi interface.

1.  Using your preferred text editor open the ```/etc/network/interfaces``` file as root.  The command will look something like: ```sudo vi /etc/network/interfaces```.

2.  Edit the file to include ```wireless-power off``` after the ```iface wlan0 inet manual``` line, like so:

    ```
    # interfaces(5) file used by ifup(8) and ifdown(8)
     
    # Please note that this file is written to be used with dhcpcd
    # For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'
     
    # Include files from /etc/network/interfaces.d:
    source-directory /etc/network/interfaces.d
     
    auto lo
    iface lo inet loopback
     
    iface eth0 inet manual
     
    allow-hotplug wlan0
    iface wlan0 inet manual
        wireless-power off
        wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
     
    allow-hotplug wlan1
    iface wlan1 inet manual
        wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
    ```

7. At this stage, power down your Raspberry Pi via `sudo poweroff` and disconnect the power.

Next up: go to [Interface LED](../01.4_Interface_LED/README.md)

&copy; 2015-17 LeanDog, Inc. and Nick Barendt
