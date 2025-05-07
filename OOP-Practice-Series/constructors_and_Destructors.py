class Logger:
    def __init__(self):
        print("Logger initialized: Object created.")

    def __del__(self):
        print("Logger finalized: Object destroyed.")

print("Creating Logger object...")
log = Logger()

print("Logger is doing something...")

print("Deleting Logger object...")
del log

import time
time.sleep(1)
