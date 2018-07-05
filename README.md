# SpiderWeb
网易云音乐爬取学习
# Author：WING

下载歌曲需要注意python3 urlretrieve 需要导入 import urllib.request<br/>  

1、编写HTTP头部信息，伪造浏览器发送请求<br/> 
2、通过网页传来的歌手名，在歌手ID文件一行一行查询，查找到就进行下一步操作获取歌手的歌曲信息，找不到返回相应信息<br/> 
3、通过爬取歌手详细页获取歌曲名字 和 歌曲ID 的节点<br/> 
4、通过网页云API转换获取歌词JSON数据<br/> 
5、通过歌曲ID和名字加上对外连接下载地址获取歌曲源文件（怎么获取对外连接下载地址是个问题）<br/>
6、加入了Django框架构建前端页面展示数据<br/>

<h3>程序运行展示</h3>
<img src="https://github.com/wing-cen/SpiderWeb/blob/master/web.png"/>
