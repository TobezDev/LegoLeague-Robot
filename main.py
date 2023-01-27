from spike import PrimeHub, MotorPair, Motor, ColorSensor

hub = PrimeHub()


def log(text):
    try:
        print(f"[LOGS]: {text}")
    except SyntaxError as err:
        print(f"[SyntaxError]: {err}")
    except TypeError as err:
        print(f"[TypeError]: {err}")


movement_motors = MotorPair("F", "E")
movement_motors.set_default_speed(70)

picker_motor = Motor("D")

colour_sensor = ColorSensor("C")
colour_sensor.light_up(100, 100, 100)

picker_motor.run_to_position(0)
movement_motors.move(30)
movement_motors.start()

colour_sensor.wait_until_color("black")
log("Road Found")

movement_motors.stop()
movement_motors.move(10, "cm", -90)
movement_motors.move(10)

picker_motor.run_for_degrees(-200, 30)
