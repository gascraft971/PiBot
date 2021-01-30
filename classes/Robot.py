from typing import Any
import RPi.GPIO as GPIO

class Robot:
	"""
	Main class for the robot
	Structure:
	
	__init__ -> Initialises GPIO mode and robot options
	setup -> Setups GPIO pins
	"""

	def __init__(self, GPIO_type: Any, config: dict) -> None:
		GPIO.setmode(GPIO_type)
		self.config = config
		self.pins = self.config["pins"]
		self.setup()
	
	def setup(self) -> None:
		wheels = self.pins["wheels"]
		for pin in [wheels["right"]["fw"], wheels["right"]["bw"], wheels["left"]["fw"], wheels["left"]["bw"]]:
			GPIO.setup(pin, GPIO.OUT)
