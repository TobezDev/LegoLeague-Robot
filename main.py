from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

completed = []

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
    __name__ = "__main__"
    # Add a name = main var to check if any edits happen to the hub between setup and startup.

async def startup():
    StatusLight.on(color="orange")
    hub.setStatus("startup")
    localeSetup = hub.findDir('/home/runner/primehub/setup/setup.ini')
    hub.runScript(localeSetup)
    return "true"

# Road Tracker Helper
async def roadCheck():
    if ColorSensor.result == "black":
        return "road"
    elif ColorSensor.result == "white":
        return "road_offside"
    else:
        return "not_road"

# -= Challenges  =-

async def oilPlatform():
    try:
        pass
        # put movement script here (preferably hardcoded)
    except Exception as e:
        hub.stopAll()
        print(f"[ERROR]: Hub has encountered an exception: {e}")


# -= End Challenges =-

setup()

if __name__ == "__main__" and setup() == "true":
    startup()
    