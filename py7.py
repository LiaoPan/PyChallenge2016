import re,zipfile

num = '90052'
reg = r'Next nothing is (\d+)'
f = zipfile.ZipFile("channel.zip")
o = []
# while True:
#     try:
#         num = re.search(reg,f.read("%s.txt"%num)).group(1)
#         print num
#     except:
#         break
#
#     o.append(f.getinfo("%s.txt"%num).comment)
#
# print "".join(o)

import urllib, zipfile, re, collections

o, n, f = [], "90052", "%s.txt"
nnr = "Next nothing is (\d+)"

# Download the ZIP file from http://www.pythonchallenge.com/pc/def/channel.zip

file = zipfile.ZipFile("channel.zip")

while True:
    try:
        n = re.search(nnr, file.read(f % n)).group(1)
    except:
        print file.read(f % n)
        break

    o.append(file.getinfo(f % n).comment)

print "".join(o)