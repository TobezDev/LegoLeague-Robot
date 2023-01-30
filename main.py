from spike import PrimeHub, MotorPair, Motor, ColorSensor

hub = PrimeHub()

movement_motors = MotorPair("F", "E")
front_motor = Motor("D")
color_sensor = ColorSensor("C")

movement_motors.set_default_speed(70)

color_sensor.light_up(100, 100, 100)

front_motor.run_to_position(0)
movement_motors.move(30)

movement_motors.start()

color_sensor.wait_until_color("black")

movement_motors.stop()
movement_motors.move(10, "cm", -90)
movement_motors.move(10)

front_motor.run_for_degrees(-200, 30)

# -=-=- #
movement_motors.move(5, "cm", -90)

movement_motors.move(40)

movement_motors.move(5, "cm", 90)

