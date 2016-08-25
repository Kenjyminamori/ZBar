import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


import sys


def EWMA(lamb, values, reverse):
    smooth = []
    EWMA_t1 = values[0]

    if (reverse == False):
        EWMA_t1 = values[0]
        for EWMA_0 in range(1, len(values)):
            smooth.append(EWMA_t1 + 0.0);
            EWMA_T = lamb*values[EWMA_0] + (1 -  lamb)*EWMA_t1
            EWMA_t1 = EWMA_T
            #sys.stdout.write('.')

        smooth.append(EWMA_t1 + 0.0);
    else:
        EWMA_t1 = values[len(values) - 1]
        for EWMA_0 in range(len(values) - 1, 0, -1):
            smooth.insert(0, EWMA_t1 + 0.0);
            EWMA_T = lamb * values[EWMA_0] + (1 -  lamb)*EWMA_t1
            EWMA_t1 = EWMA_T
            #sys.stdout.write('.')

        smooth.insert(0, EWMA_t1 + 0.0);
    return smooth


print "opening .. "
lena = Image.open("lena.jpg")
print "converting .. "
lenaAr = np.asarray(lena)

lenaBlur = []
print "processing .. "

b = True
for i in lenaAr:
    b = True != b
    sys.stdout.write('.')
    lenaBlur.append(EWMA(0.75, i, b))

print ""
print "done!"
#    for j in lenaAr:
#        print ()

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
"""
lamb = 0.2

mass = np.arange(0., 30.0, 1)
values = np.random.sample(30)

smooth = []
EWMA_t1 = values[0]

smooth.append(EWMA_t1 + 0.0);

"""
# red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

#plt.plot(mass, values, 'r--', mass, smooth) #, t, t**2, 'bs', t, t**3, 'g^')

#plt.show()

print "converting to img..."
im = Image.fromarray(np.uint8(lenaBlur))

print "let's see!.."
im.show()
im.save("lena-blur.jpg")


