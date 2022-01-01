# Quadruped robot v1 Codename: Tektite
#
# Leg order LF, RR, RF, LR     forward motion works diagonally ie LF and RR, and RF and LR
# LF lift, LF forward, LF drop, RF backward/LR backward, RR lift, RR forward, RR drop, RF lift, RF drop etc
# Return to zero  ... 'Rest' position
#
# IDs:
L = 0
LR = 1
LF = 2
R = 3
RR = 5
RF = 6

import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

# Rest Variables
L_rest = 90
LR_rest = 140
LF_rest = 50
R_rest = 70
RR_rest = 70
RF_rest = 130


# kit.servo[0].angle = 180
# kit.continuous_servo[0].throttle = 1
# time.sleep(1)
# kit.continuous_servo[0].throttle = 1
# time.sleep(1)
# kit.servo[0].angle = 0
# kit.continuous_servo[0].throttle = 0
# time.sleep(1)


def wait(x):
    for i in range(x):
        time.sleep(0.1)


def push(shoulder):
    var = shoulder == str(shoulder)
    if str(shoulder) == 'L':
        kit.servo[L].angle = 40
    if str(shoulder) == 'R':
        kit.servo[R].angle = 120


def pull(shoulder):
    var = shoulder == str(shoulder)
    if str(shoulder) == "L":
        kit.servo[L].angle = 120
    if str(shoulder) == 'R':
        kit.servo[R].angle = 40


def lift(leg):
    if str(leg) == "LF":
        kit.servo[LF].angle = 90
    if str(leg) == 'RF':
        kit.servo[RF].angle = 90
    if str(leg) == 'LR':
        kit.servo[LR].angle = 90
    if str(leg) == 'RR':
        kit.servo[RR].angle = 90


def drop(leg):
    if str(leg) == "LF":  # down
        kit.servo[LF].angle = 30
    if str(leg) == 'RF':  # up
        kit.servo[RF].angle = 170
    if str(leg) == 'LR':  # up
        kit.servo[LR].angle = 170
    if str(leg) == 'RR':  # down
        kit.servo[RR].angle = 30


def rest(limb):
    limb == str(limb)
    if str(limb) == "LF":
        kit.servo[LF].angle = LF_rest
    if str(limb) == 'RF':
        kit.servo[RF].angle = RF_rest
    if str(limb) == 'LR':
        kit.servo[LR].angle = LR_rest
    if str(limb) == 'RR':
        kit.servo[RR].angle = RR_rest
    if str(limb) == 'L':
        kit.servo[L].angle = L_rest
    if str(limb) == 'R':
        kit.servo[R].angle = R_rest


def full_rest():
    rest('LF')
    rest('RR')
    rest('L')
    rest('LR')
    rest('RF')
    rest('R')


# Alert
def alert():
    drop('LF')
    drop('RR')
    drop('RF')
    drop('LR')


# Move
def move(steps):
    if steps == 0:
        print('Moved zero steps.')
    if steps <= 0:
        steps = abs(steps)
        for i in range(steps):
            push('RR')
            push('LF')
            lift('RF')
            pull('RF')
            drop('RF')
            push('LR')
            push('RF')
            lift('LF')
            pull('LF')
            drop('LF')
    else:
        steps = abs(steps)
        for i in range(steps):
            push('LF')
            drop('LF')
            pull('RF')
            pull('LR')
            lift('RF')
            push('RF')
            drop('RF')
            pull('LF')
            pull('RR')


def self_test():
    full_rest()
    wait(1)
    push('L')
    wait(1)
    full_rest()
    wait(1)
    push('R')
    wait(1)
    full_rest()
    wait(1)
    pull('L')
    wait(1)
    full_rest()
    wait(1)
    pull('R')
    wait(1)
    full_rest()
    wait(1)
    lift('LF')
    wait(1)
    drop('LF')
    wait(1)
    full_rest()
    wait(1)
    lift('RR')
    wait(1)
    drop('RR')
    wait(1)
    full_rest()
    wait(1)
    lift('RF')
    wait(1)
    drop('RF')
    wait(1)
    full_rest()
    wait(1)
    lift('LR')
    wait(1)
    drop('LR')
    wait(1)
    full_rest()

# end