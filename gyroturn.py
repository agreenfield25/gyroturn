from drivetrain import Drivetrain


class GyroTurn:

    def __init__(self, Wheels,goal):
        self.drivetrain=Wheels
        self.goal=goal
        self.kp=-1/25

    def run(self):
        current_reading=self.drivetrain.getGyroAngleZ()
        error= current_reading-self.goal
        if abs(current_reading-self.goal)<1:
        #got there stop moving

        else:
            power= error*self.kp
            power = max(-.5, min(.5,power))
            print(f"current reading:{current_reading} power:{power}")
            self.drivetrain.arcadeDrive(power,0)

