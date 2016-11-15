#!/usr/share/anaconda3/bin/python3.5
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 00:56:42 2016

@author: root
"""
########################
# import block
########################

import docx

########################
# def block
########################

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

########################
# main block
########################
def main():
    pass


if __name__ == '__main__':
    main()
