"""
@Author: WING
Date: 2018/5/18
DES: 工具类函数，供视图函数调用
"""
import requests
from bs4 import BeautifulSoup
import urllib.request
import json
import re
import threading
import os


def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Referer': 'http://music.163.com/',
        'Host': 'music.163.com',
        'Accept-Encoding, deflate': 'gzip, deflate'
    }
    try:
        response = requests.get(url, headers=headers)
        html = response.text
        return html
    except:
        print("request error!")
    finally:
        pass


# 主要耗时在IO操作，网络请求延时，数据处理
def getSingerID():
    list = range(7000, 7500)  # 589889  max
    singerIdStr = ''
    for singerIdIndex in list:
        start_url = 'http://music.163.com/artist?id={}'.format(singerIdIndex)
        strHtml = getHtml(start_url)
        soup = BeautifulSoup(strHtml, "html.parser")
        links = soup.find('ul', class_='f-hide').find_all('a')

        if len(links) > 0:
            print(singerIdIndex)
            name = str(soup.select('#artist-name')[0]['title']).split(' ')[0]
            singerIdStr += 'ID:{}  name:{}\n'.format(str(singerIdIndex), name)
            filename = 'C:/Users/Administrator/Desktop/SingerID.txt'
            with open(filename, 'w', encoding='utf-8') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
                f.write(singerIdStr)
                f.close()


def getSingerIdFromFile(path, name):
    singerIDArr = []  # 列表
    try:
        with open(path,'r',encoding='utf-8') as f:
            for line in f.readlines():
                if line.strip() != '':
                    if name in (line.split(' ')[2].split(':')[1]):
                        print(line.split(' ')[0].split(':')[1])
                        singerIDArr.append(line.split(' ')[0].split(':')[1])
                        continue
    finally:
        if f:
            f.close()

    if len(singerIDArr) == 0:
        print("没有找到该歌手的ID")
    return singerIDArr


def getSingerInfo(html, name):
    strHtml = getHtml(html)
    soup = BeautifulSoup(strHtml, "html.parser")
    links = soup.find('ul', class_='f-hide').find_all('a')

    autoDodwnImg(soup, name, 0)
    songIDs = []
    songNames = []

    if len(links) == 0:
        return 0
    for link in links:
        songID = link.get('href').split('=')[-1]
        songName = link.get_text()
        songIDs.append(songID)
        songNames.append(songName)

    return zip(songIDs, songNames)


def autoDodwnImg(soup, name, flag):  # flag 0:singer 1:song
    fileType = ''
    if flag == 0:
        singImg = soup.find('div', class_='g-wrap6').find_all('img')[0].get('src')  # singer
        fileType = 'singers'
    else:
        singImg = soup.find('div', class_='m-lycifo').find_all('img')[0].get('src')  # song
        fileType = 'songs'

    nameEx = 'static/imgs/{}/{}.jpg'.format(fileType, name)
    if 'http' in singImg:
        r = requests.get(singImg)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        # 文件夹是否存在，不存在就创建一个
        if not os.path.exists('static/imgs/{}'.format(fileType)):
            os.makedirs('static/imgs/{}'.format(fileType))
        else:
            pass

        # 文件是否存在不存在则创建
        if not os.path.exists(nameEx):
            with open(nameEx, 'wb') as f:
                f.write(r.content)
                f.close()
                print(nameEx + ' 文件保存成功')
        else:
            pass


def getlyric(songId):
    url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(songId) + '&lv=1&kv=1&tv=-1'
    html = getHtml(url)
    json_obj = json.loads(html)

    initial_lyric = json_obj['lrc']['lyric']
    # regex = re.compile(r'\[.*\]')
    # final_lyric = re.sub(regex,'',initial_lyric).split()

    return initial_lyric

