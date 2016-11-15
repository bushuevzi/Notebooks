#!/usr/share/anaconda3/bin/python3.5
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 00:56:42 2016

@author: root
"""
########################
# import block
########################

import threading, time

########################
# def block
########################

def takeANap():
	time.sleep(5)
	print('Wake up!')

########################
# main block
########################
def main():
	print('Start of programm.')
	threadObj = threading.Thread(target=takeANap)
	threadObj.start()
	print('End of programm.')
	input()


if __name__ == '__main__':
    main()
