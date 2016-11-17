def tranChar(s):
    if s==" " or s=="\'" or s==".":
        t = s
    elif s=="y":
        t = "a"
    elif s=='z':
        t = 'b'
    else:
        t = chr(ord(s)+2)
    return t

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
str_map = "map"
s = ""
for i in str_map.strip(" "):
    s = s+tranChar(i)

print s

input = str

print "".join(map(lambda x: x.isalpha() and chr((ord(x)+2-ord("a"))%26 + ord("a")) or x, input))