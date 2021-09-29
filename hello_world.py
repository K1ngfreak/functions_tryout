def helloWorld(y):
    x = 0
    for i in range(0,y):
        x = x + 1
        print(str(x) + '. ' + 'Hello World!')

g = int(input('aantal: '))

helloWorld(g)