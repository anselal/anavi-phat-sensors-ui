import json
import time
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
# Define the colours red and green
red = (255, 0, 0)
green = (0, 255, 0)

try:
  while True:
    # Take readings from all three sensors
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    # Round the values to one decimal place
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    # Create the message str() converts the value to a string so it can be concatenated
    message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)
    # print(message)

    temperature = {"temperature": t}
    pressure = {"pressure": p}
    humidity = {"humidity": h}

    with open("temperature.json", "w") as output:
      json.dump(temperature, output)

    with open("pressure.json", "w") as output:
      json.dump(pressure, output)

    with open("humidity.json", "w") as output:
      json.dump(humidity, output)

    # if t > 18.3 and t < 26.7:
    #   bg = green
    # else:
    #   bg = red

    # Display the scrolling message
    # sense.show_message(message, scroll_speed=0.05, back_colour=bg)
    time.sleep(30)
except KeyboardInterrupt:
  sense.clear()
