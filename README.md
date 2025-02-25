# ebookspider
用于爬取tongli ebook已购买的漫画，导出为jpg。需要代理到台湾，因此大陆需要网络代理。
首先需要运行edge并打开调试接口,找到edge.exe程序位置并开启debug接口并设置存储位置。
```
"path/to/msedge.exe" --remote-debugging-port=9222 --user-data-dir="save/path"
```
浏览器打开后要保证只显示一张图，并且不再动浏览器（浏览器窗口大小变化可能会刷新页面）。
接下来需要进行东立的账号登录（支持谷歌登录）。登录后运行脚本，等连接到浏览器后，找到你要爬取漫画的url并在脚本中输入你的漫画的url。之后浏览器会进行跳转，等到当漫画第一张图加载完毕后，在命令行中输入“y”开始爬取。
![image](https://github.com/user-attachments/assets/a822bb2d-2204-43de-bafb-5134c486a47d)
进过一段时间后得到图片存储在pic目录下、
![image](https://github.com/user-attachments/assets/fa49b344-fffc-457c-ac86-dc4fe5f98874)
