#! /usr/bin/env python

x = 0

if x > 0:
    msg = 'x is positive'
else:
    msg = 'x is nonpositive'

msg # pause point A
del x, msg # clear variables to keep debugger window tidy


# Here we find the greatest common denominator (GCD) of two integers:

num1 = 2 * 3 * 7 * 17 * 19
num2 = 2**3 * 7 * 11 * 13
a = num1
b = num2

while b:
    temp = b
    b = a % b
    a = temp

the_gcd = a
the_gcd # pause point B
del num1, num2, a, b, temp, the_gcd


# Here we use more sophisticated flow control commands for loops:

z = 0

for k in [3, -3, 6, 3, -6]:
    if z < -10:
        break

    z += k

    if z % 2 == 0: # is z even?
        z -= 2
        if z % 6 == 0: # divisible by 6?
            continue

    z = -z

z # pause point C
del z, k


# Rightward drift, version 1:

keep_going = True
seconds = 100000.
msg = None

while keep_going: # you may want to use Control-X to alter 'keep_going' or 'seconds' here.
    if seconds > 60:
        minutes = seconds / 60

        if minutes > 60:
            hours = minutes / 60

            if hours > 24:
                days = hours / 24

                if days > 365.25:
                    years = days / 365.25
                    msg = str(years) + ' years'
                else:
                    msg = str(days) + ' days'
            else:
                msg = str(hours) + ' hours'
        else:
            msg = str(minutes) + ' minutes'
    else:
        msg = str(seconds) + ' seconds'

    msg

msg # pause point D
del keep_going, seconds, msg


# Rightward drift, version 2:

keep_going = True
seconds = 100000.
msg = None

while keep_going: # you may want to use Control-X to alter 'keep_going' or 'seconds' here.
    if seconds <= 60:
        msg = str(seconds) + ' seconds'
        continue

    minutes = seconds / 60
    if minutes <= 60:
        msg = str(minutes) + ' minutes'
        continue

    hours = minutes / 60
    if hours <= 24:
        msg = str(hours) + ' hours'
        continue

    days = hours / 24
    if days <= 365.25:
        msg = str(days) + ' days'
        continue

    years = days / 365.25
    msg = str(years) + ' years'

msg # All done!
