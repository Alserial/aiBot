# encoding:utf-8

import requests
from bot.bot import Bot
from bot.session_manager import Session
from bot.session_manager import SessionManager
from bridge.reply import Reply, ReplyType
from config import conf

user_session = dict()


# OpenAI对话模型API (可用)
class AigoBot(Bot):
    def __init__(self):
        super().__init__()
        self.sessions = SessionManager(Session)

    def reply(self, query, context=None):
        url = "https://aigo.work/api/v2/client/gptChat/chatForWX"
        msg = context["msg"]
        to_user_id = "@" + msg.to_user_nickname
        if msg.is_group:
            to_user_id = msg.other_user_nickname + to_user_id

        req_json = {
            "fromUserId": context["session_id"],
            "modelType": 1,
            "problem": query,
            "toUserId": to_user_id
        }
        #print(req_json)
        print(context)
        #print(context["msg"])
        headers = { "content-type": "application/json" }
        response = requests.post(url, json=req_json, headers=headers)
        print(response)
        if response:
            resp_json = response.json()
            status = resp_json["status"]
            if status == 200:
                data = resp_json["data"]
                if data:
                    return Reply(ReplyType.TEXT, data["content"])
            elif status != 404:
                return Reply(ReplyType.TEXT, "系统繁忙，请稍后再试")
        
