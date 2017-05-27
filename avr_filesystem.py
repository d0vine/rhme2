# import serial
import arduino
import hashpumpy
import time

MAGIC_SLEEP_TIME = 2

print('[ ] Initializing...')
nano = arduino.ArduinoDevice()
time.sleep(MAGIC_SLEEP_TIME) # magic!
print('[+] Task initialized.')
nano.recv()
# print(nano.recv().decode('utf-8').replace('\\r\\n', '\r\n'))
time.sleep(MAGIC_SLEEP_TIME)

# 1 because 0-length key doesn't make sense; 16 is a wild guess, but worked :D
print('[ ] Starting the brute-force process...')
for i in range(1, 16):
    token, data = hashpumpy.hashpump("96103df3b928d9edc5a103d690639c94628824f5", "cat.txt", ":passwd", i)
    request = token.encode('utf-8') + b'#' + data
    print('\r[?] Key length {}, token "{}"...'.format(i, token))
    nano.send_line(request)
    time.sleep(MAGIC_SLEEP_TIME)
    data = nano.recv()
    
    if b"FLAG" in data:
        print('[+] Flag found! Output below:')
        print(data.decode('utf-8').replace('\\r\\n', '\r\n'))
        nano.cleanup()
        exit(0)
    
    time.sleep(MAGIC_SLEEP_TIME)
