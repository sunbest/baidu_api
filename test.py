#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

import json
from base_utils import valid_encode
from utils import *
from human_data import TodayHistory

test_ip = '221.232.101.101'
test_phone = '15754301479'
test_city_name = '武汉'


def valid_month_day(month, day):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return True

    if month in (4, 6, 9, 11) and day < 31:
        return True

    if month == 2 and day < 30:
        return True

    return False


def month_day():
    result = []
    for month in xrange(1, 13):
        for day in xrange(1, 32):
            if valid_month_day(month, day):
                result.append([month, day])
            else:
                continue
    return result


start = 0
per_num = 130
times = 0

json_file_name = 'today_history.json'

# TODO h.a = [h,]


def insert_json(dic):
    f = open(json_file_name, 'r+')
    content = valid_encode(f.read())
    if content:
        content = json.loads(content)
    else:
        content = []
    f.close()

    content.append(dic)

    f = open(json_file_name, 'w')
    f.write(json.dumps(content))
    f.close()

    pass


def history(start, per_num, times):
    m_d = month_day()
    for m, d in m_d[start+per_num*times: per_num]:
        resp = today_history(m, d)
        resp.print_info()
        if resp.is_success:
            datas = resp.content.get('data', [])
            for data in datas:
                insert_json(TodayHistory(**data).dic)
        else:
            print 'Error:  %m - %d' % (m, d)


if __name__ == '__main__':
    print 'test_start'
    # insert_json()

    history(start, per_num, times)
    # test_ip = '221.232.101.101'
    # ip_info(test_ip)
    #
    # test_tel = '15754301479'
    # tel_info(test_tel)
    #
    # test_city_name = '北京'
    # city_list(test_city_name)
    #
    # test_city_name = '北京'
    # test_city_id = '101010100'
    # recent_weathers(test_city_name, test_city_id)
    #
    # test_city_pinyin = 'beijing'
    # weather_by_pinyin(test_city_pinyin)
    #
    # test_city_name = '北京'
    # weather_by_city_name(test_city_name)
    #
    # test_city_name = '北京'
    # city_by_city_name(test_city_name)
    #
    # test_city_id = '101010100'
    # weather_by_city_id(test_city_id)

    # from human_data import TodayHistory, Joke
    # kwargs = {
    #     'name': '1',
    #     'year': '2012',
    #     'month': '2',
    #     'day': '3',
    #     'content': 'xxxx'
    # }
    # t = TodayHistory(**kwargs)
    # t.print_info()
    #
    # joke_kwargs = {
    #     'BillNo': 'ct',
    #     'JokeTitle': 'title',
    #     'JokeContent': 'text',
    #     'Type': 'type',
    # }
    # j = Joke(**joke_kwargs)
    # j.print_info()
