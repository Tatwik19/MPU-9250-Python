import smbus
import math
import numpy as np
import time

from imusensor.MPU9250 import MPU9250

# IMU Address
address = 0x68
bus = smbus.SMBus(0)
imu = MPU9250.MPU9250(bus, address)
imu.begin()
imu.loadCalibDataFromFile("docs/calib_real4.json")

def currentHeading(): #Get current Headding/Facing direction from Magnetometer (0 to 360 deg)
    
    imu.readSensor()
    imu.computeOrientation()
    
        
    magX = imu.MagVals[0] 
    magY = imu.MagVals[1]
    M_PI = math.pi
    offSet = 30 # Correction Angle
    
    if (magY > 0):
        heading = 90 - math.atan(magX/magY)*(180/M_PI)
        
    elif (magY < 0):
        heading = 270 - math.atan(magX/magY)*(180/M_PI)
        
    elif (magY == 0 and magX < 0):
        heading = 180
        
    elif (magY == 0 and magX > 0): 
        heading = 0
        
    heading = -heading + offSet
    if heading > 360:
        heading = heading - 360;
    elif heading < 0:
        heading = heading + 360;
        
    return heading
try:
    while True:
        
        imu.readSensor() # Read IMU Sensor
        imu.computeOrientation()
        
        compas = currentHeading()
        
        print(currentHeading(),"Degrees")
        
#         Yaw = math.atan((math.cos(imu.AccelVals[1])*((imu.MagVals[2]*math.sin(imu.AccelVals[0]))-(imu.MagVals[1]*math.cos(imu.AccelVals[0]))))/(imu.MagVals[0]))
#         YawD = Yaw*180/M_PI
#         print(YawD)
#         print((math.atan(magY/magX))*(180/M_PI),'\n')

        time.sleep(2)
        
except KeyboardInterrupt:
    sys.exit(0)
