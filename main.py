# Quadruped robot v1 Codename: Tektite
#
# Leg order LF, RR, RF, LR     forward motion works diagonally ie LF and RR, and RF and LR
# LF lift, LF forward, LF drop, RF backward/LR backward, RR lift, RR forward, RR drop, RF lift, RF drop etc
# Return to zero  ... 'Rest' position
#
# (S)houlder, (E)lbow, (W)rist
# 012 LF
# 456 LR
# 89 10 RF
# 12 13 14 RR
# IDs:
s_LF = 0
w_LF = 2
e_LF = 1
s_LR = 4
w_LR = 6
e_LR = 5
s_RF = 8
w_RF = 10
e_RF = 9
s_RR = 12
w_RR = 14
e_RR = 13

import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

# Rest Variables
#L_rest = 90
#LR_rest = 140
#LF_rest = 50
#R_rest = 70
#RR_rest = 70
#RF_rest = 130
s_LF_rest = 130
w_LF_rest = 90
e_LF_rest = 110
s_LR_rest = 150
w_LR_rest = 50
e_LR_rest = 90
s_RF_rest = 90
w_RF_rest = 90
e_RF_rest = 90
s_RR_rest = 90
w_RR_rest = 90
e_RR_rest = 90


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
    if str(shoulder) == 's_LF':
        kit.servo[s_LF].angle = 40
    if str(shoulder) == 'e_LF':
        kit.servo[e_LF].angle = 40
    if str(shoulder) == 'w_LF':
        kit.servo[w_LF].angle = 40
    if str(shoulder) == 's_LR':
        kit.servo[s_LR].angle = 40
    if str(shoulder) == 'e_LR':
        kit.servo[e_LR].angle = 40
    if str(shoulder) == 'w_LR':
        kit.servo[w_LR].angle = 40
    if str(shoulder) == 's_RF':
        kit.servo[s_RF].angle = 120
    if str(shoulder) == 'e_RF':
        kit.servo[e_RF].angle = 120
    if str(shoulder) == 'w_RF':
        kit.servo[w_RF].angle = 120
    if str(shoulder) == 's_RR':
        kit.servo[s_RR].angle = 120
    if str(shoulder) == 'e_RR':
        kit.servo[e_RR].angle = 120
    if str(shoulder) == 'w_RR':
        kit.servo[w_RR].angle = 120


def pull(shoulder):
    var = shoulder == str(shoulder)
    if str(shoulder) == 's_LF':
        kit.servo[s_LF].angle = 40
    if str(shoulder) == 'e_LF':
        kit.servo[e_LF].angle = 40
    if str(shoulder) == 'w_LF':
        kit.servo[w_LF].angle = 40
    if str(shoulder) == 's_LR':
        kit.servo[s_LR].angle = 40
    if str(shoulder) == 'e_LR':
        kit.servo[e_LR].angle = 40
    if str(shoulder) == 'w_LR':
        kit.servo[w_LR].angle = 40
    if str(shoulder) == 's_RF':
        kit.servo[s_RF].angle = 120
    if str(shoulder) == 'e_RF':
        kit.servo[e_RF].angle = 120
    if str(shoulder) == 'w_RF':
        kit.servo[w_RF].angle = 120
    if str(shoulder) == 's_RR':
        kit.servo[s_RR].angle = 120
    if str(shoulder) == 'e_RR':
        kit.servo[e_RR].angle = 120
    if str(shoulder) == 'w_RR':
        kit.servo[w_RR].angle = 120


"""
def lift(leg):
    if str(leg) == "LF":
        kit.servo[LF].angle = 90
    if str(leg) == 'RF':
        kit.servo[RF].angle = 90
    if str(leg) == 'LR':
        kit.servo[LR].angle = 90
    if str(leg) == 'RR':
        kit.servo[RR].angle = 90
"""
"""
def drop(leg):
    if str(leg) == "LF":  # down
        kit.servo[LF].angle = 30
    if str(leg) == 'RF':  # up
        kit.servo[RF].angle = 170
    if str(leg) == 'LR':  # up
        kit.servo[LR].angle = 170
    if str(leg) == 'RR':  # down
        kit.servo[RR].angle = 30
"""

def rest(limb):
    limb == str(limb)
    if str(limb) == "s_LF":
        kit.servo[s_LF].angle = s_LF_rest
    if str(limb) == "e_LF":
        kit.servo[e_LF].angle = e_LF_rest
    if str(limb) == "w_LF":
        kit.servo[w_LF].angle = w_LF_rest
    if str(limb) == 's_RF':
        kit.servo[s_RF].angle = s_RF_rest
    if str(limb) == 'e_RF':
        kit.servo[e_RF].angle = e_RF_rest
    if str(limb) == 'w_RF':
        kit.servo[w_RF].angle = w_RF_rest
    if str(limb) == 's_LR':
        kit.servo[s_LR].angle = s_LR_rest
    if str(limb) == 'e_LR':
        kit.servo[e_LR].angle = e_LR_rest
    if str(limb) == 'w_LR':
        kit.servo[w_LR].angle = w_LR_rest
    if str(limb) == 's_RR':
        kit.servo[s_RR].angle = s_RR_rest
    if str(limb) == 'e_RR':
        kit.servo[e_RR].angle = e_RR_rest
    if str(limb) == 'w_RR':
        kit.servo[w_RR].angle = w_RR_rest


def full_rest():
    rest('s_LF')
    rest('e_LF')
    rest('w_LF')
    rest('s_RR')
    rest('e_RR')
    rest('w_RR')
    rest('s_LR')
    rest('e_LR')
    rest('w_LR')
    rest('s_RF')
    rest('e_RF')
    rest('w_RF')


# Alert
'''
def alert():
    full_rest()
    pull('w_LF')
    pull('w_RR')
    pull('w_RF')
    pull('w_LR')
'''

# Move
'''
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
'''
w_RF = 90
# end