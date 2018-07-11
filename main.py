#Created by Aidan Kelly.
#Started on July 10, 2018
#A simple CLI BitTorrent Client
import urllib
import argparse
import hashlib

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

#grabs the info dictionary, encodes it and then hashes it. We convert the hash object to a string.
decodedInfo = torrentData.get("info")
bencodedInfo = bencode.encode(decodedInfo)
infoSHA1 = hashlib.sha1(bencodedInfo)

#not sure if i need to decode the infoSHA1.digest()
infoSHA1String = infoSHA1.digest()

#URL encode the hash.
urlEncodedInfo = urllib.parse.quote_plus(infoSHA1String)

print(infoSHA1String)
print(urlEncodedInfo)

#future params for the HTTP get method.
getRequestParams = {}