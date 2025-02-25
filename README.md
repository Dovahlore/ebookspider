# ebookspider
## 功能
爬取wwb中漫画的canvas元素装换成jpg格式存储。
## 东立爬取
使用Edge浏览器和selenium爬取tongli ebook账号中已购买的漫画，导出为jpg。
首先需要运行edge并打开调试接口,找到edge.exe程序位置并开启debug接口并设置存储位置。
```
"path/to/msedge.exe" --remote-debugging-port=9222 --user-data-dir="save/path"
```
* 执行以上代码会自动弹出浏览器。浏览器要全屏，保证东立显示漫画的双页（除了首页封面单页），并且不再动浏览器（浏览器窗口大小变化可能会刷新页面并降低分辨率）。
* 接下来需要进行东立的账号登录（支持谷歌登录）。登录后运行脚本，等连接到浏览器后，找到你要爬取漫画的url并在脚本中输入你的漫画的url，浏览器会自动跳转到漫画页面。等到当漫画第一张图加载完毕后，在命令行中输入“y”开始爬取。
![image](https://github.com/user-attachments/assets/5c413a7a-7ce1-40b8-a3f7-71a53a14c565)

* 可以中断继续从某一页开始爬取，需要手动将将浏览器的漫画翻到相应也并完成加载。
![image](https://github.com/user-attachments/assets/a822bb2d-2204-43de-bafb-5134c486a47d)
进过一段时间后得到图片存储在pic目录下。
![image](https://github.com/user-attachments/assets/fa49b344-fffc-457c-ac86-dc4fe5f98874)
