# SpiderWeb
网易云音乐爬取学习
# Python3-6-0
# Author：WING

下载歌曲需要注意python3 urlretrieve 需要导入 import urllib.request<br/>  

1、编写HTTP头部信息，伪造浏览器发送请求<br/> 
2、获取爬取页的URL ，在url可以看到歌手的ID，命令行输入歌手ID开始程序<br/> 
3、通过爬取歌手详细页获取歌曲名字 和 歌曲ID 的节点<br/> 
4、通过网页云API转换获取歌词JSON数据<br/> 
5、通过歌曲ID和名字加上对外连接下载地址获取歌曲源文件（怎么获取对外连接下载地址是个问题）<br/>
6、加入了Django框架构建前端页面展示数据<br/>
