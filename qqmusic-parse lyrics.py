# 直接运行代码就好
import requests
# 引用requests模块
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
#ct=24&qqmusic_ver=1298&remoteplace=txt.yqq.lyric&searchid=104077782190132419&aggr=0&catZhida=1&lossless=0&sem=1&t=7&p=1&n=5&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0
for x in range(5):
    params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'remoteplace':'txt.yqq.lyric',
    'searchid':'104077782190132419',
    'aggr':'0',
    'catZhida':'1',
    'lossless':'0',
    'sem':'1',
    't':'7',
    'p':str(x+1),
    'n':'5',
    'w':'周杰伦',
    'g_tk_new_20200303':'5381',
    'g_tk':'5381',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'    
    }
    # 将参数封装为字典
    res_music = requests.get(url,params=params)
    # 调用get方法，下载这个字典
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['lyric']['list']
    # 一层一层地取字典，获取歌单列表
    for music in list_music:
    # list_music是一个列表，music是它里面的元素
        lyrics=music['content'].replace('\\n','\n')
        print(lyrics)
        print('-----------------')