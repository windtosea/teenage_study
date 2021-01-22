import requests
import time
import re


class TeenageStudy(object):
    def __init__(self, openid, course):
        self.openid = openid
        self.course = course

        self.accessToken = None
        self.cardNo = None
        self.nid = None

    def get_accessToken(self):
        url = 'https://jxtw.h5yunban.cn/jxtw-qndxx/cgi-bin/login/we-chat/callback'
        params = {
            'callback': 'https%3A%2F%2Fjxtw.h5yunban.cn%2Fjxtw-qndxx%2FsignUp.php',
            'scope': 'snsapi_userinfo',
            'appid': 'wxe9a08de52d2723ba',
            'openid': self.openid,  # 用户的openid，必要的参数
            'sign': 'CD8CE7188161BCC08A1D80F9E341B5CB',
            'nickname': '%25E5%25BF%2583%25E5%2590%2591%25E5%25A4%25A7%25E6%25B5%25B7',
            'headimg': 'https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FSY6aCyeNicIyiba94WZkSib9x625a0GQwOIqkgQVOYVeVCdRDaXhpxXFE4VIwhDfdXQMRFeibGAxGR6cKuWU1L0dwA%2F132',
            'time': str(int(time.time())),
            'source': 'common',
            't': str(int(time.time()))
        }
        headers = {
            'Host': 'jxtw.h5yunban.cn',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045435 Mobile Safari/537.36 MMWEBID/2026 MicroMessenger/7.0.21.1800(0x270015D5) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
            'Referer': 'https://wx.yunbanos.cn/wx/oauthInfoCallback?r_uri=https%3A%2F%2Fjxtw.h5yunban.cn%2Fjxtw-qndxx%2Fcgi-bin%2Flogin%2Fwe-chat%2Fcallback%3Fcallback%3Dhttps%253A%252F%252Fjxtw.h5yunban.cn%252Fjxtw-qndxx%252FsignUp.php%26scope%3Dsnsapi_userinfo&source=common&code=03136iml2hTUd640JMnl2v5TGd036imj&state=STATE&appid=wxe9a08de52d2723ba'
        }
        response = requests.get(url=url, params=params, headers=headers)
        self.accessToken = re.findall("\('accessToken', '(.*?)'\)", response.text, re.S)[0]

    def detail(self):
        url = 'https://jxtw.h5yunban.cn/jxtw-qndxx/cgi-bin/user-api/course/last-info'
        params = {
            'accessToken': self.accessToken
        }
        headers = {
            'Host': 'jxtw.h5yunban.cn',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045435 Mobile Safari/537.36 MMWEBID/2026 MicroMessenger/7.0.21.1800(0x270015D5) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
            'Referer': 'https://jxtw.h5yunban.cn/jxtw-qndxx/signUp.php'
        }
        response = requests.get(url=url, params=params, headers=headers)
        result = response.json()['result']
        self.cardNo = result['cardNo']
        self.nid = result['nid']

    def request(self):
        url = 'https://jxtw.h5yunban.cn/jxtw-qndxx/cgi-bin/user-api/course/join'
        params = {
            'accessToken': self.accessToken
        }
        headers = {
            'Host': 'jxtw.h5yunban.cn',
            'Origin': 'https://jxtw.h5yunban.cn',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045435 Mobile Safari/537.36 MMWEBID/2026 MicroMessenger/7.0.21.1800(0x270015D5) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
            'Referer': 'https://jxtw.h5yunban.cn/jxtw-qndxx/signUp.php'
        }
        json = {
            'cardNo': self.cardNo,
            'course': self.course,
            'nid': self.nid,
            'subOrg': None
        }
        response = requests.post(url=url, params=params, headers=headers, json=json)

        print(response.json())

    def start_study(self):
        self.get_accessToken()
        self.detail()
        self.request()

