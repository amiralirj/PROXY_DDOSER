import requests
from threading import Timer
from random import choice

def proxy_getter(Rj=True):
    try:
        resp = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=1000&anonymity=elite&ssl=all')
    except :
        print('Problem occurred with getting PROXIES ! CANT CONNECT TO (api.proxyscrape.com) ! PLEASE TRY VPN ')
        return
    r=str(resp.text).split('\n')
    host_url = 'https://example.com'
    pr_list=[]
    for i in r:
        try:
            proxies={'http':'socks5://{}'.format(i[0:-1]),'https':'socks5://{}'.format(i[0:-1])}      
            headers=None
            response = requests.get(host_url, headers=headers, proxies=proxies,timeout=12)
            print(f'Proxy Working {i[0:-1]} ')
            pr_list.append(i[0:-1])
            with open('proxy.txt', 'a+') as f:
                f.write(f'{i[0:-1]}\n')
        except :
            pass
    if Rj:
        Timer(100,proxy_getter).start()
    return pr_list

def delete_line(line):
    with open("proxy.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if not line in i:
                f.write(i)
        f.truncate()

def get_proxy():
    permission=False
    proxy_list=[]
    with open('proxy.txt','r') as f:
        for i in f:
            proxy_list.append(i)
    rnd=choice(proxy_list[-3:-1])
    proxies={'http':'socks5://{}'.format(rnd),'https':'socks5://{}'.format(rnd)}   
    try:
        response = requests.get('https://example.com', headers=None, proxies=proxies,timeout=5) 
        permission=True 
        try:delete_line(rnd)
        except:pass
    except:
        for i in range(20):
            print('proxy not found ! wait ...')
            rnd=choice(proxy_list)
            proxies={'http':'socks5://{}'.format(rnd),'https':'socks5://{}'.format(rnd)}   
            try:
                response = requests.get('https://example.com', headers=None, proxies=proxies,timeout=5) 
                permission=True 
                break
            except:
                try:delete_line(i)
                except:pass
    if not permission : raise PermissionError
    p=(str(rnd)).split(':')
    return  {'hostname':p[0],'port':int(p[1])}
    
