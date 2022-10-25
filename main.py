#import requests
import sqlite3

import ssl
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from requests.packages.urllib3.util import ssl_
from requests import Session
from bs4 import BeautifulSoup as BS
import random

CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""


class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)

url = "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt"
resp = requests.get(url)
http = str(resp.text).split('n')

session = requests.session()
adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
session.mount("https://", adapter)

class Checker_proxy:
    
    def __init__(self, proxy):
        self.proxy = proxy
        self.proxies = {'http': 'http://'+proxy,
                   'https': 'https://'+proxy
                   }
        self.proxy_ip = self.proxy.split('@')[1].split(':')[0]
        self.proxy_port = self.proxy.split('@')[1].split(':')[1]
        self.proxy_login = self.proxy.split('@')[0].split(':')[0]
        self.proxy_pass = self.proxy.split('@')[0].split(':')[1]
        
        self.session = session
        self.session.proxies = proxies

        self.main(proxy, session)
        ipv_6 = self.check_ipv6()
        speed = self.check_speed(session)
    
    def main(self):
        try:
            r = self.session.request('GET', 'https://ip4.seeip.org/')
            checker_ip = r.text
#            self.check_proxy_api(checker_ip)
            fraud_score = self.check_proxy_req(checker_ip)
            if fraud_score != 0:
                return True
            else:
                return False

        except Exception as e:
            print(e)

    def check_proxy_api(self, proxy_ip, token='3b4qx4nu7KI9BiSnNFOeYsN7sVybkd4H'):
        url = f'https://ipqualityscore.com/api/json/ip/{token}/?strictness=1&allow_public_access_points=false&fast=false&lighter_penalties=true&mobile=true'
        r = self.session.request('GET', url)
        fraud_score = int(r.json()['fraud_score'])
        return fraud_score
    
    def check_speed(session, url='https://www.top10vpn.com/tools/what-is-my-ip/'):
        time_start = time.clock()
        check = self.session.request('GET', url)
        time_end = time.clock()
        time_conn = time_end - time_start
        if time_conn < default_time:
            return True
        else:
            return False
    
    def check_ipv6(self):
        url = 'https://iptools-4.top10vpn.com/ip/?genToken=1'
        headers = {
          'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
          'Connection': 'keep-alive',
          'Origin': 'https://www.top10vpn.com',
          'Referer': 'https://www.top10vpn.com/tools/what-is-my-ip/',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-site',
          'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
          'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Linux"',
          }
        r = self.session.request('GET', url, headers=headers)
        type_proxy = str(r.json()['type'])
        if '6' in type_proxy:
            return True
        else:
            return False

class Black_list:
    
    def __init__(self, lst, octet_count, user_value):
        
        self.black_lst = []
        self.lst = lst
        self.user_value = user_value
        ip_lst = []
        for proxy in self.lst():
            ip_lst.append(proxy_ip = proxy.split('@')[1].split(':')[0])
        self.octet_count = octet_count
        if octet_count != 0:
           self.check_octet(ip_lst)
        
    def check_user_value(self):
        self.black_lst.append(self.user_value)
        for val in self.user_value:
            self.lst.remove(val)
    
    def check_octet(self, ip_lst):
        self.octet_count = self.octet_count - 1
        lst_octets = []
        for ip in ip_lst:
            check_black_lst = False
            for octet in lst_octets:
                
                if ip[::-1].index(octet[::-1])==0:
                    check_black_lst = True
                    self.black_lst.append(ip)
            
            if check_black_lst == False:
                ip_octets = '.'.join(ip.split('.')[::-1][self.octet_count:])
                lst_octets.append(ip_octets)
            
    


