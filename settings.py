#!/usr/bin/env python
# -*- coding: utf-8 -*-


from settings_local import api_key

# http://apistore.baidu.com/astore/classificationservicelist/38.html?isFree=1
# TODO, 股票信息 http://apistore.baidu.com/apiworks/servicedetail/1626.html

API_URL = {
    # 获取ip信息
    'ip': 'http://apis.baidu.com/apistore/iplookupservice/iplookup?ip={ip}',
    # 获取手机信息
    'tel': 'http://apis.baidu.com/apistore/mobilephoneservice/mobilephone?tel={tel}',  # noqa

    # 通过模糊匹配,获取精确的相匹配城市信息
    'city_list': 'http://apis.baidu.com/apistore/weatherservice/citylist?cityname={city_name}',  # noqa
    # 带历史7天和未来4天的天气
    'recent_weathers': 'http://apis.baidu.com/apistore/weatherservice/recentweathers?cityname={city_name}&?cityid={city_id}',  # noqa
    # 根据城市拼音获取天气信息
    'city_pinyin': 'http://apis.baidu.com/apistore/weatherservice/weather?citypinyin={city_pinyin}',  # noqa
    # 根据城市名称获取天气信息
    'city_name': 'http://apis.baidu.com/apistore/weatherservice/cityname?cityname={city_name}',  # noqa
    # 获取城市信息
    'city_info': 'http://apis.baidu.com/apistore/weatherservice/cityinfo?cityname={city_name}',  # noqa
    # 通过城市id[citycode]获取天气信息
    'city_id': 'http://apis.baidu.com/apistore/weatherservice/cityid?cityid={city_id}',  # noqa

    # identity 身份证
    'identity': 'http://apis.baidu.com/apistore/idservice/id?id={identity}',

    # 笑话
    'joke_text': 'http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text',  # noqa
    'joke_pic': 'http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_pic',

    'joke_text2': 'http://apis.baidu.com/hihelpsme/chinajoke/getjokelist',

    # 成语信息
    'chengyu': 'http://apis.baidu.com/netpopo/idiom/chengyu?appkey=1307ee261de8bbcf83830de89caae73f%keyword={keyword}',  # noqa
    # 历史上的今天
    'today_history': 'http://apis.baidu.com/netpopo/todayhistory/todayhistory?month={month}&day={day}&appkey=1307ee261de8bbcf83830de89caae73f',  # noqa
}

HEADERS = {
     'apikey': api_key
}
