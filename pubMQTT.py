# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client

import subMQTT

broker = 'localhost'
port = 1883
topic = "smartHome/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'roger'
password = 'RogerThat'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Edge Server publisher Connected to MQTT Broker!")
        else:
            print("Edge publisher Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, device_id):
    msg_count = 0
    while msg_count < 3:
        time.sleep(1)
        msg = f"send signal: {msg_count}"
        result = client.publish(device_id, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"\n\nSend `{msg}` to device \t`{device_id}`\n\n")
        else:
            print(f"Failed to send message to device {device_id}")
        msg_count += 1
        subMQTT.run(device_id)
        time.sleep(5)


def run(device_id):
    client = connect_mqtt()
    client.loop_start()
    publish(client, device_id)


if __name__ == '__main__':
    run()
