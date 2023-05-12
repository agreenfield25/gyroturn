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
        arcadeDrive.assert_called_once()

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


def test_averageDistanceMeter(drivetrain: Drivetrain, monkeypatch: MonkeyPatch):
        #setup

        def mock_getRightDistanceMeter(self):
                return 2.0
        def mock_getleftDistanceMeter(self):
                return 3.0

        monkeypatch.setattr(Drivetrain,"getLeftDistanceMeter",mock_getleftDistanceMeter)
        monkeypatch.setattr(Drivetrain, "getrightDistanceMeter", mock_getRightDistanceMeter)
        #Action
        dist=drivetrain.averageDistanceMeter()


