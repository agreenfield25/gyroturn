import pytest
from pytest import MonkeyPatch
from unittest.mock import MagicMock
from drivetrain import Drivetrain


@pytest.fixture
def drivetrain()->Drivetrain:
        drive = Drivetrain()
        drive.leftEncoder=MagicMock()
        drive.rightEncoder=MagicMock()
        drive.left_motor=MagicMock()
        drive.right_motor=MagicMock()
        drive.drive=MagicMock()
        drive.gyro=MagicMock()
        return drive

def test_arcadeDrive(drivetrain: Drivetrain) ->None:

        #setup
        #drivetrain=Drivetrain()
        #drivetrain.drive=MagicMock()
        arcadeDrive=drivetrain.drive.arcadeDrive


        #action
        drivetrain.drive.arcadeDrive(0.2,0.3)

        #Assert
        arcadeDrive.assert_called_once_with(0.2,0.3)

def test_resetencoders(drivetrain: Drivetrain)->None:
        #setup
        #drivetrain=Drivetrain()
        #drivetrain.rightEncoder=MagicMock()
        #drivetrain.leftEncoder=MagicMock()
        leftreset=drivetrain.leftEncoder.reset
        rightreset=drivetrain.rightEncoder.reset

        #action
        drivetrain.resetEncoders()
        # Assert
        leftreset.assert_called_once()
        rightreset.assert_called_once()

@pytest.mark.parametrize(('left_distance', 'right_distance', 'output'),(
        (2,3,2.5),
        (5,8,6.5),
        (4,0,2),
        (3,3,3),
        (-2,1,-0.5)
))
def test_averageDistanceMeter(drivetrain: Drivetrain, monkeypatch: MonkeyPatch,\
                              left_distance,right_distance,output):
        #setup

        def mock_getRightDistanceMeter(self):
                return right_distance
        def mock_getleftDistanceMeter(self):
                return left_distance

        monkeypatch.setattr(Drivetrain,"getLeftDistanceMeter",mock_getleftDistanceMeter)
        monkeypatch.setattr(Drivetrain, "getRightDistanceMeter", mock_getRightDistanceMeter)
        #Action
        dist=drivetrain.averageDistanceMeter()


        assert dist(2.0+3.0)/2


