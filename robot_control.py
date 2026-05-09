import serial
import time

# Sesuaikan dengan port USB di Android (biasanya /dev/ttyACM0 atau /dev/ttyUSB0)
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    print("Robot Terhubung!")
except:
    print("Gagal terhubung. Pastikan kabel OTG terpasang.")

def kendali_robot():
    while True:
        perintah = input("Masukkan perintah (w:maju, s:mundur, x:stop): ").lower()
        if perintah == 'w':
            ser.write(b'F') # Forward
        elif perintah == 's':
            ser.write(b'B') # Backward
        elif perintah == 'x':
            ser.write(b'S') # Stop
            break

if __name__ == "__main__":
    kendali_robot()

