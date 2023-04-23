
import json
import time
import random
import paho.mqtt.client as mqtt
from paho.mqtt import client as mqtt_client
import subMQTT
import pubMQTT


HOST = "localhost"
PORT = 1883     
WAIT_TIME = 0.25  
broker = 'localhost'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'roger'
password = 'RogerThat'


class Edge_Server:
    
    def __init__(self, instance_name):
        
        self._instance_id = instance_name
        self.client = mqtt.Client(self._instance_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.connect(HOST, PORT, keepalive=60)
        self.client.loop_start()
        self._registered_list = []

    # Terminating the MQTT broker and stopping the execution
    def terminate(self):
        self.client.disconnect()
        self.client.loop_stop()

    # Connect method to subscribe to various topics.     
    def _on_connect(self, client, userdata, flags, result_code):
        pubMQTT.connect_mqtt()
        pass
        
    # method to process the recieved messages and publish them on relevant topics 
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg):
        pubMQTT.publish(client)
        print(f"Received `{msg.payload.decode()}` from `{msg.device_id}` device")
        pass


    # Returning the current registered list
    def get_registered_device_list(self):
        return self._registered_list
        pass

    # Getting the status for the connected devices
    def get_status(self):
        pass

    # Controlling and performing the operations on the devices
    # based on the request received
    def set(self):
        pubMQTT.run()
        pass

    # def run():
    #     client = connect_mqtt()
    #     client.loop_start()
    #     publish(client)

    # run()