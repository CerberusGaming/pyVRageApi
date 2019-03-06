import base64
import datetime
import hmac
import requests
import random
import sys
import urllib.parse

from hashlib import sha1 as SHA1
from io import StringIO


class VRageAPI:
    def __init__(self, url_base: str, api_key: str):
        self.url_base = str(url_base).rstrip("/")
        self._key = api_key

    def _generate_hmac(self, url: str, params: dict = None, date: datetime.datetime = None):
        _hmac = hmac.new(key=base64.b64decode(self._key.encode('utf8')), digestmod=SHA1)
        _buffer = StringIO()

        _nonce = str(random.randint(0, sys.maxsize))

        if date is None:
            date = datetime.datetime.utcnow()
        _date = date.strftime('%a, %d %b %Y %H:%M:%S GMT')

        url = "/vrageremote{}".format(url.replace("/vrageremote", ""))

        if params is not None:
            _params = urllib.parse.urlencode(params, doseq=True)
            _url = "{}?{}".format(url, _params)
        else:
            _url = url

        _buffer.write(url + "\r\n")
        _buffer.write(_nonce + "\r\n")
        _buffer.write(_date + "\r\n")
        _hmac.update(bytes(_buffer.getvalue(), 'utf8'))

        return url, params, _date, "{}:{}".format(_nonce, base64.b64encode(_hmac.digest()).decode('utf8'))

    def do_call(self, url: str, method: str = 'get', params: dict = None, data: str = None):
        if data is not None:
            data = '"{}"'.format(data.replace('"', '\\"'))
        url, params, date, auth = self._generate_hmac(url=url, params=params)
        headers = {
            "Authorization": auth,
            "Date": date
        }
        if method.lower() in ["get", "patch", "post", "delete"]:
            req = getattr(requests, method.lower())
            retr = req(self.url_base + url, headers=headers, params=params, data=data)
            if retr.status_code == 200:
                return retr.json()
            else:
                return None
        else:
            return None
