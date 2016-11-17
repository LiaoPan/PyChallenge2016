import urllib,pickle

uri = 'http://www.pythonchallenge.com/pc/def/banner.p'
data = urllib.urlopen(uri)
tdata = pickle.load(data)

for i in tdata:
    print "".join([j[1]*j[0] for j in i])
