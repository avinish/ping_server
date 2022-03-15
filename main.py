import os,ipaddress
from datetime import date

def get_result_ip (ip) :
    response = os.system("ping -c 1 " + ip)
    if response == 0:
        return True
    else:
        print ("Trying again Ip {}".format(ip))
        response = os.system("ping -c 1 " + ip)
        if response == 0:
            return True
        else :
            print("Trying again Ip {}".format(ip))
            response = os.system("ping -c 1 " + ip)
            if response == 0:
                return True
            else :
                return False

def ping_ip_range (start_ip,number) :
    for i in range (0,number + 1):
        ip_addr = ipaddress.IPv4Address(start_ip) + i
        result = get_result_ip(ip_addr.__str__())
        print ("IP Addr {} result {}".format(ip_addr,result))
        file1.write("{},{}".format(ip_addr,result))
        file1.write("\n")

def create_database() :
    pass

if __name__ == '__main__':
    today = date.today()
    filename = "ping_result-" + today.__str__() + ".csv"
    file1 = open(filename, "w")
    ping_ip_range ("0.0.0.0",10)
    file1.close()

