# dummy_sensor.py

import paho.mqtt.client as mqtt
import psutil
import time

broker = "mqtt_broker"  # MQTT broker hostname

client = mqtt.Client()

client.connect(broker)

while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    mem_percent = psutil.virtual_memory().percent

    client.publish("sensor/cpu", cpu_percent)
    client.publish("sensor/mem", mem_percent)

    time.sleep(5)

