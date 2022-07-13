from dronekit import connect, VehicleMode,LocationGlobalRelative
import time
from pymavlink import mavutil
iha = connect("/dev/serial0", baud=57600, wait_ready=True)

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



def goto_position_target_relative_ned(x, y, down):

    msg = iha.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, # frame
        0b0000111111111000, # type_mask (only positions enabled)
        x, y, down,
        0, 0, 0, # x, y, z velocity in m/s  (not used)
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
    # send command to iha
    iha.send_mavlink(msg)

while iha.mode.name is not "GUIDED":
    time.sleep(1)
    
if iha.mode.name is "GUIDED":
    
    goto_position_target_relative_ned(5,5,-5)
    
    konum1=LocationGlobalRelative(-35.36295893,149.16581571,2)
   
    konum2=LocationGlobalRelative(-35.36234136,149.16467289,2)
   
    konum3=LocationGlobalRelative(-35.36200450,149.16592586,2)
    
    iha.simple_goto(konum1)
    time.sleep(10)
    iha.simple_goto(konum2)
    time.sleep(10)
    iha.simple_goto(konum3)
    time.sleep(10)
    
iha.mode=VehicleMode("LAND")
