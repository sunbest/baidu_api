#!/usr/bin/env python
# -*- coding: utf-8 -*-
from settings import API_URL
from base_utils import get_info


def ip_info(ip):
    """
    查询IP地址信息
    特殊IP：
    0.0.0.0 和127.0.0.0保留
    10.x.x.x、172.16.x.x～172.31.x.x、192.168.x.x 私有地址，这些地址被大量用于企业内部网络中
    224.0.0.0到239.255.255.255用于多点广播

    :param ip:
    :return:
        BaiduApiResponse:
            content: {
                "ip": "117.89.35.58", //IP地址
                "country": "中国", //国家
                "province": "江苏", //省份 国外的默认值为none
                "city": "南京", //城市  国外的默认值为none
                "district": "鼓楼",// 地区 国外的默认值为none
                "carrier": "中国电信" //运营商  特殊IP显示为未知
            }
    """
    print 'ip', '='*32
    url = API_URL.get('ip').format(ip=ip)
    return get_info(url)


def tel_info(tel):
    """
    查询手机号信息
    :param tel:
    :return:
        BaiduApiResponse:
            content: {
                telString: "15846530170", //手机号码
                province: "黑龙江",    //省份
                carrier: "黑龙江移动"  //运营商
            }
    """
    print 'tel', '='*32
    url = API_URL.get('tel').format(tel=tel)
    return get_info(url)


def city_list(city_name):
    """
    城市名模糊查询天气
    :param city_name:
    :return:
        BaiduApiResponse:
            content: [
                {
                    province_cn: "北京",
                    district_cn: "北京",
                    name_cn: "朝阳",
                    name_en: "chaoyang",
                    area_id: "101010300"
                },
                {
                    province_cn: "辽宁",
                    district_cn: "朝阳",
                    name_cn: "朝阳",
                    name_en: "chaoyang",
                    area_id: "101071201"
                },...
            ]
    """
    print 'city_list', '='*32
    url = API_URL.get('city_list').format(city_name=city_name)
    return get_info(url)


def recent_weathers(city_name, city_id):
    """
    城市名\城市编码精确查询城市几天的天气
    :param city_name:
    :param city_id:
    :return:
        BaiduApiResponse:
            content: {
                city: "北京",
                cityid: "101010100",
                today: {
                    date: "2015-08-03",
                    week: "星期一",
                    curTemp: "28℃",
                    aqi: "92",
                    fengxiang: "无持续风向",
                    fengli: "微风级",
                    hightemp: "30℃",
                    lowtemp: "23℃",
                    type: "阵雨",
                    index: [
                        {
                            name: "感冒指数",
                            code: "gm",
                            index: "",
                            details: "各项气象条件适宜，发生感冒机率较低。但请避免长期处于空调房间中，以防感冒。",
                            otherName: ""
                        },
                        {
                            code: "fs",
                            details: "属中等强度紫外辐射天气，外出时应注意防护，建议涂擦SPF指数高于15，PA+的防晒护肤品。",
                            index: "中等",
                            name: "防晒指数",
                            otherName: ""
                        },
                        {
                            code: "ct",
                            details: "天气炎热，建议着短衫、短裙、短裤、薄型T恤衫等清凉夏季服装。",
                            index: "炎热",
                            name: "穿衣指数",
                            otherName: ""
                        },
                        {
                            code: "yd",
                            details: "有降水，推荐您在室内进行低强度运动；若坚持户外运动，须注意选择避雨防滑并携带雨具。",
                            index: "较不宜",
                            name: "运动指数",
                            otherName: ""
                        },
                        {
                            code: "xc",
                            details: "不宜洗车，未来24小时内有雨，如果在此期间洗车，雨水和路上的泥水可能会再次弄脏您的爱车。",
                            index: "不宜",
                            name: "洗车指数",
                            otherName: ""
                        },
                        {
                            code: "ls",
                            details: "有降水，不适宜晾晒。若需要晾晒，请在室内准备出充足的空间。",
                            index: "不宜",
                            name: "晾晒指数",
                            otherName: ""
                        }
                    ]
                },
                forecast: [
                    {
                        date: "2015-08-04",
                        week: "星期二",
                        fengxiang: "无持续风向",
                        fengli: "微风级",
                        hightemp: "32℃",
                        lowtemp: "23℃",
                        type: "多云"
                    },...共4个
                ],
                history: [
                    {
                        date: "2015-07-31",
                        week: "星期五",
                        aqi: "52",
                        fengxiang: "无持续风向",
                        fengli: "微风级",
                        hightemp: "高温 29℃",
                        lowtemp: "低温 22℃",
                        type: "多云"
                    },...共2个
                ]
            }
    """
    print 'recent_weathers', '='*32
    url = API_URL.get('recent_weathers').format(
        city_name=str(city_name), city_id=str(city_id)
    )
    return get_info(url)


def weather_by_pinyin(city_pinyin):
    """
    城市名拼音查询天气
    :param city_name:
    :return:
        BaiduApiResponse:
            content: {
               city: "北京", //城市
               pinyin: "beijing", //城市拼音
               citycode: "101010100",  //城市编码
               date: "15-02-11", //日期
               time: "11:00", //发布时间
               postCode: "100000", //邮编
               longitude: 116.391, //经度
               latitude: 39.904, //维度
               altitude: "33", //海拔
               weather: "晴",  //天气情况
               temp: "10", //气温
               l_tmp: "-4", //最低气温
               h_tmp: "10", //最高气温
               WD: "无持续风向",	 //风向
               WS: "微风(<10m/h)", //风力
               sunrise: "07:12", //日出时间
               sunset: "17:44" //日落时间
            }
    """
    print 'weather_by_pinyin', '='*32
    url = API_URL.get('city_pinyin').format(city_pinyin=city_pinyin)
    return get_info(url)


def weather_by_city_name(city_name):
    """
    城市名查询天气
    :param city_name:
    :return:
        BaiduApiResponse:
            content: {
               city: "北京", //城市
               pinyin: "beijing", //城市拼音
               citycode: "101010100",  //城市编码
               date: "15-02-11", //日期
               time: "11:00", //发布时间
               postCode: "100000", //邮编
               longitude: 116.391, //经度
               latitude: 39.904, //维度
               altitude: "33", //海拔
               weather: "晴",  //天气情况
               temp: "10", //气温
               l_tmp: "-4", //最低气温
               h_tmp: "10", //最高气温
               WD: "无持续风向",	 //风向
               WS: "微风(<10m/h)", //风力
               sunrise: "07:12", //日出时间
               sunset: "17:44" //日落时间
            }
    """
    print 'weather_by_city_name', '='*32
    url = API_URL.get('city_name').format(city_name=city_name)
    return get_info(url)


def city_by_city_name(city_name):
    """
    城市名查询城市信息
    :param city_name:
    :return:
        BaiduApiResponse:
            content: {
                cityName: "北京",
                provinceName: "北京",
                cityCode: "101010100",  //天气预报城市代码
                zipCode: "100000",      //邮编
                telAreaCode: "010"     //电话区号
            }
    """
    print 'city_by_city_name', '='*32
    url = API_URL.get('city_name').format(city_name=city_name)
    return get_info(url)


def weather_by_city_id(city_id):
    """
    城市编码查询天气信息
    :param city_name:
    :return:
        BaiduApiResponse:
            content: {
               city: "北京", //城市
               pinyin: "beijing", //城市拼音
               citycode: "101010100",  //城市编码
               date: "15-02-11", //日期
               time: "11:00", //发布时间
               postCode: "100000", //邮编
               longitude: 116.391, //经度
               latitude: 39.904, //维度
               altitude: "33", //海拔
               weather: "晴",  //天气情况
               temp: "10", //气温
               l_tmp: "-4", //最低气温
               h_tmp: "10", //最高气温
               WD: "无持续风向",	 //风向
               WS: "微风(<10m/h)", //风力
               sunrise: "07:12", //日出时间
               sunset: "17:44" //日落时间
            }
    """
    print 'weather_by_city_id', '='*32
    url = API_URL.get('city_id').format(city_id=city_id)
    return get_info(url)


def identity_info(identity):
    """
    身份证信息
    :param city_name:
    :return:
        BaiduApiResponse:
            content: {
                "sex": "M", //M-男，F-女，N-未知
                "birthday": "1987-04-20", //出生日期
                "address": "湖北省孝感市汉川市" //身份证归属地 市/县
            }
    """
    print 'identity_info', '='*32
    url = API_URL.get('identity').format(identity=identity)
    return get_info(url)
