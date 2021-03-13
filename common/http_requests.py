import requests
from common.logger import logger


class HTTPRequest(object):

    def request(self, method, url,
                params=None, data=None,
                json=None, headers=None,
                cookies=None):
        method = method.lower()
        if method == 'post':
            if json:
                logger.info("")
                return self.requests.post(url=url, json=json, headers=headers, cookies=cookies)
            else:
                logger.info("")
                return self.requests.post(url=url, data=data, headers=headers, cookies=cookies)
        elif method == 'get':
            logger.info("")
            return self.requests.post(url=url, parmas=params, headers=headers, cookies=cookies)


class HTTPRequest2(object):
    """记录cookies信息，给下一次请求用"""

    def __init__(self):
        self.session = requests.sessions.Session()

    def request(self, method, url,
                params=None, data=None,
                json=None, headers=None,
                cookies=None):
        method = method.lower()
        if method == 'post':
            if json:
                logger.info("")
                return self.session.post(url=url, json=json, headers=headers, cookies=cookies)
            else:
                logger.info("")
                return self.session.post(url=url, data=data, headers=headers, cookies=cookies)
        elif method == 'get':
            logger.info("")
            return self.session.post(url=url, parmas=params, headers=headers, cookies=cookies)
