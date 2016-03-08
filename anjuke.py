# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import sys


def load_page(url):
    return urllib.urlopen(url).read()


def get_jjr_info(page):
    context = load_page(url="http://shanghai.anjuke.com/tycoon/p%d/" % page)
    print '正在获取第%d页' % page
    soup = BeautifulSoup(context)
    anjuke_jjr = '第%d页' % page + '\n'
    for jjr_info in soup.findAll('div', {'class': "jjr-info"}):
        jjr_name_tag = jjr_info.find('a')
        if jjr_name_tag is not None:
            jjr_name = jjr_name_tag.attrs['title']
        jjr_tel_tag = jjr_info.find('span')
        if jjr_tel_tag is not None:
            jjr_tel = jjr_tel_tag.text
        jjr_addr_tag = jjr_info.find('address')
        if jjr_addr_tag is not None:
            _jjr_addr = jjr_addr_tag.text.split()   # 将文本分割为数组
            if _jjr_addr == []:
                jjr_empl = ''
                jjr_addr = ''
            else:
                jjr_empl = _jjr_addr[0]
                if len(_jjr_addr) == 2:
                    jjr_addr = _jjr_addr[1]
                else:
                    jjr_addr = ''

        anjuke_jjr += '姓名：' + jjr_name + '  tel：' + jjr_tel + '  公司：' + jjr_empl + '  地址：' + jjr_addr + '\n'
    return anjuke_jjr


def save_info(content):
    filename = 'anjuke_jjr.txt'
    f = open(filename, 'a')
    print u'正在把信息存到文本'
    f.write(content.encode('utf-8'))
    print u'保存成功'


def download(start, end):
    for x in xrange(start, end):
        save_info(get_jjr_info(x))

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    download(1, 51)    # 修改页码范围



