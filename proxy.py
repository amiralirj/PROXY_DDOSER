import requests
from threading import Timer
from random import choice
def proxy_getter():
    resp = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=1000&anonymity=elite&ssl=all')
    #print(resp.text)
    r=str(resp.text).split('\n')
    host_url = 'https://www.example.org'
    for i in r:
        try:
            proxy=i.split(':')
            proxies={'ip':'{}'.format(proxy[0]),'port':'{}'.format(proxy[1])}      
            headers=None
            response = requests.get(host_url, headers=headers, proxies=proxies,timeout=12)
            print(f'Proxy Working {i} ')
            with open('proxy.txt', 'a+') as f:
                f.write(f'{i[0:-1]}\n')
        except :
            pass
    Timer(100,proxy_getter)
    return


def get_proxy():
    proxy_list=[]
    with open('proxy.txt','r') as f:
        for i in f:
            proxy_list.append(i)
    rnd=choice(proxy_list[-2:-1])
    proxy=rnd.split(':')
    proxies={'ip':'{}'.format(proxy[0]),'port':'{}'.format(proxy[1])} 
    try:
        response = requests.get('https://example.com', headers=None, proxies=proxies,timeout=5)  
    except:
        for i in range(100):
            print('proxy not found ! wait ...')
            rnd=choice(proxy_list)
            proxy=rnd.split(':')
            proxies={'ip':'{}'.format(proxy[0]),'port':'{}'.format(proxy[1])}   
            try:
                response = requests.get('https://example.com', headers=None, proxies=proxies,timeout=5)  
                break
            except:pass       
    p=(str(rnd)).split(':')
    return  {'hostname':p[0],'port':int(p[1])}
    
proxy_getter()