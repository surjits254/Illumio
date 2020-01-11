
#check port through the entire range
def checkPort(port, firewallPort):
    rangeIndex = firewallPort.find("-")
    if rangeIndex == -1:
        firewallPort = int(firewallPort)
        return port == firewallPort
    else:
        minBound = int(firewallPort[:rangeIndex])
        maxBound = int(firewallPort[rangeIndex + 1:])
        return minBound <= port and port <= maxBound

