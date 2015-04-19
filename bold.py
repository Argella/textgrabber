from sys import argv 

script, url = argv 

def getbold(url): #gets <strong> strings in an html document
    import urllib2
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    count = 0
    i = 0
    j = 0
    infile = opener.open(url)
    s = infile.read()
    while not ("PE html" in n):
        i = s.find("<strong>", i) + 8
        n = ""
        while s[i] != '<' and i >= 0:
            n += s[i]
            i+=1
        j = s.find("<span style=\"text-decoration: underline;\">", i, s.find("<strong>", i)) + 42
        if j == 41:
            j = i + 8
        k = ""
        while s[j] != '<' and j >= 0:
            k += s[j]
            j+=1
        print n + "--" + k


    




