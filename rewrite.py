import time

i = 0

while i <= 10:
    time.sleep(1)
    print(f'Hello world {i}', end='\r')
    i += 1