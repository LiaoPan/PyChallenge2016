import urllib,re,time

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

reg = r"and the next nothing is (\d+)"
num = "8022"

while True:
    try:
        source = urllib.urlopen(uri % num).read()
        # print source
        num = re.search(reg,source).group(1)
        print num
    except:
        break

print "Result is:",num
