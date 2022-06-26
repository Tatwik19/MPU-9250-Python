import os
import sys
import time
import smbus
import math 

from imusensor.MPU9250 import MPU9250

address = 0x68
bus = smbus.SMBus(0)
imu = MPU9250.MPU9250(bus, address)
imu.begin()
# print("Caliberation Started")
# imu.caliberateGyro()
# print("Gyro caliberated")
# imu.caliberateAccelerometer()
# print("ACC caliberated")


# print("Calibrating Magnetometer")
# imu.caliberateMagPrecise()
# imu.caliberateMagApprox()
# print("Magnetometer Magnetometer")

# or load your own caliberation file
# imu.loadCalibDataFromFile("docs/calib_real4.json")

while True:
    imu.readSensor()
    imu.computeOrientation()
 
    print ("Accel x: {0} ; Accel y : {1} ; Accel z : {2}".format(imu.AccelVals[0]*180/M_PI, imu.AccelVals[1]*180/M_PI, imu.AccelVals[2]*180/M_PI))
    print ("Gyro x: {0} ; Gyro y : {1} ; Gyro z : {2}".format(imu.GyroVals[0], imu.GyroVals[1], imu.GyroVals[2]))
    print ("Mag x: {0} ; Mag y : {1} ; Mag z : {2}".format(imu.MagVals[0], imu.MagVals[1], imu.MagVals[2]))
    print ("roll: {0} ; pitch : {1} ; yaw : {2}".format(imu.roll, imu.pitch, imu.yaw),'\n')
        
    time.sleep(1)
