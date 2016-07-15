# ISTS15_Alarm_System
A home alarm system designed to run on a Blue teams network and control a Raspberry Pi sensor.

The alarm control center runs on one of the servers in the Blue teams network. It continually checks to see if the sensor is send it information signifying if it is on. If it recieves the information from the sensor it will send back an acknowledgement. If the sensor recieves that acknowledgement then the LED light on the Raspberry Pi will stay on. If no acknowledgement is recieved, it will turn off.
