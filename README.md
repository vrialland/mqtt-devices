# mqtt-devices
Micropython app to handle several devices through MQTT

## Config file

Create a file named `config.py` in the sources folder with this template:

```
# WIFI
WIFI_SSID = b"my_ssid"
WIFI_PASSWORD = b"my_password"

#  MQTT
MQTT_HOST = b"127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = b"some_topic"
```

Here are the different values:

- `WIFI_SSID`: SSID of the wifi network you're connecting to
- `WIFI_PASSWORD`: Password of the wifi network
- `MQTT_HOST`: MQTT server's IP
- `MQTT_PORT`: MQTT server's port
- `MQTT_TOPIC`: Name of the topic the client uses to look for commands
