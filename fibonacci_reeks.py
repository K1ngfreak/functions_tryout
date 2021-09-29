import time

a = 0
b = 1

while b != 0:
    result = a + b
    print(str(a) + ' + ' + str(b) + ' = ' + str(result))
    a = b
    b = result
    time.sleep(0.25)