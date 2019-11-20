import unicornhathd
from time import sleep
from sys import exit, argv

#prob = 6
prob = int(argv[1])
print(prob)
unicornhathd.brightness(0.8)

for x in range (16):
    for y in range (prob):
        unicornhathd.set_pixel(x,y,0,0,255)
unicornhathd.show()
sleep(8)
unicornhathd.off()
