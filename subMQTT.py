# python3.6

import random
import time
from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic = "smartHome/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'roger'
password = 'RogerThat'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("sub Connected to MQTT Broker!")
        else:
            print("sub Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client, device_id):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.device_id}` device")

    client.subscribe(topic)
    client.on_message = on_message
    time.sleep(3)


def run(device_id):
    client = connect_mqtt()
    client.loop_start()
    subscribe(client, device_id)
    # client.loop_forever()


if __name__ == '__main__':
    run()
