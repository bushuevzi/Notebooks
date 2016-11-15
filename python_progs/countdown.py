#!/usr/share/anaconda3/bin/python3.5
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 00:56:42 2016

@author: root
"""
########################
# import block
########################

import time, subprocess

########################
# def block
########################

########################
# main block
########################
def main():
    timeLeft = 10
    while timeLeft > 0:
        print(timeLeft)
        time.sleep(1)
        timeLeft = timeLeft - 1
# At the end of the countdown, play a sound file.
    subprocess.Popen(['vlc', './10.mp3'], shell=True)


if __name__ == '__main__':
    main()
