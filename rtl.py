from dronekit import connect,VehicleMode
import time
iha = connect('127.0.0.1:14550',wait_ready=True)
while iha.is_armable != True
  print("iha arm edilebilir değil")
  time.sleep(1)
print("iha arm edilebilir")

iha.mode=VehicleMode("GUIDED")

iha.armed=True

while iha.armed!=True
  print("iha arm ediliyor")
  time.sleep(1)

  print("iha arm edildi")
 
iha.simple_takeoff(5)
time.sleep(15)

iha.parameters['LAND_SPEED']=20  
iha.mode=VehicleMode("RTL")
