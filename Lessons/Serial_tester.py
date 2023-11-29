import time
import matplotlib
import serial
from matplotlib import pyplot as plt
plt.style.use('ggplot')
matplotlib.use("TkAgg")

arduino = serial.Serial('/dev/cu.usbserial-210', baudrate=9600, timeout=.1)


def get_data():
    data =""
    while len(data) < 1:
        data = arduino.readline()
    return data


rpms = []

for i in range(50):
    time.sleep(0.1)
    data = get_data()
    msg = data.decode('utf-8')
    error, act, rpm = msg.strip().split(',')
    print(f"Error: {error}, Actual: {act}, RPM: {rpm}")
    rpms.append(float(float(rpm)*2))

plt.plot(rpms)
plt.show()
print(sum(rpms)/len(rpms))