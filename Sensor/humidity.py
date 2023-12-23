import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11

GPIO_PIN = 17

hum, temp = Adafruit_DHT.read(DHT_SENSOR, GPIO_PIN)


def environmental_sensor(hum: float, temp: float) -> List:
    while true:
        try:
            if hum is not None and temp is not None:
                print(list("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temp, hum)))
                break
        except Exception as e:
            if "Failed to retrieve data" in str(e):
                print("Failed to retrieve data from humidity sensor")
                continue
            else:
                raise Exception("Failed to retrieve data from humidity sensor")
