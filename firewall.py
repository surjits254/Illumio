import csv
from ipUtil import checkIP
from portUtil import checkPort

class firewall(object):
    input = {}

    def __init__(self, file):
        # creating ruleset dictionaries
        self.input["inbound"] = {}
        self.input["outbound"] = {}
        self.input["inbound"]["tcp"] = {}
        self.input["inbound"]["udp"] = {}
        self.input["outbound"]["tcp"] = {}
        self.input["outbound"]["udp"] = {}

        datafile = open(file, 'r') #'r' to just read the file
        myreader = csv.reader(datafile)

        for row in myreader:
            direction, protocol, port, ip = row
            port_dict = self.input[direction][protocol]
            if port in port_dict:
              self.input[direction][protocol][port] += [ip]
            else:
              self.input[direction][protocol][port] = [ip]

    #accept input packets for checking validity against ruleset
    def accept_packet(self, direction, protocol, port, ip_address):
        try:
            ports = self.input[direction][protocol]
        except KeyError:
            return False
        for port_val, ips in ports.items():
            if checkPort(port, port_val):
                for ip in ips:
                    if checkIP(ip_address, ip):
                        return True
        return False


