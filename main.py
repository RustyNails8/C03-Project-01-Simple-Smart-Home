import time
from EdgeServer import Edge_Server
from LightDevice import Light_Device
from ACDevice import AC_Device

WAIT_TIME = 0.25  

print("\nSmart Home Simulation started.")
# Creating the edge-server for the communication with the user

edge_server_1 = Edge_Server('edge_server_1')
time.sleep(WAIT_TIME)  

# Creating the light_device
print("Intitate the device creation and registration process." )
print("\nCreating the Light devices for their respective rooms.")

light_device_1 = Light_Device("1", "Kitchen")
time.sleep(WAIT_TIME)  

light_device_2 = Light_Device("2", "Garage")
time.sleep(WAIT_TIME)

light_device_3 = Light_Device("3", "BR1")
time.sleep(WAIT_TIME)

light_device_4 = Light_Device("4", "BR1")
time.sleep(WAIT_TIME)

light_device_5 = Light_Device("5", "Living")
time.sleep(WAIT_TIME)



# Creating the ac_device  
print("\nCreating the AC devices for their respective rooms. ")
ac_device_1 = AC_Device("ac_1", "BR1")
time.sleep(WAIT_TIME)  

print("\nSmart Home Simulation stopped.")
edge_server_1.terminate()
