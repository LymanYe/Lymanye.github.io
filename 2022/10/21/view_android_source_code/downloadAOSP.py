import xml.dom.minidom
import os
from subprocess import call

## 注意地址中使用的是 "/" 而不是"\", unbantu 跟Windows 是有区别的
 
#代码保存位置，硬盘建议大于100G
rootdir = "F:/Android/AOSP/android_10_0_0_r47"
 
#git 安装路径，可以使用 where git 命令查看
git = "D:/Program Files/Git/bin/git.exe"

# 刚刚切换 android-10.0.0_r47 目录下的defaul.xml 文件
dom = xml.dom.minidom.parse("F:/Android/AOSP/clone_tsinghua/manifest/default.xml")
root = dom.documentElement

# clone 清华大学镜像库地址
prefix = git + " clone https://mirrors.tuna.tsinghua.edu.cn/git/AOSP/"
suffix = ".git"
 
if not os.path.exists(rootdir):
    os.mkdir(rootdir)
 
for node in root.getElementsByTagName("project"):
    os.chdir(rootdir)
    d = node.getAttribute("path")
    last = d.rfind("/")
    if last != -1:
        d = rootdir + "/" + d[:last]
        if not os.path.exists(d):
            os.makedirs(d)
        os.chdir(d)
    cmd = prefix + node.getAttribute("name") + suffix
    call(cmd)