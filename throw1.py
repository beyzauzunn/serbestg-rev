from dronekit import connect, VehicleMode,LocationGlobalRelative
import time
from pymavlink import mavutil
iha = connect("/dev/serial0", baud=57600, wait_ready=False)

while iha.is_armable is not True:
    print("IHA arm edilebilir durumda degil.")
    time.sleep(1)
print("IHA arm edilebilir.")

iha.mode = VehicleMode("THROW")
iha.parameters['THROW_TYPE']=0
iha.parameters['THROW_MOT_START']=0
iha.parameters['THROW_NEXTMODE']=4
time.sleep(5)
if iha.mode.name is "THROW":
    print("Throw moduna geçiş yapiliyor.")

print("Throw moduna geçiş yapildi.")

iha.armed = True

while iha.armed is False:
    print("IHA arm ediliyor...")
    time.sleep(1)
if iha.armed is True:
    print("IHA arm edildi.")

while iha.mode.name is not "GUIDED":
    time.sleep(1)
    
if iha.mode.name is "GUIDED":
   
    konum1=LocationGlobalRelative(41.1013957,29.0258011,3)
   
    konum2=LocationGlobalRelative(41.1016221,29.0262571,3)
   
    konum3=LocationGlobalRelative(41.1018626,29.0255812,3)
    
    iha.simple_goto(konum1)
    time.sleep(10)
    iha.simple_goto(konum2)
    time.sleep(10)
    iha.simple_goto(konum3)
    time.sleep(10)
    
iha.mode=VehicleMode("LAND")
