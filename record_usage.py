import csv
import psutil
import time
import signal
import sys
import os

filename = "process_snapshot.csv"
stop = False
NUM_CORES = os.cpu_count()

# Handle Ctrl+C gracefully
def signal_handler(sig, frame):
    global stop
    print("\nStopping...")
    stop = True

signal.signal(signal.SIGINT, signal_handler)

# Open file in append mode (create if not exists)
file = open(filename, "w", newline="")
writer = csv.writer(file)

# Write header only if file is empty
if file.tell() == 0:
    writer.writerow(["timestamp", "pid", "name", "cpu_percent", "memory_percent"])

print(f"Recording process snapshots to {filename}... Press Ctrl+C to stop.")

# Prime CPU counters
for proc in psutil.process_iter():
    try:
        proc.cpu_percent(interval=None)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

try:
    while not stop:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == "System Idle Process":
                continue # this is not actually using anything up but shows an amount such that the sum is 100%, so ignore it
            try:
                cpu = proc.cpu_percent(interval=None)/NUM_CORES
                mem = proc.memory_percent()
                writer.writerow([timestamp, proc.info['pid'], proc.info['name'], cpu, mem])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        file.flush()
        time.sleep(1)

finally:
    print("Closing file.")
    file.close()


