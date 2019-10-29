""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import ubinascii

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()
# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
GATEWAY_ID = WIFI_MAC[:6] + "FFFF" + WIFI_MAC[6:12]

# If used with the TTN
#SERVER = 'router.eu.thethings.network'

# If used with loRaServer and Internet Access
#SERVER = '192.168.0.156'

# If used with the loRaServer and Raspberry as Access Point
SERVER = '192.168.1.1'

PORT = 1700
NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

# If used with Internet Access
#WIFI_SSID = 'vodafoneFE80'
#WIFI_PASS = 'Z6CPA3RREASP6X'

# If used with the Raspberry (As Access Point)
WIFI_SSID = 'AlexIoT'
WIFI_PASS = 'alejandro1234'

# for EU868
LORA_FREQUENCY = 868100000
LORA_GW_DR = "SF7BW125" # DR_5
LORA_NODE_DR = 5
