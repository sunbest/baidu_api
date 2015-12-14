#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

import json
from base_utils import valid_encode
from utils import *
from human_data import TodayHistory, Joke

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


START = 0
PER_NUM = 130
TIMES = 1

# TODO h.a = [h,]


def insert_json(json_file_name, dic):
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


def history(start, per_num, times, json_file_name='today_history.json'):
    m_d = month_day()
    for m, d in m_d[start+per_num*times: per_num*(times+1)]:
        resp = today_history(m, d)
        resp.print_info()
        if resp.is_success:
            datas = resp.content.get('data', [])
            for data in datas:
                insert_json(json_file_name, TodayHistory(**data).dic)
        else:
            print 'Error:  %m - %d' % (m, d)


def joke_text(json_file_name='joke_text.json', pages=689):
    for page in range(1, pages):
        resp = joke_info('joke_text', page=page)
        if resp.is_success:
            datas = resp.content.get('showapi_res_body', {})
            max_page = datas.get("allPages", 1)
            print 'joke_text == max_page:  ', max_page

            if not datas:
                break
            datas = datas.get("contentlist", [])
            for data in datas:
                insert_json(json_file_name, Joke(**data).dic)


def joke_text2(json_file_name='joke_text2.json', pages=554):
    for page in range(1, pages):
        resp = joke_info('joke_text2', page=page)
        if resp.is_success:
            datas = resp.content.get('res_body', {})

            max_page = datas.get("PageCount", 1)
            print 'joke_text2 == max_page:  ', max_page

            datas = datas.get("JokeList", [])
            for data in datas:
                insert_json(json_file_name, Joke(**data).dic)


if __name__ == '__main__':
    print 'test_start'
    # insert_json()

    # history(START, PER_NUM, TIMES)
    # joke_text()
    joke_text2()

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
