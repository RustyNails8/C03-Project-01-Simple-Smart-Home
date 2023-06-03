
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
        if result_code == 0:
            print("Connected to MQTT broker")
            # Perform any additional setup or actions upon successful connection
        else:
            print(f"Connection failed with result code {result_code}")

        pubMQTT.connect_mqtt()
        # pass
        
    # method to process the recieved messages and publish them on relevant topics 
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg):
        # pubMQTT.publish(client)
        # print(f"Received `{msg.payload.decode()}` from `{msg.device_id}` device")

        topic = msg.topic
        payload = msg.payload.decode()

        # Process the received message based on the topic or payload
        # Add your own logic to handle different topics or payload formats
        if topic == "register_topic":
            self._handle_registration(payload)
        elif topic == "command_topic":
            self._handle_command(payload)
        else:
            print(f"Received message on topic: {topic}, payload: {payload}")
        # pass

    def _handle_registration(self, payload):
        # Parse the payload and perform device registration
        # Add the registered device to the _registered_list
        # Example:
        device_id = payload["device_id"]
        room = payload["room"]
        device_type = payload["device_type"]
        # Create the device instance based on the received information
        device = create_device_instance(device_id, room, device_type)
        # Register the device with the edge server
        self.register_device(device)

    def _handle_command(self, payload):
        # Parse the payload and perform the desired action or command
        # Example:
        device_id = payload["device_id"]
        command = payload["command"]
        # Find the device with the given device_id from the _registered_list
        device = self.find_device_by_id(device_id)
        if device:
            # Call the appropriate method on the device instance
            device.process_command(command)
        else:
            print(f"Device with ID '{device_id}' not found")
            
    def register_device(self, device):
        self._registered_list.append(device)

    # Returning the current registered list
    def get_registered_device_list(self):
        return self._registered_list
        # pass

    # Getting the status for the connected devices
    def get_status(self, device_id):
        for device in self._registered_list:
            if device._device_id == device_id:
                # Assuming the device has a method to retrieve its status
                print("\n Status of device  :      " + device._device_id + " ... ")
                print("      Device Status:      " + device._switch_status)
                print("      Device Type:        " + device._device_type)
                print("      Device Position:    " + device._room_type)                
                
                if device._device_type == "LIGHT" :
                    print("      Device Intensity:   " + device._light_intensity)   

                if device._device_type == "AC" :
                    print("      Device Temperature: " + str(device._temperature) + "  Celcius")   


            else:
                continue

            return device._switch_status
        # Device with the given device_id not found
        return None        
        # pass

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