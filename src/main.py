# -*- coding: utf-8 -*-
# filename: main.py
from flask import Flask, request
from wechatpy import WeChatClient
from wechatpy import parse_message
from wechatpy.replies import create_reply

from .app_ import appid, secret, ip

app = Flask(__name__)

# Update the menu, uncomment if the menu needs to change
# client = WeChatClient(appid, secret)
# rtn_msg = client.menu.create({
#     "button": [
#         {
#             "type": "click",
#             "name": "今日??",
#             "key": "CLICK_TODAY"
#         },
#         {
#             "type": "click",
#             "name": "关于??",
#             "key": "CLICK_ABOUT"
#         },
#         {
#             "name": "菜单",
#             "sub_button": [
#                 {
#                     "type": "view",
#                     "name": "登记",
#                     "url": "http://" + ip + "/enroll"
#                 },
#                 {
#                     "type": "click",
#                     "name": "赞一下我们!",
#                     "key": "CLICK_GOOD"
#                 }
#             ]
#         }
#     ]
# })
# print(rtn_msg)


@app.route('/wx', methods=['POST'])
def message_reply():
    if request.method == 'POST':
        try:
            webData = request.data
            app.logger.info("Handle Post webdata is " + webData)  # 后台日志
            recMsg = parse_message(webData)
            if recMsg.type == 'text':
                reply = create_reply('text reply', message=recMsg)
                # 转换成 XML
                xml = reply.render()
                return xml
            else:
                app.logger.warning("Unsupported message type. Do nothing.")
                return "success"
        except Exception as Argument:
            return Argument


if __name__ == '__main__':
    app.run(host=ip, port=80)
