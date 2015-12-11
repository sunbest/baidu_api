#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json


class HumanData(object):
    keys = []
    tran_keys = {}

    def __init__(self, **kwargs):
        kwargs_copy = kwargs.copy()
        kwargs_copy = self.trans(**kwargs_copy)

        for key in self.keys:
            self.__dict__[key] = kwargs_copy.get(key, '')

    def trans(self, **kwargs):
        kwargs_copy = kwargs.copy()
        for k in self.tran_keys.keys():
            if k in kwargs_copy:
                v = kwargs_copy.pop(k)
                kwargs_copy[self.tran_keys[k]] = v
        return kwargs_copy

    def print_info(self):
        for i in self.__dict__:
            print '%s :  %s' % (i, self.__dict__[i])
        print '='*32

    @property
    def json(self):
        return json.dumps(self.dic)

    @property
    def dic(self):
        dic = {}
        for key in self.keys:
            dic[key] = self.__dict__[key]
        return dic


class IP(HumanData):
    """
    ip                // IP地址
    country           // 国家
    province          // 省份 国外的默认值为none
    city              // 城市 国外的默认值为none
    district          // 地区 国外的默认值为none
    carrier           //运营商  特殊IP显示为未知
    """
    keys = ['ip', 'country', 'province', 'city', 'district', 'carrier']


class TelPhone(HumanData):
    """
    phone             // IP地址
    province          // 省份 国外的默认值为none
    city              // 城市 国外的默认值为none
    suit              // 地区 国外的默认值为none
    supplier          //运营商  特殊IP显示为未知
    """
    keys = ['phone', 'province', 'city', 'supplier', 'suit']


class WeatherIndex(HumanData):
    """
        name: "感冒指数",
        code: "gm",
        index: "",
        details: "各项气象条件适宜，发生感冒机率较低。但请避免长期处于空调房间中，以防感冒。",
        otherName: ""
    """
    keys = ['name', 'code', 'index', 'details', 'otherName']


class Weather(HumanData):
    """
        date: "2015-08-03",
        week: "星期一",
        time: '11:00'

        'latitude'
        'longitude'
        'altitude'

        temp: "28℃",
        aqi: "92",
        fengxiang: "无持续风向",
        fengli: "微风级",
        hightemp: "30℃",
        lowtemp: "23℃",
        weather: "阵雨",
        index:[]
    """
    keys = [
        'city', 'cityid', 'pinyin',
        'date', 'week', 'time',
        'latitude', 'longitude', 'altitude',
        'temp', 'hightemp', 'lowtemp',
        'aqi', 'fengxiang', 'fengli',
        'weather', 'index', 'sunrise', 'sunset'
    ]

    tran_keys = {
        'curTemp': 'temp',
        'l_tmp': 'lowtemp',
        'h_tmp': 'heighttemp',
        'WD': 'fengxiang',
        'WS': 'fengli',
        'type': 'weather',
        'citycode': 'cityid'
    }

    def __init__(self, **kwargs):
        kwargs_copy = kwargs.copy()

        index_objs = []
        for i in kwargs_copy.get('index', []):
            index_objs.append(WeatherIndex(**i))
        kwargs_copy.update({'index': index_objs})

        super(Weather, self).__init__(**kwargs_copy)


class WeatherCity(HumanData):
    """
    'province',
    'district',
    'name',
    'pinyin',
    'cityid',
    """
    keys = [
        'province', 'district', 'name', 'pinyin', 'cityid',
    ]

    tran_keys = {
        'province_cn': 'province',
        'district_cn': 'district',
        'name_cn': 'name',
        'name_en': 'pinyin',
        'area_id': 'cityid',
    }


class Identity(HumanData):
    """
    sex:        性别
    birthday:   "M", //M-男，F-女，N-未知
    address:    地址
    """
    keys = ['sex', 'birthday', 'address']


class ChengYu(HumanData):
    """
    name:       名称      "粗枝大叶",
    pinyin:     拼音      "cū  zhī  dà  yè",
    content:    内容      "绘画，画树木粗枝大叶，不用工笔。比喻工作粗糙，不认真细致。",
    comefrom:   出自      "《朱子语类》卷七八：...",
    antonym:    反义词     ["精雕细刻","小心谨慎"],
    thesaurus:  同义词     ["粗心大意"]
    """
    keys = ['name', 'pinyin', 'content', 'comefrom', 'antonym', 'thesaurus']
    tran_keys = {
        'pronounce': 'pinyin'
    }


class Joke(HumanData):
    """
     ct:    时间/单号
     title: 标题
     text:  内容
     type:  类型: 1. text,  2. img
     img:   图片地址
    """
    keys = ['ct', 'text', 'title', 'type', 'img']

    tran_keys = {
        'BillNo': 'ct',
        'JokeTitle': 'title',
        'JokeContent': 'text',
        'Type': 'type',
    }


class TodayHistory(HumanData):
    """
    name: "孙中山受困旧金山",
    year: "1904",
    month: "4",
    day: "6",
    content: "仙人岛扣留所，孙中山曾被关押于此"
    """
    keys = ['name', 'year', 'month', 'day', 'content']

    @property
    def cur_date(self):
        year = int(self.year)
        month = int(self.month)
        day = int(self.day)
        return datetime.date(year=year, month=month, day=day)