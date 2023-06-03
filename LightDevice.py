import json
import paho.mqtt.client as mqtt

HOST = "localhost"
PORT = 1883


class Light_Device:
    _INTENSITY = ["LOW", "HIGH", "MEDIUM", "OFF"]

    def __init__(self, device_id, room):
        self._device_id = device_id
        self._room_type = room
        self._light_intensity = self._INTENSITY[2]
        self._device_type = "LIGHT"
        self._device_registration_flag = False
        self.client = mqtt.Client(self._device_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.on_disconnect = self._on_disconnect
        self.client.connect(HOST, PORT, keepalive=60)
        self.client.loop_start()
        self._switch_status = "OFF"


    def _on_connect(self, client, userdata, flags, result_code):
        if result_code == 0:
            print(f"Device {self._device_id} connected to MQTT broker")
            self._register_device()
            self.client.subscribe("command_topic")
        else:
            print(f"Connection failed with result code {result_code}")

    def _register_device(self):
        registration_payload = {
            "device_id": self._device_id,
            "room": self._room_type,
            "device_type": self._device_type
        }
        self.client.publish("register_topic", json.dumps(registration_payload))
        # print('Registration request is acknowledged for device ' + device_type + '_' + device_id + ' in ' + room_type)
        # print('Request is processed for ' + device_type + '_' + device_id + '.')
        # print('LIGHT-DEVICE Registered! - Registration status is available for ' + device_type + '_' + device_id + ' : True\n\n')

    def _on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = json.loads(msg.payload.decode())

        if topic == "command_topic":
            device_id = payload["device_id"]
            command = payload["command"]
            if device_id == self._device_id:
                self._handle_command(command)

    def _handle_command(self, command):
        if command == "turn_on":
            self._set_switch_status("ON")
        elif command == "turn_off":
            self._set_switch_status("OFF")
        elif command in self._INTENSITY:
            self._set_light_intensity(command)

    def _set_switch_status(self, switch_state):
        # Update the switch status of the device
        self._switch_status = switch_state
        print(f"Switch status of {self._device_id}: {self._switch_status}")

    def _set_light_intensity(self, light_intensity):
        for intensity in self._INTENSITY:
            if light_intensity == intensity:
                self._light_intensity = light_intensity
                print(f"{self._device_id} light intensity set to {light_intensity}")

    def _get_switch_status(self):
        # Return the current switch status of the device
        return self._switch_status

    def _get_light_intensity(self):
        # Return the current switch status of the device
        return self._light_intensity

    # def _set_switch_status(self, switch_state):
    #     print(f"{self._device_id} switch turned {switch_state}")

    # def _set_light_intensity(self, light_intensity):
    #     print(f"{self._device_id} light intensity set to {light_intensity}")

    def _on_disconnect(self, client, userdata, result_code):
        print(f"Device {self._device_id} disconnected from MQTT broker")


# # Example usage:
# device = Light_Device("device_id_1", "Kitchen")







# import json
# import paho.mqtt.client as mqtt

# HOST = "localhost"
# PORT = 1883


# class Light_Device():

#     # setting up the intensity choices for Smart Light Bulb  
#     _INTENSITY = ["LOW", "HIGH", "MEDIUM", "OFF"]

#     def __init__(self, device_id, room):
#         # Assigning device level information for each of the devices. 
#         self._device_id = device_id
#         self._room_type = room
#         self._light_intensity = self._INTENSITY[0]
#         self._device_type = "LIGHT"
#         self._device_registration_flag = False
#         self.client = mqtt.Client(self._device_id)  
#         self.client.on_connect = self._on_connect  
#         self.client.on_message = self._on_message  
#         self.client.on_disconnect = self._on_disconnect  
#         self.client.connect(HOST, PORT, keepalive=60)  
#         self.client.loop_start()  
#         self._register_device(self._device_id, self._room_type, self._device_type)
#         self._switch_status = "OFF"

#     def _register_device(self, device_id, room_type, device_type):
#         print('Registration request is acknowledged for device ' + device_type + '_' + device_id + ' in ' + room_type)
#         print('Request is processed for ' + device_type + '_' + device_id + '.')
#         print('LIGHT-DEVICE Registered! - Registration status is available for ' + device_type + '_' + device_id + ' : True\n\n')
#         # pass

#     # Connect method to subscribe to various topics. 
#     def _on_connect(self, client, userdata, flags, result_code):
#         if result_code == 0:
#             print("Connected to MQTT broker")
#             # Perform any additional setup or actions upon successful connection
#         else:
#             print(f"Connection failed with result code {result_code}")
#         # pass

#     def on_connect(client, userdata, flags, rc):
#         if rc == 0:
#             print("Connected to MQTT Broker!")
#         else:
#             print("Failed to connect, return code %d\n", rc)

#         client = mqtt_client.Client(client_id)
#         client.username_pw_set(username, password)
#         client.on_connect = on_connect
#         client.connect(broker, port)
#         return client
#         pass

#     # method to process the recieved messages and publish them on relevant topics 
#     # this method can also be used to take the action based on received commands
#     def _on_message(self, client, userdata, msg):
#         print(f"Received `{msg.payload.decode()}` from `{msg.device_id}` device")

#         topic = msg.topic
#         payload = msg.payload.decode()

#         # Process the received message based on the topic or payload
#         # Add your own logic to handle different topics or payload formats
#         if topic == "register_topic":
#             self._handle_registration(payload)
#         elif topic == "command_topic":
#             self._handle_command(payload)
#         else:
#             print(f"Received message on topic: {topic}, payload: {payload}")

#         # pass

#     def _handle_registration(self, payload):
#         # Parse the payload and perform device registration
#         # Add the registered device to the _registered_list
#         # Example:
#         device_id = payload["device_id"]
#         room = payload["room"]
#         device_type = payload["device_type"]
#         # Create the device instance based on the received information
#         device = create_device_instance(device_id, room, device_type)
#         # Register the device with the edge server
#         self.register_device(device)

#     def _handle_command(self, payload):
#         # Parse the payload and perform the desired action or command
#         # Example:
#         device_id = payload["device_id"]
#         command = payload["command"]
#         # Find the device with the given device_id from the _registered_list
#         device = self.find_device_by_id(device_id)
#         if device:
#             # Call the appropriate method on the device instance
#             device.process_command(command)
#         else:
#             print(f"Device with ID '{device_id}' not found")

#     # Getting the current switch status of devices 
#     def _get_switch_status(self):
#         pass

#     # Setting the the switch of devices
#     def _set_switch_status(self, switch_state):
#         pass

#     # Getting the light intensity for the devices
#     def _get_light_intensity(self):
#         pass

#     # Setting the light intensity for devices
#     def _set_light_intensity(self, light_intensity):
#         pass    

#      # Connect method to subscribe to various topics. 
#     def _on_disconnect(self, client, userdata, flags, result_code):
#         pass
