import wpimath

from drivetrain import Drivetrain

from wpimath.controller import PIDController
from autoroutine import AutoRoutine

class GyroTurn(AutoRoutine):

    def __init__(self, bob: Drivetrain, goal:float):
        self.pid_controller=PIDController(1/120,1/400,0)
        self.drivetrain=bob
        self.goal=goal
        #self.kp=-1/120
        #self.ki=1/2000
        #self.tolerance=1
        #self.total_error=0
        self.pid_controller.setSetpoint(self.goal)
        self.pid_controller.setTolerance(3)
        self.pid_controller.setIntegratorRange(-.2,.2)


    def run(self):
        current_reading=self.drivetrain.getGyroAngleZ()
        power=self.pid_controller.calculate(current_reading)
        #error=current_reading - self.goal
        #self.total_error+=error
        #self.total_error = min(500,max(-500,self.total_error))
        if self.pid_controller.atSetpoint():
            # Got there stop moving
            self.drivetrain.arcadeDrive(0,0)
        else:
            #power = error*self.kp+self.total_error*self.ki
            #power = max(-.5, min(.5, power))
            print(f" {current_reading=} {power=}")
            self.drivetrain.arcadeDrive(power, 0)
