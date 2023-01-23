from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *


hub = PrimeHub()


def setup():
    Hub = PrimeHub()
    StatusLight = Hub.status_light
    LightMatrix = Hub.light_matrix

    distanceSensor = DistanceSepiknsor('<port>')
    colorSensor = ColorSensor('<port>')
    motor_r = Motor('<port>')
    motor_l = Motor('<port>')

    motors = MotorPair(motor_l, motor_r)


def startup():
    StatusLight.on(color='orange')
    setup()


@hub.event
async def on_ready():
    startup()

    # hello