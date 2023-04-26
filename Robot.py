import wpilib

from wpilib import TimedRobot
from robotcontainer import RobotContainer

class MyRobot(TimedRobot):

    def robotInit(self):
        self.container = RobotContaier()

    def autonomousInit(self) -> None:

        pass

    def autonomousPeriodic(self) -> None:

        pass

    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self) -> None:
        pass





