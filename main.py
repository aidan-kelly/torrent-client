import argparse

parser = argparse.ArgumentParser(description='Simple torrent client.')
parser.add_argument("file", help='The torrent file of the file you want to download.')
args = parser.parse_args()

metainfofile = args.file

print("The metainfo file is " + metainfofile)