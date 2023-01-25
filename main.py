from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *


completed = []
__name__ = "__main__"


hub = PrimeHub()


async def setup():
    Hub = PrimeHub()
    StatusLight = Hub.status_light
    LightMatrix = Hub.light_matrix
    colorSensor = ColorSensor('C')
    forceSensor = ForceSensor('B')
    frontMotor = Motor('D')
    motor_r = Motor('E')
    motor_l = Motor('F')
    motors = MotorPair(motor_l, motor_r) 
    # Setup a control panel for hosting both motors at one time.

async def startup(Hub, StatusLight, motor_r, motor_l, motors):
    StatusLight.on(color="orange")

async def road(l_colorSensor, r_ColorSensor):
    if l_ColorSensor.result == "black" or r_ColorSensor.result == "black":
        return True
    else:
        return False

async def road_lr(l_colorSensor, r_ColorSensor):
    if l_colorSensor.result() == "white":
        return "Left"
    elif r_ColorSensor.result() == "white":
        return "Right"
    else:
        return None

        
async def travel(location: str):
    if location.lower() == "windmill":
        windmil_challenge()
        location.lower().append(completed)
    elif location.lower() == "":
        pass
        location.lower().append(completed)
    elif location.lower() == "":
        pass
        location.lower().append(completed)
    elif location.lower() == "":
        pass
        location.lower().append(completed)
    else:
        print("Location is invalid.")


# -= Challenges =-



# -= End Challenges =-

async def setup(self):
    self.runModule(setup)
    self.runModule(startup)
    
    self.initiate(road, road_lr, travel)
    self.initiate(windmil_challenge)
    self.initiateModule([windmil_challenge, road, road_lr, travel].seperate())

