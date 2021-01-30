import RPi.GPIO as GPIO
from classes import Robot
import json

with open("config.json") as file:
	pins = json.load(file)

if __name__ == "__main__":
	robot = Robot(GPIO.BCM, pins)