# -*- coding: utf-8 -*-
# filename: handle.py

from __future__ import print_function

# import hashlib
# import web
# import wechatpy
# from wechatpy import parse_message
# from wechatpy.replies import create_reply
#
# import reply




# class Handle(object):
# def GET(self):
#     try:
#         data = web.input()
#         if len(data) == 0:
#             return "hello, this is handle view"
#         signature = data.signature
#         timestamp = data.timestamp
#         nonce = data.nonce
#         echostr = data.echostr
#         token = "MtqhD78R"  # 请按照公众平台官网\基本配置中信息填写
#
#         list_ = [token, timestamp, nonce]
#         list_.sort()
#         sha1 = hashlib.sha1()
#         map(sha1.update, list_)
#         hashcode = sha1.hexdigest()
#         print("handle/GET func: hashcode, signature: ", hashcode, signature)
#         if hashcode == signature:
#             return echostr
#         else:
#             return ""
#     except Exception as Argument:
#         return Argument

# def POST(self):
#     try:
#         webData = web.data()
#         print("Handle Post webdata is ", webData)  # 后台日志
#         recMsg = parse_message(webData)
#         if recMsg.type == 'text':
#             reply = create_reply('text reply', message=recMsg)
#             # 转换成 XML
#             xml = reply.render()
#             return xml
#         else:
#             print("暂且不处理")
#             return "success"
#     except Exception as Argument:
#         return Argument
