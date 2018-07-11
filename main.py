import argparse

#pip3 install bencode.py
import bencode

#pip3 install requests
import requests

#set up command line args
parser = argparse.ArgumentParser(description='Simple torrent client.')
parser.add_argument("file", help='The torrent file of the file you want to download.')
args = parser.parse_args()

#grab torrent file name from cli
metainfofile = args.file

#output the metainfo file name
print("The metainfo file is " + metainfofile)

#open the file and decode the BEncoded contents
fs = open(metainfofile, 'rb')
torrentData = bencode.decode(fs.read())

#print out the announce link
print(torrentData.get("announce"))