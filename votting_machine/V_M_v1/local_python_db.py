import serial
import os

candidates = ["candidate 1", "candidate 2", "candidate 3"]

for candidate in candidates:
    os.makedirs(f"votes/{candidate}", exist_ok=True)

vote_count = { "candidate 1": 0, "candidate 2": 0, "candidate 3": 0 }

ser = serial.Serial('COM3', 9600)  
print("Waiting for votes...")
while True:
    line = ser.readline().decode('utf-8').strip()
    print(f"Received vote for: {line}")

    if line in candidates:
        vote_count[line] += 1
