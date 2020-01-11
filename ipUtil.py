
#check ip through the entire ip
def checkIP(ip, firewallIP):
    rangeIndex = firewallIP.find("-")
    if rangeIndex == -1:
        return ip == firewallIP
    else:
        minBound = firewallIP[:rangeIndex]
        minBound = int(minBound.replace(".", ""))
        maxBound = firewallIP[rangeIndex + 1:]
        maxBound = int(maxBound.replace(".", ""))
        ip = int(ip.replace(".", ""))
        return minBound <= ip and ip <= maxBound