import urllib.request

mypackage = 'motd'
myversion = '1.0'

url = 'https://github.com/dbarbi/motd/motd.db'
motdfile = urllib.request.urlopen
for line in file:
    decoded_line = line.decode("utf-8")
    package, valid_versions, message = decoded_line.split()

    if package == mypackage and check_valid_version(myversion, valid_versions):
        print (message)


def check_valid_version(my, versionrange):
    if versionrange.beginswith("<="):
        lowerbound = -1
        upperbound = toint(versionrange.replace("<=", "").strip())
    if versionrange.beginswith("<"):
        lowerbound = -1
        upperbound = toint(versionrange.replace("<", "").strip()) - 1
    elif versionrange.beginswith(">="):
        lowerbound = toint(versionrange.replace(">=", "").strip()) + 1
        upperbound = 1000000000
    elif versionrange.beginswith(">"):
        lowerbound = toint(versionrange.replace(">", "").strip())
        upperbound = 1000000000
    else:
        upperbound = lowerbound = toint(versionrange.replace(">", "").replace("<", "").replace("=", "").strip())

    testnumber = toint(my)
    if testnumber > lowerbound and testnumber < upperbound:
        return True
    else:
        return False


def toint(versionstring):
    versionparts=[]
    versionparts = versionstring.split(".")
    if len(versionparts) == 1:
        versionparts.append("0")
    if len(versionparts) == 2:
        versionparts.append("0")
    number = int(versionparts[2]) + int(versionparts[1])*1000 + int(versionparts[0])*1000000
    return number

