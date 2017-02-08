#-*- coding: utf-8 -*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from qiniu import Auth, put_file
import qiniu.config
from ctypes import *
import time

access_key = "5qxJd-0wSTXEMQ2NJKblJVzq1dJOt5WS9r2Sf3eG" # 填入你的AK
secret_key = "xjuUQ39C-KzDtjOB_B6Bg_L1rTw2T-aTvrCuZBth" # 填入你的SK
bucket_name = "thinktxt" # 填入你的七牛空间名称
url = "https://thinktxt.static.lxyour.com" # 填入你的域名地址

q = Auth(access_key, secret_key)
mime_type = "image/jpeg"
params = {'x:a': 'a'}

def upload_qiniu(path):
    dirname, filename = os.path.split(path)
    key = '%s' % filename
    key = key.decode('gbk').encode('utf8')
    token = q.upload_token(bucket_name, key)
    progress_handler = lambda progress, total: progress
    ret, info = put_file(token, key, path, params, mime_type, progress_handler=progress_handler)
    return ret != None and ret['key'] == key

if __name__ == '__main__':
    path = sys.argv[1]
    ret = upload_qiniu(path)
    if ret:
        name = os.path.split(path)[1]
        markdown_url = "![](%s/%s)" % (url, name)
        # make it to clipboard
        ahk = cdll.AutoHotkey # load AutoHotkey
        ahk.ahktextdll("") # start script in persistent mode (wait for action)
        while not ahk.ahkReady(): # Wait for AutoHotkey.dll to start
            time.sleep(0.01)
        ahk.ahkExec(u"clipboard = %s" % markdown_url.decode('gbk'))
     else: print "upload_failed"
