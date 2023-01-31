from spike import PrimeHub, MotorPair, Motor, ColorSensor
from time import sleep

# Initialising
hub = PrimeHub()
movement_motors = MotorPair("F", "E")
movement_motors.set_default_speed(70)
front_motor = Motor("D")
color_sensor = ColorSensor("C")
color_sensor.light_up(100, 100, 100)

# Move robot out of 'home' area
movement_motors.start()
sleep(1.45)

# Stopping when it sees the road
color_sensor.wait_until_color("black")
movement_motors.stop()

# Turning left and dropping off the payload
movement_motors.move(9.5, "cm", -96)
movement_motors.move(10)
front_motor.run_for_degrees(-200, 30)

# -= BEGIN MISSION 2 =- #
# Moving toward the high 5 Module
movement_motors.move(44)

# Pulling out the thing
front_motor.run_for_degrees(180)
movement_motors.move(-5, "cm", 0, 100)
front_motor.run_for_degrees(-180)
movement_motors.move(-5)

# -= END OF MISSION 2 =- #
# -= BEGIN MISSION 3 =- #
movement_motors.move(10, "cm", 90)

movement_motors.start()
sleep(1.75)
color_sensor.wait_until_color("black")
movement_motors.stop()

movement_motors.move(5, "cm", -90)

for i in range(3):
    movement_motors.move(5)
    front_motor.run_for_degrees(200)
    movement_motors.move(-5)
    
# -= END MISSION 3 =- #