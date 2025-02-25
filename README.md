用于爬取tongli ebook已购买的漫画，导出为jpg
首先需要运行edge,找到edge程序位置并开启debug接口。设置存储位置。
"path/to/msedge.exe" --remote-debugging-port=9222 --user-data-dir="save/path"
接下来进行东立账号登录，可以使用谷歌登录。运行脚本，打开已购买的漫画网页后在输入“ok”进行当前漫画爬取。
