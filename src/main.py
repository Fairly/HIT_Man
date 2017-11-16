# -*- coding: utf-8 -*-
# filename: main.py
from flask import Flask, request, redirect
from wechatpy import WeChatClient
from wechatpy import parse_message
from wechatpy.replies import create_reply

from .config import appid, secret, ip

app = Flask(__name__)

# Update the menu, uncomment if the menu needs to change
client = WeChatClient(appid, secret)
rtn_msg = client.menu.create({
    "button": [
        {
            "type": "click",
            "name": "今日??",
            "key": "CLICK_TODAY"
        },
        {
            "name": "菜单",
            "sub_button": [
                {
                    "type": "view",
                    "name": "登记",
                    "url": "http://" + ip + "/enroll"
                    # "url": "http://www.qq.com"
                },
                {
                    "type": "click",
                    "name": "赞一下我们!",
                    "key": "CLICK_GOOD"
                }
            ]
        },
        {
            "type": "click",
            "name": "关于??",
            "key": "CLICK_ABOUT"
        },
    ]
})
print(rtn_msg)


@app.route('/enroll')
def enroll():
    return 'try to enroll!'


def handle_event(recMsg):
    if recMsg.event == 'view':
        redirect(recMsg.url)


@app.route('/wx', methods=['POST'])
def message_reply():
    if request.method == 'POST':
        try:
            webData = request.data
            app.logger.info("Handle Post webdata is " + str(webData))  # 后台日志
            recMsg = parse_message(webData)
            if recMsg.type == 'text':
                reply = create_reply('text reply', message=recMsg)
                # 转换成 XML
                xml = reply.render()
                return xml
            elif recMsg.type == 'event':
                # handle_event(recMsg)
                return 'success'
            else:
                app.logger.warning("Unsupported message type. Do nothing.")
                return "success"
        except Exception as e:
            app.logger.error(e)
