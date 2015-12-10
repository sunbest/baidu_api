#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import json
import requests
from settings import HEADERS


def time_use(fn, *args, **kwargs):

    def f(*args, **kwargs):
        s = time.time()
        fn(*args, **kwargs)
        e = time.time()
        print e-s
    return f


class BaiduApiResponse(object):

    def __init__(self, **kwargs):
        err_num = kwargs.get('errNum')
        err_msg = kwargs.get('errMsg')
        data = kwargs.get('retData')

        self.content = None
        self.error = {}

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
            print c
        else:
            print 'Error: %s'% self.error.get('err_msg')


@time_use
def get_info(url):
    resp = requests.get(url, headers=HEADERS)
    content = json.loads(resp.content)
    result = BaiduApiResponse(**content)
    result.print_info()
    return result