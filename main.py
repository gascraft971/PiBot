import RPi.GPIO as GPIO
from classes import Robot
import json

if __name__ == "__main__":
	with open("config.json") as configFile:
		config = json.load(configFile)

	robot = Robot.Robot(GPIO.BCM, config)