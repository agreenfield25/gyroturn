import wpilib

from wpilib import TimedRobot
from robotcontainer import RobotContainer
from drivetrain import Drivetrain

class MyRobot(TimedRobot):

    def robotInit(self):
        self.container = RobotContainer()

    def autonomousInit(self) -> None:
        self.auto=self.container.get_aitonomous()

    def autonomousPeriodic(self) -> None:
        self.auto.run()


    def teleopInit(self) -> None:

        ...

    def teleopPeriodic(self) -> None:
      forward = self.container.controller.getRawAxis(0)
      rotate = self.container.controller.getRawAxis(1)
      self.container.drivetrain.arcadeDrive(rotate,forward)
      print(f"Forward:{forward} Rotate: {rotate}")






