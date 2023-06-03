import time
from EdgeServer import Edge_Server
from LightDevice import Light_Device
from ACDevice import AC_Device

import pubMQTT
import subMQTT
from pprint import pprint

WAIT_TIME = 1.25  

print("\nSmart Home Simulation started.")
# Creating the edge-server for the communication with the user

edge_server_1 = Edge_Server('edge_server_instance_1')
# subMQTT.run()
# pubMQTT.run()
time.sleep(WAIT_TIME)    

# Creating the light_device
print("Intitate the device creation and registration process." )
print("\nCreating the Light devices for their respective rooms.")
time.sleep(5)

print("\n\n******************* SECTION 1: REGSITRATION OF THE DEVICES THROUGH SERVER *******************\n")

print("\n\n******************* REGSITRATION OF LIGHT DEVICES INITIATED *******************\n")

light_device_1 = Light_Device("light_1", "Kitchen")
edge_server_1.register_device(light_device_1)
time.sleep(WAIT_TIME)    

light_device_2 = Light_Device("light_2", "Garage")
edge_server_1.register_device(light_device_2)
time.sleep(WAIT_TIME)  

light_device_3 = Light_Device("light_3", "BedRoom_1")
edge_server_1.register_device(light_device_3)
time.sleep(WAIT_TIME)  

light_device_4 = Light_Device("light_4", "BedRoom_2")
edge_server_1.register_device(light_device_4)
time.sleep(WAIT_TIME)  

light_device_5 = Light_Device("light_5", "Living")
edge_server_1.register_device(light_device_5)
time.sleep(WAIT_TIME)  

print("\n\n******************* REGSITRATION OF AC DEVICES INITIATED *******************\n")


# Creating the ac_device  
print("\nCreating the AC devices for their respective rooms. ")
ac_device_1 = AC_Device("ac_1", "BedRoom_1")
edge_server_1.register_device(ac_device_1)
time.sleep(WAIT_TIME)    

ac_device_2 = AC_Device("ac_2", "BedRoom_2")
edge_server_1.register_device(ac_device_2)
time.sleep(WAIT_TIME)  

ac_device_3 = AC_Device("ac_3", "Living")
edge_server_1.register_device(ac_device_3)
time.sleep(WAIT_TIME)  


print("\n\n******************* GETTING THE STATUS BY DEVICE_ID *******************\n")
time.sleep(5)

status = edge_server_1.get_status("light_1")
status = edge_server_1.get_status("light_2")
status = edge_server_1.get_status("light_3")
status = edge_server_1.get_status("light_4")
status = edge_server_1.get_status("light_5")

status = edge_server_1.get_status("ac_1")
status = edge_server_1.get_status("ac_2")
status = edge_server_1.get_status("ac_3")


# pubMQTT.run("light_1")
# pubMQTT.run("light_2")
# # pubMQTT.run("light_3")
# # pubMQTT.run("light_4")
# # pubMQTT.run("light_5")

# pubMQTT.run("ac_1")
# pubMQTT.run("ac_2")
# # pubMQTT.run("ac_3")

# Now we have these status

# ac_device_3._device_id
# ac_device_3._device_type
# ac_device_3._room_type
# ac_device_3._switch_status
# ac_device_3._temperature


# light_device_5._device_id
# light_device_5._device_type
# light_device_5._room_type
# light_device_5._switch_status
# light_device_5._light_intensity


print("\n\n******************* SECTION 2: SWITCH ON AND OFF THE DEVICES *******************\n")
time.sleep(5)

registered_devices = edge_server_1.get_registered_device_list()
# print(registered_devices)
# pprint(registered_devices)

print("\n\n******************* Switch ON all lights *******************\n")
time.sleep(WAIT_TIME)  
light_device_1._set_switch_status("ON")
light_device_2._set_switch_status("ON")
light_device_3._set_switch_status("ON")
light_device_4._set_switch_status("ON")
light_device_5._set_switch_status("ON")

status = edge_server_1.get_status("light_1")
status = edge_server_1.get_status("light_2")
status = edge_server_1.get_status("light_3")
status = edge_server_1.get_status("light_4")
status = edge_server_1.get_status("light_5")
time.sleep(WAIT_TIME)  


print("\n\n******************* Switch OFF all lights except BedRoom Lights *******************\n")
time.sleep(WAIT_TIME)  
light_device_1._set_switch_status("OFF")
light_device_2._set_switch_status("OFF")
light_device_5._set_switch_status("OFF")

status = edge_server_1.get_status("light_1")
status = edge_server_1.get_status("light_2")
status = edge_server_1.get_status("light_3")
status = edge_server_1.get_status("light_4")
status = edge_server_1.get_status("light_5")
time.sleep(WAIT_TIME)  


print("\n\n******************* Switch ON all AC *******************\n")
time.sleep(WAIT_TIME)  
ac_device_1._set_switch_status("ON")
ac_device_2._set_switch_status("ON")
ac_device_3._set_switch_status("ON")

status = edge_server_1.get_status("ac_1")
status = edge_server_1.get_status("ac_2")
status = edge_server_1.get_status("ac_3")
time.sleep(WAIT_TIME)  

print("\n\n******************* Switch OFF all BedRoom AC *******************\n")
time.sleep(WAIT_TIME)  
ac_device_1._set_switch_status("OFF")
ac_device_2._set_switch_status("OFF")
ac_device_3._set_switch_status("ON")

status = edge_server_1.get_status("ac_1")
status = edge_server_1.get_status("ac_2")
status = edge_server_1.get_status("ac_3")
time.sleep(WAIT_TIME)  



print("\n\n******************* SECTION 3: INCREASE AND DECREASE INTENSITY AND TEMPERATURE OF DEVICES *******************\n")
time.sleep(5)

registered_devices = edge_server_1.get_registered_device_list()
# print(registered_devices)
# pprint(registered_devices)

print("\n\n******************* Set HIGH INTENSITY ON all lights *******************\n")
time.sleep(WAIT_TIME)  
light_device_1._set_light_intensity("HIGH")
light_device_2._set_light_intensity("HIGH")
light_device_3._set_light_intensity("HIGH")
light_device_4._set_light_intensity("HIGH")
light_device_5._set_light_intensity("HIGH")

status = edge_server_1.get_status("light_1")
status = edge_server_1.get_status("light_2")
status = edge_server_1.get_status("light_3")
status = edge_server_1.get_status("light_4")
status = edge_server_1.get_status("light_5")
time.sleep(WAIT_TIME)  


print("\n\n******************* SET LOW Intensity ON BedRoom Lights *******************\n")
time.sleep(WAIT_TIME)  
light_device_1._set_light_intensity("LOW")
light_device_2._set_light_intensity("LOW")
light_device_5._set_light_intensity("LOW")

status = edge_server_1.get_status("light_1")
status = edge_server_1.get_status("light_2")
status = edge_server_1.get_status("light_3")
status = edge_server_1.get_status("light_4")
status = edge_server_1.get_status("light_5")
time.sleep(WAIT_TIME)  


print("\n\n******************* Set Temperatue of 24 degree Celcius on all AC *******************\n")
time.sleep(WAIT_TIME)  

ac_device_1._set_switch_status("ON")
ac_device_2._set_switch_status("ON")
ac_device_3._set_switch_status("ON")

ac_device_1._set_temperature(24)
ac_device_2._set_temperature(24)
ac_device_3._set_temperature(24)

status = edge_server_1.get_status("ac_1")
status = edge_server_1.get_status("ac_2")
status = edge_server_1.get_status("ac_3")
time.sleep(WAIT_TIME)  

print("\n\n******************* Switch OFF all BedRoom AC *******************\n")
time.sleep(WAIT_TIME)  
ac_device_1._set_switch_status("OFF")
ac_device_2._set_switch_status("OFF")
ac_device_3._set_switch_status("ON")

status = edge_server_1.get_status("ac_1")
status = edge_server_1.get_status("ac_2")
status = edge_server_1.get_status("ac_3")
time.sleep(WAIT_TIME)  


print("\nSmart Home Simulation stopped.")
edge_server_1.terminate()
