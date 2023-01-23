from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

def setup():
    Hub = PrimeHub()
    StatusLight = Hub.status_light
    LightMatrix = Hub.light_matrix

    distanceSensor = DistanceSensor('<port>')

    lightSensor = LightSensor('<port>')
    l_colorSensor = ColorSensor('<port>')
    r_colorSensor = ColorSensor('<port>')

    motor_r = Motor('<port>')
    motor_l = Motor('<port>')

    motors = MotorPair(motor_l, motor_r)

def startup(Hub, StatusLight, motor_r, motor_l, motors):
    StatusLight.on(color="orange")

def road(l_colorSensor, r_ColorSensor):
    if l_ColorSensor.result == "black" or r_ColorSensor.result == "black":
        return True
    else:
        return False

def road_lr(l_colorSensor, r_ColorSensor):
    if l_colorSensor.result() == "white":
        return "Left"
    elif r_ColorSensor.result() == "white":
        return "Right"
    else:
        return None

# -= Challenges =-

def windmil_thing():
    if DistanceSensor.result <= 3:
        motors.forward(rotations=0.5)
        motors.backward(rotations=0.5)
        motors.forward(rotations=0.5)
        motors.backward(rotations=0.5)
        motors.forward(rotations=0.5)
    else:
        onRoad = road()
        if onRoad is None:
            lr = road_lr()
            if lr == "Left":
                motor_r(rotations="")
            elif lr == "Right":
                motor_l.forward(rotations="")
            else:
                print("[LOGS]: Error: Cannot find adequate path for function: road.")
        

if __name__ == "__main__":
    setup()
    startup()


