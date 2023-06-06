import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins

GPIO_TRIGGER = 18
GPIO_ECHO = 24
ledpin = 12


#Setting the GPIO- GPIO_TRIGGER is a digital output
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
#Setting the GPIO - GPIO_ECHO is an analog input
GPIO.setup(GPIO_ECHO, GPIO.IN)
#Setting LED -ledpin as a digital output
GPIO.setup(ledpin, GPIO.OUT)
#Setting pi_pwm as a Pulse Width Modulator(PWM) with frequency of 1000.
pi_pwm = GPIO.PWM(ledpin,1000)
#Starting the PWM duty cycle
pi_pwm.start(0)

#Starting - set the trigger to low to allow the sensor to settle down
GPIO.output(GPIO_TRIGGER, GPIO.LOW)
time.sleep(2)
	
def distance():
	
	
	#Starting to read, a pulse of 1 nanosecond is required to trigger the sensor.
	GPIO.output(GPIO_TRIGGER, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, GPIO.LOW)
	
	#Obtaining the results
	#This while loop takes the time at which the ECHO is 0.
	while GPIO.input(GPIO_ECHO) ==0:
		start_time = time.time()
	#This while loop records the time when the ECHO is 1.
	while GPIO.input(GPIO_ECHO) == 1:
		end_time = time.time()
		
	# the output is the result between time at ECHO = 1 minus time at ECHO =0.	
	complete_time = end_time - start_time
	#The dist a product which provides a result between 0 and 100 for a distance of 9cm.
	#The dist value needs to be between 0 and 100 as required for the PWM ChangeDutyCycle procedure.
	dist = round(complete_time * 60000, 2)
	print(dist)
	return dist

def pwmled(distance):
		#This function is used to change the Duty Cycle of the signal for the LED, ranging from 0 to 100.
		pi_pwm.ChangeDutyCycle(distance)


try:
		while True:
			#Below we are passing the dist value from the function distance() to the function pwmled().
			pwmled(distance())
			time.sleep(2)
			
			# Pressing CTRL + C, will interupt the program and clean up the GPIO.
except KeyboardInterrupt:
			print("Completed")
			GPIO.cleanup()
