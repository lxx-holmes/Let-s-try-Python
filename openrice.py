import requests, bs4,random
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
restaurants_list=[]
place=str(input('要搜索哪个区域？请输入简体中文：'))
#在输入框里输入你想搜索的地名，比如红磡、尖沙咀、中环...(请输入中文简体。)

'''-------以下为爬取该区域内的餐厅信息-----------'''
for i in range(2):
    #这里是你想爬取的页数，为了不给服务器增加太大负担，暂设定为两页；可根据自己需要调节。

    url = 'https://www.openrice.com/zh-cn/hongkong/restaurants?where='+str(place.encode(encoding="utf-8")).replace('\'','').replace('b','',1).replace('x','%').replace('\\','')+'&page='+str(i+1)
    #该地点的utf-8 code自动写入网址；自动变更页数。

    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    bs = bs.find_all('div', class_="content-cell-wrapper")
    for item in bs:
        link='openrice.com'+item.find('a')['href']
        name=item.find('a').text.strip().encode('utf-8').decode('utf-8')
        address=item.find('div',class_='icon-info address').find('span').text.strip()
        price=item.find('div',class_='icon-info icon-info-food-price').text.strip()
        good_rate=item.find('span',class_='score score-big highlight').text.strip()
        bad_rate=item.find('span',class_='score highlight').text.strip()
        category=item.find('ul',class_='pois-categoryui-list').find_all('a')
        cate=[]
        for i in range(len(category)):
            cate.append(category[i].text.strip())
        restaurants_list.append([name,link,address,price,good_rate,bad_rate,','.join(cate)])

'''-------以下为写入excel文件-----------'''
import csv
#调用csv模块
with open('C:/Users/Susie X Li/Desktop/{}_restaurants.csv'.format(place), 'a',newline='') as csvfile:
#调用open()函数打开csv文件，传入参数：文件名某地_restaurants、追加模式“a”、newline=''。
    writer = csv.writer(csvfile, dialect='excel')
    header=['餐厅名','链接','地址','价格','好评数','差评数','类别']
    writer.writerow(header)

with open('C:/Users/Susie X Li/Desktop/{}_restaurants.csv'.format(place), 'a', newline='')as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        for restaurant in restaurants_list:
            try:
                writer.writerow(restaurant)   
            except:
                continue

'''-------以下为帮你选餐厅-----------'''
your_cate=str(input('你想吃什么菜？请输入简体中文： '))
to_select=[]
for restaurant in restaurants_list:
    if your_cate in restaurant[6]:
        to_select.append(restaurant)
while True:
    to_eat=random.randint(0,len(to_select)-1)
    url_reviews = 'http://'+to_select[to_eat][1]+'/reviews'
    print('''您选择的餐厅是：{}
地址：{}
价位：{}
好评数vs差评数：{}vs{}
查看该餐厅食评：{}'''.format(to_select[to_eat][0],to_select[to_eat][2],to_select[to_eat][3],to_select[to_eat][4],to_select[to_eat][5],url_reviews))
    decision=str(input('是否选择该餐厅？输入Y选择，输入其他重选： '))
    if decision=='Y':
        break