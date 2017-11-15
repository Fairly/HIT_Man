# -*- coding: utf-8 -*-
# filename: main.py
from flask import Flask, request
from wechatpy import WeChatClient
from wechatpy import parse_message
from wechatpy.replies import create_reply

from app_ import appid, secret, ip

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


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/wx', methods=['GET', 'POST'])
def handle():
    if request.method == 'POST':
        try:
            webData = request.data()
            print("Handle Post webdata is ", webData)  # 后台日志
            recMsg = parse_message(webData)
            if recMsg.type == 'text':
                reply = create_reply('text reply', message=recMsg)
                # 转换成 XML
                xml = reply.render()
                return xml
            else:
                print("暂且不处理")
                return "success"
        except Exception as Argument:
            return Argument
    if request.method == 'GET':
        return 'From handle.get'


@app.route('/login/', methods=["GET", "POST"])
def login_page():
    error = ''
    try:

        if request.method == "POST":

            attempted_username = request.form['username']
            attempted_password = request.form['password']

            # flash(attempted_username)
            # flash(attempted_password)

        return 'Login success!'

    except Exception as e:
        # flash(e)
        return e


if __name__ == '__main__':
    app.run(host=ip, port=80)
