from spike import PrimeHub, MotorPair, Motor, ColorSensor
from time import sleep

# Initialising
hub = PrimeHub()
movement_motors = MotorPair("F", "E")
movement_motors.set_default_speed(50)
front_motor = Motor("D")
back_motor = Motor("B")
color_sensor = ColorSensor("C")

# Letting it move out of start area before it begins to look for black
movement_motors.start()
sleep(2.5)


# Stopping when it sees the road
color_sensor.wait_until_color("black")
movement_motors.stop()

# Turning left and dropping off the payload
movement_motors.move(11, "cm", -90)
movement_motors.move(43)
back_motor.run_for_degrees(150, 5)
back_motor.run_for_degrees(-150, 30)

# -= BEGIN MISSION 2 =- #
# Moving toward the high 5 Module
movement_motors.move(7.5)

# Pulling out the thing
front_motor.run_for_degrees(250, 100)
movement_motors.move(-10, "cm", 0, 10)
front_motor.run_for_degrees(-250)
movement_motors.move(-5)

# -= END OF MISSION 2 =- #
# -= BEGIN MISSION 3 =- #
movement_motors.move(9.9, "cm", 90)

movement_motors.start()
sleep(2.5)
color_sensor.wait_until_color("black")
movement_motors.stop()
movement_motors.move(7.5, "cm", -90)
movement_motors.move(-2.5)
front_motor.run_for_degrees(250)

for i in range(3):
    movement_motors.move(10)
    movement_motors.move(-7.5)
    
# -= END MISSION 3 =- #
# -= BEGIN MISSION 4 -= #

# -= END MISSION 4 =- #
# -= RETURN HOME =- #

movement_motors.move(-7.5)
movement_motors.move(22.5, 'cm', 90)

movement_motors.start()
color_sensor.wait_until_color("white")
sleep(2)

movement_motors.stop()