# prototype1.py
#
# This is the first racecar coding
#

from Panda import *

# create the scene
grassScene()

# create the vehicle
car = jeep()

# set camera
#camera.position = P3(0,5,1)
#camera.hpr = HPR(pi,0,0)
camera.rod(car)


# force constant
fK = slider(label = "Force constant", min = 0, max = 5, init = 2)
# friction constant
fcK = slider(label = "Friction", min = 0, max = 10, init = 0.5)
# centripetal force threshold
thresh = slider(label = "Centripetal threshold", min = 0.01, max = 2, init = 1.5)
# velocity variable
setType(car.vel, P3Type)
#text(format("Velocity: %f", abs(car.vel)*abs(car.vel)))

# driving state
def driving(model, p0 = P3(0,0,0), hpr0 = HPR(0,0,0)):
    # vehicle movement variable
    # steering wheel angle
    a = -0.2 * getX(mouse)
    # the force on the vehicle
    f = fK * getY(mouse)
    # velocity
    #velocity = abs(car.vel)
    velocity = abs(car.vel)*abs(car.vel)
    # friction on vehicle
    fc = -fcK * velocity
    # speed
    s = integral(f - fc)
    # heading
    h = integral(s * -a)
    car.hpr = hpr0 + HPR(h,0,0)
    # velocity
    car.vel = P3C(s,h+pi/2,0)
    # position
    car.position = p0 + integral(car.vel)
    # centripetal force
    cent = abs(velocity*velocity * a)

    # spin out the vehicle
    car.when(cent > thresh, spin)


# drive reaction
def drive(model, var):
    # preserve state
    p = now(model.position)
    hpr = now(model.hpr)

    # drive!
    driving(model, p, hpr)


# spinning state
def spinning(model, p0, hpr0, v0):
    # spinning
    p = p0 + integral(v0 * (1 - localTime / 3))
    model.position = p
    hpr = hpr0 + HPR(integral(20 * (1 - localTime / 3)),0,0)
    model.hpr = hpr

    # drive away
    car.react1(localTimeIs(3), drive)


# spin reaction
def spin(model, var):

    # preserve state
    p = now(model.position)
    hpr = now(model.hpr)
    v = now(model.vel)

    # spin out!
    spinning(model, p, hpr, v)



# go for a drive!
driving(car)

# run loop
start()
