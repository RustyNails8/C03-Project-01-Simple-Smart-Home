import time
from EdgeServer import Edge_Server
from LightDevice import Light_Device
from ACDevice import AC_Device

import pubMQTT
import subMQTT

WAIT_TIME = 1.25  

print("\nSmart Home Simulation started.")
# Creating the edge-server for the communication with the user

edge_server_1 = Edge_Server('edge_server_1')
# subMQTT.run()
# pubMQTT.run()
time.sleep(WAIT_TIME)  

# Creating the light_device
print("Intitate the device creation and registration process." )
print("\nCreating the Light devices for their respective rooms.")
time.sleep(5)
print("\n\n******************* REGSITRATION OF THE DEVICES THROUGH SERVER *******************\n")

print("\n\n******************* REGSITRATION OF LIGHT DEVICES INITIATED *******************\n")

light_device_1 = Light_Device("light_1", "Kitchen")
time.sleep(WAIT_TIME)  

light_device_2 = Light_Device("light_2", "Garage")
time.sleep(WAIT_TIME)

light_device_3 = Light_Device("light_3", "BR1")
time.sleep(WAIT_TIME)

light_device_4 = Light_Device("light_4", "BR1")
time.sleep(WAIT_TIME)

light_device_5 = Light_Device("light_5", "Living")
time.sleep(WAIT_TIME)

print("\n\n******************* REGSITRATION OF AC DEVICES INITIATED *******************\n")


# Creating the ac_device  
print("\nCreating the AC devices for their respective rooms. ")
ac_device_1 = AC_Device("ac_1", "BR1")
time.sleep(WAIT_TIME)  

ac_device_1 = AC_Device("ac_2", "BR2")
time.sleep(WAIT_TIME)

ac_device_1 = AC_Device("ac_3", "Living")
time.sleep(WAIT_TIME)


print("\n\n******************* GETTING THE STATUS AND CONTROLLING THE DEVICES *******************\n")

print("\n\n******************* GETTING THE STATUS BY DEVICE_ID *******************\n")

pubMQTT.run("light_1")
pubMQTT.run("light_2")
pubMQTT.run("light_3")
pubMQTT.run("light_4")
pubMQTT.run("light_5")

pubMQTT.run("ac_1")
pubMQTT.run("ac_2")
pubMQTT.run("ac_3")


print("\nSmart Home Simulation stopped.")
edge_server_1.terminate()
