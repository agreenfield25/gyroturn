
from drivetrain import Drivetrain

class GyroTurn:

    def __init__(self, bob: Drivetrain, goal:float):
        self.drivetrain=bob
        self.goal=goal
        self.kp=-1/25
        self.tolerance=1


    def run(self):
        current_reading=self.drivetrain.getGyroAngleZ()
        error=current_reading - self.goal
        if abs(error)<self.tolerance:
            # Got there stop moving
            self.drivetrain.arcadeDrive(0,0)
        else:
            power = error*self.kp
            power = max(-.5, min(.5, power))
            print(f"current reading: {current_reading} power: {power}")
            self.drivetrain.arcadeDrive(power, 0)
