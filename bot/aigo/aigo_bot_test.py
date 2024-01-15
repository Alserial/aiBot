# encoding:utf-8

import requests


def reply(query):
    url = "https://aigo.work/api/v2/client/gptChat/chatForWX"
    req_json = {
	    "fromUserId": "lyqtianxia",
	    "modelType": 1,
	    "problem": query,
	    "toUserId": "wxid_test"
    }
    headers = { "content-type": "application/json" }
    response = requests.post(url, json=req_json, headers=headers)
    if response:
        resp_json = response.json()
        if resp_json["status"] == 200:
            print(resp_json["data"]["content"])


reply("商标总共有多少个类别？")