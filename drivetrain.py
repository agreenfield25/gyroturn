import wpilib

from wpilib import Joystick, Spark, Encoder

from wpilib.drive import DifferentialDrive

class Drivetrain:

    def __init__(self):
        self.motor = Spark
        self.drivetrain
        self.controller = Joystick(0)
        self.left_motor = Spark(0)
        self.right_motor = Spark(1)
        self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)
        self.leftEncoder = Encoder(4, 5)
        self.rightEncoder = Encoder(6, 7)


    def move(self, forward, rotate):
        forward = self.controller.getRawAxis(0)
        rotate = self.controller.getRawAxis(1)
        self.drivetrain.arcadeDrive(rotate, forward)

