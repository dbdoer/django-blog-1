#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 19-7-2 下午3:02
# @Author  : Hubery
# @File    : crawler.py
# @Software: PyCharm

import logging
from lxml import etree
from hot.helper import get_text


def crawler_wei_bo():
    """
    爬取微博热榜
    :return:
    """
    url = 'https://s.weibo.com/top/summary?cate=realtimehot'
    response_html = get_text(url)
    content_list = []
    try:
        tree = etree.HTML(response_html.text)
        tr_list = tree.xpath('//table/tbody/tr')[1:]
        for tr in tr_list:
            # index = tr.xpath('./td[1]/text()')[0]
            title = tr.xpath('./td[2]/a/text()')[0]
            href = 'https://s.weibo.com%s' % tr.xpath('./td[2]/a/@href')[0]
            content_list.append({'title': title, 'href': href})
    except Exception as e:
        logging.exception(e)
    return {'hot_name': '新浪微博', 'content': content_list}


def crawler_zhi_hu():
    """
    获取知乎热榜
    :return:
    """
    url = 'https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true'
    headers = {
        'path': '/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true',
        'x-api-version': '3.0.76',
        'x-requested-with': 'fetch',
    }
    content_list = []
    try:
        response_html = get_text(url, options=headers)
        print(response_html.json())
        data_list = response_html.json().get('data', '')
        # print(data_list)
        if data_list:
            for data in data_list:
                title = data.get('target').get('title_area').get('text', '')
                href = data.get('target').get('link').get('url', '')
                content_list.append({'title': title, 'href': href})
    except Exception as e:
        logging.exception(e)
    return {'hot_name': '知乎热榜', 'content': content_list}


def crawler_v2ex():
    """
    爬取v2ex热榜
    :return:
    """
    url = 'https://www.v2ex.com/?tab=hot'
    headers = {
        'authority': 'www.v2ex.com',
        'referer': 'https://www.v2ex.com/'
    }
    response_html = get_text(url, options=headers)
    content_list = []
    try:
        tree = etree.HTML(response_html.text)
        span_list = tree.xpath("//div[@class='box']/div[@class='cell item']/table/tr/td[3]/span[1]")
        for span in span_list:
            title = span.xpath('./a/text()')[0]
            href = 'https://www.v2ex.com%s' % span.xpath('./a/@href')[0]
            content_list.append({'title': title, 'href': href})
    except Exception as e:
        logging.exception(e)
    return {'hot_name': 'V2EX', 'content': content_list}


def crawler_tie_ba():
    """
    获取贴吧热榜
    :return:
    """
    url = 'http://tieba.baidu.com/hottopic/browse/topicList'
    content_list = []
    try:
        response_html = get_text(url=url)
        req_json = response_html.json()
        for i in req_json.get('data').get('bang_topic').get('topic_list'):
            title = i.get('topic_name')
            href = i.get('topic_url').replace('amp;', '')
            content_list.append({'title': title, 'href': href})
    except Exception as e:
        logging.exception(e)
    return {'hot_name': '贴吧', 'content': content_list}


def crawler_dou_ban():
    """
    豆瓣讨论精选
    :return:
    """
    url = 'https://www.douban.com/group/explore'
    headers = {
        'Host': 'www.douban.com',
        'Referer': 'https://www.douban.com/group/explore'
    }
    response_html = get_text(url, options=headers)
    content_list = []
    try:
        tree = etree.HTML(response_html.text)
        h3_list = tree.xpath("//div[@class='channel-item']/div[@class='bd']/h3")
        for h3 in h3_list:
            title = h3.xpath('./a/text()')[0]
            href = h3.xpath('./a/@href')[0]
            content_list.append({'title': title, 'href': href})
    except Exception as e:
        logging.exception(e)
    return {'hot_name': '豆瓣', 'content': content_list}


def crawler_tian_ya():
    """
    获取天涯热榜贴
    :return:
    """
    url = 'http://bbs.tianya.cn/hotArticle.jsp'
    headers = {
        'Host': 'bbs.tianya.cn'
    }
    response_html = get_text(url, options=headers)
    content_list = []
    try:
        tree = etree.HTML(response_html.text)
        # print(response_html)
        tbody_list = tree.xpath("//div[@class='mt5']/table/tbody")[1:]
        for tbody in tbody_list:
            for tr in tbody.xpath('./tr'):
                title = tr.xpath("./td[@class='td-title']/a/text()")[0]
                href = 'http://bbs.tianya.cn' + tr.xpath("./td[@class='td-title']/a/@href")[0]
                content_list.append({'title': title, 'href': href})
    except Exception as e:
        logging.exception(e)
    return {'hot_name': '天涯', 'content': content_list}


def crawler_github():
    """
    获取github 热榜
    :return:
    """
    url = 'https://github.com/trending'
    headers = {
        'Host': 'github.com',
        'Referer': 'https://github.com/explore'
    }
    content_list = []
    try:
        response_html = get_text(url, options=headers)
        tree = etree.HTML(response_html.text)
        article_list = tree.xpath("//article[@class='Box-row']")
        print(article_list.__len__())
        for article in article_list:
            title = article.xpath('string(./h1/a)').strip()
            href = 'https://github.com/%s' % article.xpath('./h1/a/@href')[0]
            describe = article.xpath('string(./p)').strip()
            content_list.append({'title':'%s---%s' % (title, describe), 'href': href})
    except Exception as e:
        logging.exception(e)
    return {'hot_name': 'GitHub', 'content': content_list}


def crawler_wang_yi():
    """
    爬取网易云音乐榜单
    :return:
    """
    url = 'https://music.163.com/discover/toplist?id=19723756'
    headers = {
        'authority': 'music.163.com',
        'referer': 'https://music.163.com/',

    }
    content_list = []
    try:
        response_html = get_text(url, options=headers)
        tree = etree.HTML(response_html.text)
        ul_list = tree.xpath('//div[@id="song-list-pre-cache"]/ul[@class="f-hide"]/li')
        for li in ul_list:
            title = li.xpath('./a/text()')[0]
            href = 'https://music.163.com/#%s' % li.xpath('./a/@href')[0]
            content_list.append({'title': title, 'href': href})
    except Exception as e:
        logging.exception(e)
    return {'hot_name': '云音乐飙升榜', 'content': content_list}


if __name__ == '__main__':
    pass
    # a = crawler_wei_bo()
    # print(a)
    c = crawler_zhi_hu()
    print(c)
    # get_v2ex()
    # get_tieba()
    # e = crawler_dou_ban()
    # print(e)
    # crawler_tian_ya()
    # d = crawler_github()
    # print(d)
    # c = crawler_zhi_hu()
    # print(c)
    # crawler_wang_yi()