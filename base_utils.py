#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import json
import requests
from settings import HEADERS


def time_use(fn, *args, **kwargs):

    def f(*args, **kwargs):
        s = time.time()
        result = fn(*args, **kwargs)
        e = time.time()
        print e-s
        return result
    return f


def valid_encode(code):
    try:
        code = str(code)
    except UnicodeEncodeError:
        code = code.encode('utf-8')
    return code


class BaiduApiResponse(object):

    def __init__(self, **kwargs):
        err_num = kwargs.get('errNum', None)
        err_msg = kwargs.get('errMsg', None)
        data = kwargs.get('retData') or kwargs

        self.content = None
        self.error = {}

        # 成语接口返回值例外处理
        if err_num is None or err_msg is None:
            err_num, err_msg = 0, 'success'

        if err_num == 0 and err_msg == 'success':
            self.content = data

        else:
            self.error = {
                'err_num': err_num,
                'err_msg': err_msg
            }

    @property
    def is_success(self):
        return self.content is not None

    def print_info(self):
        if self.is_success:
            c = self.content
            print 'print_info' + '*'*32
            print c
        else:
            print 'Error: %s' % self.error.get('err_msg')


@time_use
def get_info(url, data=None):
    # valid_encode(url)
    # import urllib
    # url = urllib.quote(url)
    print url
    resp = requests.get(url, headers=HEADERS)
    content = json.loads(resp.content)

    result = BaiduApiResponse(**content)
    return result
