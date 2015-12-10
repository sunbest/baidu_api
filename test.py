#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

test_ip = '221.232.101.101'
test_phone = '15754301479'
test_city_name = '武汉'


if __name__ == '__main__':
    print 'test_start'
    test_ip = '221.232.101.101'
    ip_info(test_ip)

    test_tel = '15754301479'
    tel_info(test_tel)

    test_city_name = '北京'
    city_list(test_city_name)

    test_city_name = '北京'
    test_city_id = '101010100'
    recent_weathers(test_city_name, test_city_id)

    test_city_pinyin = 'beijing'
    weather_by_pinyin(test_city_pinyin)

    test_city_name = '北京'
    weather_by_city_name(test_city_name)

    test_city_name = '北京'
    city_by_city_name(test_city_name)

    test_city_id = '101010100'
    weather_by_city_id(test_city_id)
