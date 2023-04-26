
import wpilib

from drivestraight import Drivestraight
from gyroturn import GyroTurn
from drivetrain import Drivetrain

    class RobotContainer:

        def __init__(self):
            self.controller = wpilib.Joystick
            self.drivetrain=Drivetrain()
            self.chooser = wpilib.SendableChooser()
            self._configure()
        def _configure(self):
            self.chooser.setDefaultOption("Go Streaight", DriveStraight(self.drivetrain,2))
            self.chooser.addOption("Turn 90", GyroTurn(self.drivetrain,90))
            wpilib.SmartDashboard.putData(self.chooser)


        def get_autonomous(self):
            return self.chooser.getSelected()


