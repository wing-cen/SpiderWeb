from django.shortcuts import render
import self as self
from django.http import HttpResponse, HttpResponseRedirect
import datetime, json
# from django.views.decorators.csrf import csrf_exempt (1)
from django.shortcuts import render   #CSRF处理2
from django.template.context_processors import csrf #CSRF处理2
from SpiderWeb.common import *

def getIndexPage(request):
    return render(request, 'index.html')  # render 相当于打包的意思，第一个参数固定

# @csrf_exempt (1)
def getSingerIDEx(request):
    if request.POST['name'] == '':
        return HttpResponse(json.dumps({"data": 'EmptyError'}),
                            content_type='application/json')
    name = request.POST['name']

    singerIDEx = getSingerIdFromFile('C:\\Users\\Administrator\\Desktop\\WXpy\\歌手ID\\SingerID.txt',name)
    # print('{}:  {}:'.format(name,singerIDEx))
    if len(singerIDEx) > 0:
        return HttpResponse(json.dumps({"data": singerIDEx}),
                        content_type='application/json')
    else:
        return HttpResponse(json.dumps({"data": 'Not Found'}),
                            content_type='application/json')

def searchSongByName(request):
    if request.POST['name'] == '':
        return HttpResponse(json.dumps({"data": 'EmptyError'}),
                            content_type='application/json')
    name = request.POST['name']
    singerIDEx = getSingerIdFromFile('static/file/SingerID.txt', name)

    dataArr = []
    if len(singerIDEx) > 0:
        start_url = 'http://music.163.com/artist?id={}'.format(singerIDEx[0])
        singer_infos = getSingerInfo(start_url,name)

        if singer_infos == 0:
            return HttpResponse(json.dumps({"data": 'running error'}),
                                content_type='application/json')
        for item in singer_infos:
            dataArr.append(json.dumps({'name': item[1], 'id': item[0]}, sort_keys=True, indent=2, separators=(',', ': '),ensure_ascii=False))

        return HttpResponse(json.dumps({"data":dataArr }),
                        content_type='application/json')
    else:
        return HttpResponse(json.dumps({"data": 'Not Found'}),
                            content_type='application/json')

def playSong(request):
    id = request.POST['id']

    data = []
    singer_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(id)
    url = 'http://music.163.com/song?id={}'.format(id)
    strHtml = getHtml(url)
    soup = BeautifulSoup(strHtml, "html.parser")
    autoDodwnImg(soup,id,1)
    lyric = getlyric(id)
    data.append(json.dumps({'url': singer_url, 'lyric': lyric}, sort_keys=True, indent=2, separators=(',', ': '),
                              ensure_ascii=False))
    return HttpResponse(json.dumps({"data": data}),
                        content_type='application/json')
