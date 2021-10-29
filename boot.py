import network
import machine
import utime
import webrepl
import config

pum = machine.Pin(16, machine.Pin.OUT)
pum.off()

def do_connect():
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(config.WIFI_SSID, config.WIFI_PASSWD)
        ccounter = 0
        while not wlan.isconnected():
            ccounter+=1
            if(ccounter >= 200):  # 20 seconds
                print("Connection failed")
                break
            utime.sleep_ms(100)
    print('network config:', wlan.ifconfig())

webrepl.start()

do_connect()