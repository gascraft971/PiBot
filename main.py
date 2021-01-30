import RPi.GPIO as GPIO
from classes import Robot

if __name__ == "__main__":
	robot = Robot(GPIO.BCM)
