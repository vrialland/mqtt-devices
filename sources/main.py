import network
import time
import ujson

import config
import devices

from umqtt.simple import MQTTClient

RED = (10, 0, 0)
GREEN = (0, 10, 0)
YELLOW = (10, 10, 0)

ws2812 = devices.WS2812(14, 16)

# Define MQTT callback
def callback(topic, msg):
    print(msg)
    data = ujson.loads(msg)
    if data.pop("command") == "set_color":
        ws2812.set_color(**data)


# Set color to red while not connected to WIFI nor MQTT
ws2812.set_color(*RED)
print(b"WS2812 ready!")

#  Connect to WIFI
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect(config.WIFI_SSID, config.WIFI_PASSWORD)
    print(b"Connecting to wifi...")
    while not sta_if.isconnected():
        # Rotating red leds while not connected
        for i in range(ws2812.nb_leds):
            ws2812.set_color()
            ws2812.set_color(*RED, index=i % ws2812.nb_leds)

# Connected to wifi, set the leds yellow
print(b"Connected!")
ws2812.set_color(*YELLOW)

#  Setup MQTT client
print(b"Connecting to MQTT server...")
client = MQTTClient(b"test_device", config.MQTT_HOST, port=config.MQTT_PORT)
client.set_callback(callback)
client.connect()
client.subscribe(config.MQTT_TOPIC)
# Connection is OK, light the leds green for 3 seconds
print(b"Connected!")
ws2812.set_color(g=10)
time.sleep(2)
ws2812.set_color()

# Main loop
while True:
    client.wait_msg()

client.disconnect()
