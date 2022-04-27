# Name: [Your Name]
# Date: 4/24/2022
# Project: Countdown Timer using Github
# File: countdownClass --> main.py
# -----------------------------------------------------------------
import time


def timeCountdown(userTime):
    while userTime:
        min, secs = divmod(userTime, 60)

        timer = '{:02d} : {:02d}'.format(min, secs)

        print('\r', timer, end=' ')

        time.sleep(1)

        userTime -= 1

    print('\n Timer Completed')


userTime = input('Please enter the time in seconds: \n')

timeCountdown(int(userTime))

'''The timer countdown function is used to import the userTime parameter. This will take the seconds and translate it 
to a timer to allow the user to countdown. '''
