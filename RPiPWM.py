import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
ledpin = 12

#set GPIO direct (IN/OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(ledpin, GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,1000)
pi_pwm.start(0)
# start up the sensor
GPIO.output(GPIO_TRIGGER, GPIO.LOW)
time.sleep(2)
	
def distance():
	
	
	# starting with reading
	GPIO.output(GPIO_TRIGGER, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, GPIO.LOW)
	
	#Obtaining the results
	while GPIO.input(GPIO_ECHO) ==0:
		start_time = time.time()
	
	while GPIO.input(GPIO_ECHO) == 1:
		end_time = time.time()
		
		
	complete_time = end_time - start_time
	dist = round(complete_time * 60000, 2)
	print(dist)
	return dist

def pwmled(distance):
		
		pi_pwm.ChangeDutyCycle(distance)


try:
		while True:
			
			pwmled(distance())
			time.sleep(2)
			
			# Reset by pressing CTRL + C
except KeyboardInterrupt:
			print("Completed")
			GPIO.cleanup()
