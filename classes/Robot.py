from typing import Any
import RPi.GPIO as GPIO

class Robot:
	"""
	Main class for the robot
	Structure:
	
	__init__ -> Initialises GPIO mode and robot options
	setup -> Setups GPIO pins
	"""

	def __init__(self, GPIO_type: Any, pins) -> None:
		GPIO.setmode(GPIO_type)
