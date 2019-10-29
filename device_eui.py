from network import WLAN
import ubinascii
wl = WLAN()
ubinascii.hexlify(wl.mac())[:6] + 'FFFF' + ubinascii.hexlify(wl.mac())[6:]
