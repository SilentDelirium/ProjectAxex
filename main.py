# Quadruped robot v1
#
# Leg order LF, RR, RF, LR     forward motion works diagonally ie LF and RR, and RF and LR
# LF lift, LF forward, LF drop, RF backward/LR backward, RR lift, RR forward, RR drop, RF lift, RF drop etc
# Return to zero  ... 'Rest' position

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# import time
# from adafruit_servokit import ServoKit


# kit = ServoKit(channels=16)


# kit.servo[0].angle = 180
# kit.continuous_servo[0].throttle = 1
# time.sleep(1)
# kit.continuous_servo[0].throttle = 1
# time.sleep(1)
# kit.servo[0].angle = 0
# kit.continuous_servo[0].throttle = 0
# time.sleep(1)


def push(leg):
    var = leg == str(leg)
    if leg == 'LF':
        print('pushing Left Front leg')
    if str(leg) == 'RF':
        print('pushing Right Front leg')
    if str(leg) == 'LR':
        print('pushing Left Rear leg')
    if str(leg) == 'RR':
        print('pushing Right Rear leg')


def pull(leg):
    var = leg == str(leg)
    if str(leg) == "LF":
        print('pulling Left Front leg')
    if str(leg) == 'RF':
        print('pulling Right Front leg')
    if str(leg) == 'LR':
        print('pulling Left Rear leg')
    if str(leg) == 'RR':
        print('pulling Right Rear leg')


def lift(leg):
    var = leg == str(leg)
    if str(leg) == "LF":
        print('lifting Left Front leg')
    if str(leg) == 'RF':
        print('lifting Right Front leg')
    if str(leg) == 'LR':
        print('lifting Left Rear leg')
    if str(leg) == 'RR':
        print('lifting Right Rear leg')


def drop(leg):
    var = leg == str(leg)
    if str(leg) == "LF":
        print('dropping Left Front leg')
    if str(leg) == 'RF':
        print('dropping Right Front leg')
    if str(leg) == 'LR':
        print('dropping Left Rear leg')
    if str(leg) == 'RR':
        print('dropping Right Rear leg')


def rest(leg):
    var = leg == str(leg)
    if str(leg) == "LF":
        print('resting Left Front leg')
    if str(leg) == 'RF':
        print('resting Right Front leg')
    if str(leg) == 'LR':
        print('resting Left Rear leg')
    if str(leg) == 'RR':
        print('resting Right Rear leg')


def full_rest():
    rest('LF')
    rest('RR')
    rest('LR')
    rest('RF')


# Move
def move(steps):
    if steps == 0:
        print('Moved zero steps.')
    if steps <= 0:
        var = steps == int(steps)
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
        var = steps == int(steps)
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
    lift('LF')
    push('LF')
    pull('LF')
    rest('LF')
    drop('LF')
    lift('RR')
    push('RR')
    pull('RR')
    rest('RR')
    drop('RR')
    lift('LR')
    push('LR')
    pull('LR')
    rest('LR')
    drop('LR')
    lift('RF')
    push('RF')
    pull('RF')
    rest('RF')
    drop('RF')


# add in self check for all correctly zeroed (rested)

self_test()
