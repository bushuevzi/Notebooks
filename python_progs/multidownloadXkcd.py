#!/usr/share/anaconda3/bin/python3.5
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 00:56:42 2016

@author: root
"""
########################
# import block
########################

import requests, os, bs4, threading

########################
# def block
########################

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading page http://xkcd.com/%s...' % (urlNumber))
        res = requests.get('http://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'http:'+comicElem[0].get('src')
            # Download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

########################
# main block
########################
def main():
    os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd
    downloadTreads = []    # a list of all the Thread objects
    for i in range (0,1400, 100): # loops 14 times, creates 14 threads
        downloadTread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
        downloadTreads.append(downloadTread)
        downloadTread.start()

    # Wait for all threads to end.
    for downloadThread in downloadTreads:
        downloadTread.join()
    print('Done.')


if __name__ == '__main__':
    main()
