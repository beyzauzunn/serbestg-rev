from dronekit import connect, VehicleMode

iha = connect("/dev/serial0", baud=57600, wait_ready=True)

print(iha.is_armable)

print(iha.armed)

iha.mode = VehicleMode("GUIDED")

iha.armed = True

iha.simple_takeoff(5)

time.sleep(10)

iha.mode = VehicleMode("RTL")
