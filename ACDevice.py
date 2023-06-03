import json
import paho.mqtt.client as mqtt

HOST = "localhost"
PORT = 1883


class AC_Device:
    _INTENSITY = ["LOW", "HIGH", "MEDIUM", "OFF"]

    def __init__(self, device_id, room):
        self._device_id = device_id
        self._room_type = room
        self._temperature = 22
        self._device_type = "AC"
        self._device_registration_flag = False
        self.client = mqtt.Client(self._device_id)  
        self.client.on_connect = self._on_connect  
        self.client.on_message = self._on_message  
        self.client.on_disconnect = self._on_disconnect  
        self.client.connect(HOST, PORT, keepalive=60)  
        self.client.loop_start()  
        # self._register_device(self._device_id, self._room_type, self._device_type)
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
#         # print('Registration request is acknowledged for device ' + device_type + '_' + device_id + ' in ' + room_type)
#         # print('Request is processed for ' + device_type + '_' + device_id + '.')
#         # print('LIGHT-DEVICE Registered! - Registration status is available for ' + device_type + '_' + device_id + ' : True\n\n')        
#         # pass


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

    def _set_temperature(self, temperature):
        self._temperature = temperature
        print(f"{self._device_id} temperature set to {temperature}")

    def _get_switch_status(self):
        # Return the current switch status of the device
        return self._switch_status

    def _get_temperature(self):
        # Return the current switch status of the device
        return self._temperature              

    def _on_disconnect(self, client, userdata, result_code):
        print(f"Device {self._device_id} disconnected from MQTT broker")



# import json
# import paho.mqtt.client as mqtt


# HOST = "localhost"
# PORT = 1883
    
# class AC_Device():
    
#     _MIN_TEMP = 18  
#     _MAX_TEMP = 32  

#     def __init__(self, device_id, room):
        
#         self._device_id = device_id
#         self._room_type = room
#         self._temperature = 22
#         self._device_type = "AC"
#         self._device_registration_flag = False
#         self.client = mqtt.Client(self._device_id)  
#         self.client.on_connect = self._on_connect  
#         self.client.on_message = self._on_message  
#         self.client.on_disconnect = self._on_disconnect  
#         self.client.connect(HOST, PORT, keepalive=60)  
#         self.client.loop_start()  
#         self._register_device(self._device_id, self._room_type, self._device_type)
#         self._switch_status = "OFF"

#     # calling registration method to register the device
#     def _register_device(self, device_id, room_type, device_type):
#         registration_payload = {
#             "device_id": self._device_id,
#             "room": self._room_type,
#             "device_type": self._device_type
#         }
#         self.client.publish("register_topic", json.dumps(registration_payload))
        
#         # print('Registration request is acknowledged for device ' + device_type + '_' + device_id + ' in ' + room_type)
#         # print('Request is processed for ' + device_type + '_' + device_id + '.')
#         # print('LIGHT-DEVICE Registered! - Registration status is available for ' + device_type + '_' + device_id + ' : True\n\n')        
#         # pass

#     # Connect method to subscribe to various topics. 
#     # def _on_connect(self, client, userdata, flags, result_code):
#     #     pass

#     def _on_connect(client, userdata, flags, rc):
#         if result_code == 0:
#             print(f"Device {self._device_id} connected to MQTT broker")
#             self._register_device()
#             self.client.subscribe("command_topic")
#         else:
#             print(f"Connection failed with result code {result_code}")
            
#                     # if rc == 0:
#         #     print("Connected to MQTT Broker!")
#         # else:
#         #     print("Failed to connect, return code %d\n", rc)

#         # client = mqtt_client.Client(client_id)
#         # client.username_pw_set(username, password)
#         # client.on_connect = on_connect
#         # client.connect(broker, port)
#         # return client
#         # pass

#     # method to process the recieved messages and publish them on relevant topics 
#     # this method can also be used to take the action based on received commands
#     def _on_message(self, client, userdata, msg): 
#         topic = msg.topic
#         payload = json.loads(msg.payload.decode())

#         if topic == "command_topic":
#             device_id = payload["device_id"]
#             command = payload["command"]
#             if device_id == self._device_id:
#                 self._handle_command(command)        # print(f"Received `{msg.payload.decode()}` from `{msg.device_id}` device")
#         # pass

#     # Getting the current switch status of devices 
#     def _get_switch_status(self):
#         pass

#     # Setting the the switch of devices
#     def _set_switch_status(self, switch_state):
#         pass

#     # Getting the temperature for the devices
#     def _get_temperature(self):
#         pass        

#     # Setting up the temperature of the devices
#     def _set_temperature(self, temperature):
#         pass

#     # Connect method to subscribe to various topics. 
#     def _on_disconnect(self, client, userdata, flags, result_code):
#         pass    
